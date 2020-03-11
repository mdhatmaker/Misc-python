#!/usr/bin/env python
import sys
import os
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams

# main
def convertPDF(outfile,pdfFile):
    # debug option
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    #outfile = None
    outtype = None
    outdir = None
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    """    for (k, v) in opts:
        if k == '-d': debug += 1
        elif k == '-p': pagenos.update( int(x)-1 for x in v.split(',') )
        elif k == '-m': maxpages = int(v)
        elif k == '-P': password = v
        elif k == '-o': outfile = v
        elif k == '-C': caching = False
        elif k == '-n': laparams = None
        elif k == '-A': laparams.all_texts = True
        elif k == '-V': laparams.detect_vertical = True
        elif k == '-M': laparams.char_margin = float(v)
        elif k == '-L': laparams.line_margin = float(v)
        elif k == '-W': laparams.word_margin = float(v)
        elif k == '-F': laparams.boxes_flow = float(v)
        elif k == '-Y': layoutmode = v
        elif k == '-O': outdir = v
        elif k == '-t': outtype = v
        elif k == '-c': codec = v
        elif k == '-s': scale = float(v)
    #"""
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug
    PDFDevice.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)
    if not outtype:
        outtype = 'text'
        if outfile:
            if outfile.endswith('.htm') or outfile.endswith('.html'):
                outtype = 'html'
            elif outfile.endswith('.xml'):
                outtype = 'xml'
            elif outfile.endswith('.tag'):
                outtype = 'tag'
    if outfile:
        outfp = file(outfile, 'w')
    else:
        outfp = sys.stdout
    if outtype == 'text':
        device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)
    elif outtype == 'xml':
        device = XMLConverter(rsrcmgr, outfp, codec=codec, laparams=laparams, outdir=outdir)
    elif outtype == 'html':
        device = HTMLConverter(rsrcmgr, outfp, codec=codec, scale=scale,
                               layoutmode=layoutmode, laparams=laparams, outdir=outdir)
    elif outtype == 'tag':
        device = TagExtractor(rsrcmgr, outfp, codec=codec)
    else:
        pass  #return usage()
    fname = pdfFile  #for fname in args:
    fp = file(fname, 'rb')
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password,
                caching=caching, check_extractable=True)
    fp.close()
    device.close()
    outfp.close()
    return

def output(st):
    print st
    outfile.write(st + "\n")
    return

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "ERROR: Usage: stmtreader.py [pdf_filename]"
        sys.exit(1)

    fileToConvert = sys.argv[1]
    if not os.path.isfile(fileToConvert):
        print "ERROR: PDF file does not exist: %s" % fileToConvert
        sys.exit(1)
        
    txtFile = "temp.txt"
    print "Processing %s..." % fileToConvert
    print "(this may take several minutes)"
    convertPDF(txtFile, fileToConvert)
    print "Done."
    print ""

    # Now look through the text file to find our information
    openPositions = False
    date = None
    copperDate = None
    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

    outfile = open("tempout.txt","w")
    infile = open(txtFile,"r")
    while infile:
        line = infile.readline()
        if not line: break
        if date == None:
            abbrev = [x for x in months if x in line]
            if abbrev:
                i = line.find(abbrev[0])
                date = line[i:i+13]
                output(date)
                output("=============")
        if "O  P  E  N      P  O  S  I  T  I  O  N  S" in line:
            openPositions = True
            continue
        if "*USD-US REG*" in line:
            openPositions = False
            continue
        if openPositions == True:
            if "LME COPPER US" in line:
                i = line.find("LME COPPER US")
                copperDate = line[i-10:i]
            if copperDate == None:
                output(line)
            else:
                foundSummary = False
                words = line.split()
                for w in words:
                    if w.endswith("*"):
                        foundSummary = True
                        output(w)
                if foundSummary == True:
                    output(copperDate)
                    output("----------")
        if "CONVERTED ACCOUNT VALUE AT MKT" in line:
            accountValue = line

    words = accountValue.split("      ")
    output(words[0])
    output(words[1])

    outfile.close()
    outfileName = date.replace(',','').strip() + ".txt"
    pdfOutfileName = date.replace(',','').strip() + ".pdf"
    os.rename("tempout.txt", outfileName)
    os.rename(fileToConvert, pdfOutfileName)
    print ""
    print "Output sent to %s" % outfileName
    

    
    
    
        
    
