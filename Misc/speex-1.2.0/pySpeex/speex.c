/*
 * speex.c
 *
 * Python wrapper for Speex speech codec (www.speex.org)
 *
 * Defines a 'speex' object through which encoding and
 * decoding can be done
 */

#include <speex.h>
#include "Python.h"

/*
 * Module docstring
 */

char pyspeex_module_doc[] =
"Module: speex\n"
"\n"
"by David McNab <david@rebirthing.co.nz>\n"
"\n"
"This Python module implements a Python wrapper to the Speex\n"
"speech codec, (http://www.speex.org), providing a class\n"
"called 'speex' which can be used to encode and decode streams\n"
"of audio speech data\n"
;


/*
 * Structure of speex python object. Contains all required
 * buffers and config data
 */

#define BYTES_PER_FRAME (sizeof(short))

typedef struct 
{
  PyObject_HEAD
  long arg1;
  long arg2;
  // todo - declare my needed object vars here

  /* Data for encoding */
  void *encState;
  int encQuality;
  int encFramesPerBlock; // number of frames per block
  float *encBuf;
  float *encPtr;
  int encNumFrames;
  SpeexBits encBits;

  /* Data for decoding */
  void *decState;
  int decQuality;
  unsigned char *decBuf;
  unsigned char *decPtr;
  unsigned short decBlkSize;
  int decNumBytes;
  int decPhase;
  int decEnhanceOn;
  SpeexBits decBits;

} SpeexObject;

staticforward PyTypeObject SpeexType;

#define is_SpeexObject(v)		((v)->ob_type == &SpeexType)

static SpeexObject *
newSpeexObject(void)
{
	SpeexObject * new;
	new = PyObject_New(SpeexObject, &SpeexType);
    // todo - fill in object vars as needed (defined in SpeexObject)
	return new;
}

static void
SpeexDealloc(PyObject *ptr)
{		
	SpeexObject *self = (SpeexObject *)ptr;

    /*Destroy the encoder state and data*/
    speex_encoder_destroy(self->encState);
    if (self->encBuf != NULL)
      free(self->encBuf);

    /*Destroy the encoder state*/
    speex_encoder_destroy(self->decState);
    if (self->decBuf != NULL)
      free(self->decBuf);

    /*Destroy the bit-packing structs*/
    speex_bits_destroy(&self->encBits);
    speex_bits_destroy(&self->decBits);

	/* Overwrite the contents of the object */
    // todo - close down stream, finalise speex etc
	PyObject_Del(ptr);
}


static char SpeexNew__doc__[] = 
"new(): Create a new speex speech stream object\n"
"\n"
"Arguments:\n"
" - quality - 0 (lowest) to 10 (highest), default 8\n"
"\n"
"The created speex stream object has two methods:\n"
" - encode - encode a block of speech audio data\n"
"\n"
"   Arguments:\n"
"    - block of audio data, as sequence of frames, where\n"
"      each frame is an int\n"
"\n"
"   Returns:\n"
"    - raw string containing encoded data, or\n"
"      empty string if there is not yet any encoded\n"
"      data available\n"
"\n"
" - decode - decodes a block of speech audio data\n"
"\n"
"   Arguments:\n"
"    - block of encoded data, as raw string,\n"
"\n"
"   Returns:\n"
"    - block of audio data, as sequence of ints, or\n"
"      an empty sequence if there is no decoded data\n"
"      available yet\n"
"\n"
"Notes:\n"
" - Both of these methods use internal buffering, which means that\n"
"   you can feed in data piecemeal. This helps a lot when sending and\n"
"   receiving data over the net."
;

