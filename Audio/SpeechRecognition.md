https://www.datasciencewiki.com/2019/12/speechvoiceaudio-to-text-conversion.html


Speech/Voice/Audio to Text Conversion using Python | SpeechRecognition
Cloud TVDecember 12, 2019


Prerequisite
Operating System(OS)
Python

Walk-through
SpeechRecognition is a python library for performing speech recognition, with support for several engines and APIs, online and offline.

Below are the Speech recognition engine/API support as of now:

CMU Sphinx (works offline)
Google Speech Recognition
Google Cloud Speech API
Wit.ai
Microsoft Bing Voice Recognition
Houndify API
IBM Speech to Text
Snowboy Hotword Detection (works offline)

voice_to_speech_demo.py

# Import the necessary packages
import speech_recognition as sr

if __name__ == "__main__":
    print("Application Started ... ")
    r = sr.Recognizer()
    audio = sr.AudioFile("D:\\voice_to_speech\\audio_file.wav")

    with audio as source:
        audio = r.record(source, duration=100)
        print(r.recognize_google(audio))

    '''with audio as source:
        audio = r.record(source, duration=100)
        print(r.recognize_google(audio, language='en-IN', show_all=True))'''

    print("Application Completed.")

Output
D:\softwares\installed\Anaconda2\Anaconda2\python.exe C:/Users/UserName/PycharmProjects/voice_to_speech/voice_to_speech_demo.py
Application Started ... 
Hello World India
Application Completed.

Process finished with exit code 0

Summary
In this article, we have successfully learned how to convert Speech/voice/audio to Text Conversion using Python package SpeechRecognition. Please go through all these steps and provide your feedback and post your queries/doubts if you have. Thank you. Appreciated.

Happy Learning !!!