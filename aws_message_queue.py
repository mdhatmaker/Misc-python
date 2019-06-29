import boto.sqs
from boto.sqs.message import Message
import wave, struct
import scipy.io.wavfile
import sys
import pyaudio  
import wave  
import lz4

def play_wav(filename):
    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    f = wave.open(filename,"rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    total_data = ''

    #play stream
    while data:
        total_data += data
        stream.write(data)
        #data_size += len(data)
        data = f.readframes(chunk)  
    print "data size:", len(total_data)
    
    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()
    return total_data

def compress(data):
    compressed_data = lz4.block.compress(data)
    print "compressed", len(data), "to", len(compressed_data)
    return compressed_data

def decompress(compressed_data):
    data = lz4.block.decompress(compressed_data)
    print "decompressed", len(compressed_data), "to", len(data)
    return data


"""
waveFile = wave.open('gladiators.wav', 'r')

length = waveFile.getnframes()
for i in range(0,length):
    waveData = waveFile.readframes(1)
    #data = struct.unpack("<h", waveData)
    data = struct.unpack("<h", waveData[2])
    print(int(data[0]))
waveFile.close()
"""

audiofilename = 'gladiators.wav'
#sampling_rate, np_array_data = scipy.io.wavfile.read(audiofilename)

[samplerate, x] = scipy.io.wavfile.read(audiofilename) # x is a numpy array of integer, representing the samples 
# scale to -1.0 -- 1.0
if x.dtype == 'uint8':
    nb_bits = 8 # -> 8-bit wav files
    print "8-bit wav file"
if x.dtype == 'int16':
    nb_bits = 16 # -> 16-bit wav files
    print "16-bit wav file"
elif x.dtype == 'int32':
    nb_bits = 32 # -> 32-bit wav files
    print "32-bit wav file"
max_nb_bit = float(2 ** (nb_bits - 1))
samples = x / (max_nb_bit + 1.0) # samples is a numpy array of float representing the samples

wav_data = play_wav(audiofilename)

compressed = compress(wav_data)
uncompressed = decompress(compressed)

sys.exit()

# Create connection and queue
conn = boto.sqs.connect_to_region("us-west-2", aws_access_key_id="AKIAIBLFZLNPLNRBQDYQ", aws_secret_access_key="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")
q = conn.create_queue('myqueue')

conn.get_all_queues()
#[Queue(https://us-west-2.queue.amazonaws.com/318295528387/icb.fifo), Queue(https://us-west-2.queue.amazonaws.com/318295528387/myqueue)]

# Get a specific queue
#my_queue = conn.get_queue('myqueue')

# Create a simple message and write it to queue
mo = Message()
mo.set_body('This is my first message.')
q.write(mo)

# Read messages from the queue
rs = q.get_messages()
print len(rs), "messages retrieved"

# Display body of first message
mi = rs[0]
print mi.get_body()


# Write 10 more messages
for i in range(1, 11):
    mo = Message()
    mo.set_body('This is message %d' % i)
    q.write(mo)


rs = q.get_messages(10)
print len(rs), "messages retrieved"


print rs[0].get_body()
print rs[1].get_body()


print "qcount:", q.count()


rs = q.get_messages()
print len(rs), "messages retrieved"

print "qcount:", q.count()


# Attempt to read messages (with specified timeout in seconds)
m = q.read()
while m != None:
    print m.get_body()
    m = q.read()
    