static SpeexObject *
SpeexNew(PyObject *self, PyObject *args, PyObject *kwds)
{
  // todo - add keywords pertinent to speex
  static char *kwlist[] = {"quality", NULL};
  SpeexObject *new = NULL;
  int encQuality = 8;

  /* Set default values */
  if (!PyArg_ParseTupleAndKeywords(args, kwds, "|i",
                                   kwlist,
                                   &encQuality)) 
    return NULL;

  /* Create and initialise new object */
  new = newSpeexObject();

  /* Set up encoder */
  new->encState = speex_encoder_init(&speex_nb_mode);
  speex_encoder_ctl(new->encState, SPEEX_SET_QUALITY, &encQuality);
  speex_encoder_ctl(new->encState, SPEEX_GET_FRAME_SIZE, &new->encFramesPerBlock);
  //printf("encoder frame size=%d\n", new->encFramesPerBlock);
  new->encBuf = malloc(new->encFramesPerBlock * sizeof(float));
  memset(new->encBuf, 0, new->encFramesPerBlock * sizeof(float));
  if (new->encBuf == NULL)
    return NULL;
  new->encNumFrames = 0;
  new->encPtr = new->encBuf;
  speex_bits_init(&new->encBits);

  /* Set up decoder */
  new->decState = speex_decoder_init(&speex_nb_mode);
  new->decEnhanceOn = 1;
  speex_decoder_ctl(new->decState, SPEEX_SET_ENH, &new->decEnhanceOn);
  new->decBuf = malloc(2); // just big enough for leading length field
  new->decPhase = 0;
  if (new->decBuf == NULL)
    return NULL;
  new->decPtr = new->decBuf;
  new->decNumBytes = 0;
  speex_bits_init(&new->decBits);

  return new;
}

char pyspeex_encode_doc[] =
"Encode some audio data\n"
"\n"
"Arguments:\n"
"  - data - sequence of audio frames to encode\n"
"Returns:\n"
"  - raw string with encoded data\n"
;

PyObject *pyspeex_encode(PyObject *ptr, PyObject *args, PyObject *kwds)
{
  SpeexObject *self = (SpeexObject *)ptr;
  static char *kwlist[] = {"data", NULL};
  PyObject *inputFramesList = NULL;
  //PyObject *tmpobj;
  int numInputFrames;
  float *framesBuf, *framesPtr;
  int i;
  int totFrames;
  /*SpeexBits bits;*/
  int cbitsSiz = self->encFramesPerBlock * 5 / 4;
  //int cbitsSiz = 2048;
  //char cbits[cbitsSiz];
  char cbits[2048];
  int nBlocks;
  int nBytes;
  char *bufOut = malloc(0);
  int bufOutSiz = 0;
  int remainder;

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", kwlist,
                                   &inputFramesList))
    return NULL; 

  /* Determine number of frames */
  numInputFrames = PyList_Size(inputFramesList);

  //printf("enc - numInputFrames = %d\n", numInputFrames);

  if (numInputFrames == 0)
    return Py_BuildValue("s", "");

  /* Encode what we have, block by block */
  totFrames = numInputFrames + self->encNumFrames;
  //printf("totFrames=%d, input data size=%d\n",
  //totFrames, totFrames * BYTES_PER_FRAME);
  framesBuf = framesPtr = malloc(totFrames * sizeof(float));
  if (framesBuf == NULL)
    {
      PyErr_SetString(PyExc_MemoryError, "speex.encode: malloc fail");
      return NULL;
    }
  
  /* Copy in the fragments we have in buffer */
  //printf("copying in buf of %d frames\n", self->encNumFrames);
  for (i = 0; i < self->encNumFrames; i++)
    {
      *framesPtr++ = self->encBuf[i];
      //*framesPtr++ = 0;
    }
  
  /* Extract the rest from input sequence */
  //printf("copying extra %d frames from input\n", numInputFrames);
  for (i = 0; i < numInputFrames; i++)
    *framesPtr++ = PyInt_AsLong(PyList_GetItem(inputFramesList, i));

  //printf("written %d frames to buf\n", framesPtr - framesBuf);

  /* Encode these frames */
  nBlocks = totFrames / self->encFramesPerBlock;
  framesPtr = framesBuf;
  for (i = 0; i < nBlocks; i++)
    {
      //printf("seeking to encode a block, nBlocks=%d\n", nBlocks);
      speex_bits_reset(&self->encBits);
      //printf("ok1 - state=0x%lx, buf=0x%lx, bits=0x%lx\n",
         //self->encState, framesBuf, &self->encBits);
      speex_encode(self->encState, framesPtr, &self->encBits);
      //printf("ok2\n");
      nBytes = speex_bits_write(&self->encBits, cbits, cbitsSiz);
      //printf("ok3\n");
      bufOut = realloc(bufOut, bufOutSiz+nBytes+2);
      //printf("ok4\n");
      // write out 2 length bytes
      bufOut[bufOutSiz++] = nBytes % 256;
      bufOut[bufOutSiz++] = nBytes / 256;
      memcpy(bufOut+bufOutSiz, cbits, nBytes);
      //printf("ok5\n");
      bufOutSiz += nBytes;
      //printf("ok6\n");

      framesPtr += self->encFramesPerBlock;
    }

  /* stick remainder, if any, into buffer */
  self->encNumFrames = totFrames - (nBlocks * self->encFramesPerBlock);
  remainder = self->encNumFrames * sizeof(float);
  memcpy(self->encBuf, framesPtr, remainder);
  //memset(self->encBuf, 0, self->encFramesPerBlock * sizeof(float));
  //printf("encNumFrames=%d\n", self->encNumFrames);
  //printf("remainder=%d\n", remainder);

  /* ditch temp buffer */
  free(framesBuf);

  /* pass back encoded buffer as raw string */
  //printf("bufOutSize=%d\n", bufOutSiz);
  return Py_BuildValue("s#", bufOut, bufOutSiz);
}

