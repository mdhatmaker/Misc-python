import speech_recognition as ar

if __name__ == "__main__":
    print("Application Started ...\n")
    r = ar.Recognizer()
    #audio_filename = "D:\\voice_to_speech\\audio_file.wav"
    #audio_filename = "Episode 793 Scott Adams - Impeachment Super Bowl, TDS Update, NYT's Endorsement, Sleep Tricks-eLNd7-_XmtM.m4a"
    audio_filename = "Episode 793 Scott Adams - Impeachment.clip1.wav"
    audio = ar.AudioFile(audio_filename)

    '''with audio as source:
        audio = r.record(source, duration=100)
        print(r.recognize_google(audio))'''

    json_filename = r"D:\Users\mhatm\OneDrive\Documents\credentials\My First Project-d3d72ccc6708.json"
    f = open(json_filename, 'r')
    json = f.read()

    
    #audio_duration = 25
    #audio_offset = 0
    with audio as source:
        #audio = r.record(source, duration=50)
        #audio = r.record(source, duration=audio_duration, offset=audio_offset)
        #transcript = r.recognize_google(audio, language='en-US', show_all=False)
        #transcript = r.recognize_bing(audio, api_key, language="en-US", show_all=False)
        #transcript = r.recognize_houndify()
        #transcript = r.recognize_ibm(audio, username="mhatmaker@gmail.com", password="Wikki6969", language="en-US", show_all=False)
        for x in range(6):
            audio = r.record(source, duration=50)
            transcript = r.recognize_google_cloud(audio, json, language="en-US", preferred_phrases=None, show_all=False)
            print(transcript, end='\n\n')
        #audio_offset += 1   #audio_duration

        
    print("\nApplication Completed.")  