char pyspeex_decode_doc[] =
"Decode an encoded block, return as sequence of frame tuples\n"
"\n"
"Arguments:\n"
"  - encoded - raw string, containing encoded data\n"
"Returns:\n"
"  - decoded blocks, as sequence of frames, where each frame\n"
"    is an int\n"
;

PyObject *pyspeex_decode(PyObject *ptr, PyObject *args, PyObject *kwds)
{
  SpeexObject *self = (SpeexObject *)ptr;
  char *kwlist[] = {"data", NULL};
  unsigned char *encBuf = NULL;
  unsigned char *encBufEnd = NULL;
  unsigned char *encPtr = NULL;
  int encBufLen = 0;
  int numDecFrames; /* number of decoded frames */
  //int cbitsSiz = self->encFramesPerBlock * 5 / 4;
  //char cbits[cbitsSiz];
  float *decFloats = malloc(0);
  float *decFloats1;
  short *decShorts = malloc(0);
  short *decShorts1;
  int decBlocks = 0;
  PyObject *ret;
  int i;

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "s#", kwlist,
                                   &encBuf, &encBufLen))
    return NULL; 

  // We get an earlymark if caller provided no data
  if (encBufLen == 0)
    return Py_BuildValue("[]");

  /* decode the sucker */
  encPtr = encBuf;
  encBufEnd = encBuf + encBufLen;

  while (encPtr < encBufEnd)
    {
      /* state depends on whether we've received the block header count bytes */
      if (self->decPhase == 0)
        {
          // Grab LSB of block size
          self->decBuf[0] = *encPtr;
          self->decPhase = 1;
          encPtr++;
          encBufLen--;
          continue;
        }
      else if (self->decPhase == 1)
        {
          // Grab MSB of block size and determine total block size
          self->decBuf[1] = *encPtr;
          self->decBlkSize = self->decBuf[0] + 256 * self->decBuf[1];

          // resize dec buffer to suit
          // todo - find better way to sanity check the size
          self->decBuf = realloc(self->decBuf, self->decBlkSize);
          self->decPtr = self->decBuf;
          self->decNumBytes = 0;
          self->decPhase = 2;
          encPtr++;
          encBufLen--;
          continue;
        }
      else
        {
          int needed = self->decBlkSize - self->decNumBytes;

          // do we have enough input data to complete a frame?
          if (encBufLen >= needed)
            {
              int newNumFrames = (decBlocks + 1) * self->encFramesPerBlock;

              // great - decode frame and add to our array of shorts
              memcpy(self->decPtr,
                     encPtr, self->decBlkSize - self->decNumBytes);
              encPtr += needed;
              encBufLen -= needed;

              // do the decoding
              // expand shorts and floats buffers
              decShorts = realloc(decShorts, newNumFrames * sizeof(short));
              decShorts1 = decShorts + decBlocks * self->encFramesPerBlock;
              decFloats = realloc(decFloats, newNumFrames * sizeof(float));
              decFloats1 = decFloats + decBlocks * self->encFramesPerBlock;

              /*Copy the data into the bit-stream struct*/
              speex_bits_read_from(&self->decBits, self->decPtr, self->decBlkSize);

              /*Decode the data*/
              speex_decode(self->decState, &self->decBits, decFloats1);

              /*Copy from float to short (16 bits) for output*/
              for (i=0; i < self->encFramesPerBlock; i++)
                decShorts1[i] = decFloats1[i];

              self->decPhase = 0; // back to awaiting LSB of count header
              self->decNumBytes = 0;
              self->decBuf = realloc(self->decBuf, 2);
              decBlocks++;
              continue;
            }
          else
            {
              // not enough to decode another speex frame - just stick into buffer
              memcpy(self->decPtr, encPtr, encBufLen);
              self->decPtr += encBufLen;
              encBufLen = 0;
              break;
            }
        }
    }

  /* did we get anything? */
  if (decBlocks > 0)
    {
      /* build up a sequence of tuples */
      numDecFrames = decBlocks * self->encFramesPerBlock;
      ret = PyList_New(numDecFrames);
      for (i = 0; i < numDecFrames; i++)
        PyList_SET_ITEM(ret, i, Py_BuildValue("i", decShorts[i]));
    }
  else
    ret = Py_BuildValue("[]");
  free(decShorts);
  free(decFloats);
  return ret;
  //return Py_BuildValue("s#", decBuf, decBufLen);
}

/* stream object methods */

static PyMethodDef SpeexStreamMethods[] =
{
  //{"name", (PyCFunction)function, METH_KEYWORDS|METH_VARARGS, docstring},
  {"encode",
   (PyCFunction)pyspeex_encode,
   METH_VARARGS|METH_KEYWORDS,
   pyspeex_encode_doc
  },
  {"decode",
   (PyCFunction)pyspeex_decode,
   METH_VARARGS|METH_KEYWORDS,
   pyspeex_decode_doc
  },
  {NULL, NULL}			/* sentinel */
};


static int SpeexSetattr(PyObject *ptr, char *name, PyObject *val)
{
  SpeexObject *self=(SpeexObject *)ptr;

  if (!strcmp(name, "arg1"))
    {
      self->arg1 = PyInt_AsLong(val);
    }
  else if (!strcmp(name, "arg2"))
    {
      self->arg2 = PyInt_AsLong(val);
      //printf("arg2=%ld\n", self->arg2);
    }
  else
    {
      PyErr_Format(PyExc_AttributeError,
		   "non-existent attribute '%s'",
		   name);
      return -1;
    }

  return 0;
}

static PyObject *
SpeexGetattr(PyObject *s, char *name)
{
  SpeexObject *self = (SpeexObject*)s;
  if (!strcmp(name, "arg1"))
      return PyInt_FromLong((long)self->arg1);
  else if (!strcmp(name, "arg2"))
      return PyInt_FromLong((long)self->arg2);

  return Py_FindMethod(SpeexStreamMethods, (PyObject *) self, name);
}

/* List of functions defined in the module */

static struct PyMethodDef SpeexMethods[] =
{
 {"new", (PyCFunction) SpeexNew, METH_VARARGS|METH_KEYWORDS, SpeexNew__doc__},
 {NULL, NULL}			/* sentinel */
};

static PyTypeObject SpeexType =
{
	PyObject_HEAD_INIT(NULL)
	0,				/*ob_size*/
	"speex",		/*tp_name*/
	sizeof(SpeexObject),	/*tp_size*/
	0,				/*tp_itemsize*/
	/* methods */
	SpeexDealloc,	/*tp_dealloc*/
	0,				/*tp_print*/
	SpeexGetattr,	/*tp_getattr*/
	SpeexSetattr,    /*tp_setattr*/
	0,			/*tp_compare*/
	(reprfunc) 0,			/*tp_repr*/
	0,				/*tp_as_number*/
};

/* Initialization function for the module */

#if PYTHON_API_VERSION < 1011
#define PyModule_AddIntConstant(m,n,v) {PyObject *o=PyInt_FromLong(v); \
           if (o!=NULL) \
             {PyDict_SetItemString(PyModule_GetDict(m),n,o); Py_DECREF(o);}}
#endif

void
initspeex(void)
{
  PyObject *m;
  
  SpeexType.ob_type = &PyType_Type;

  /* Create the module and add the functions */
  m = Py_InitModule3("speex", SpeexMethods, pyspeex_module_doc);

  //PyModule_AddIntConstant(m, "myconstant", 415);

  /* Check for errors */
  if (PyErr_Occurred())
    Py_FatalError("can't initialize module speex");
}

