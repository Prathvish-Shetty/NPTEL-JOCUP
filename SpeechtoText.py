import speech_recognition as sr
Audio_File=(r"C:\Users\Prathvish Shetty\Downloads\PM Modis speech at release of autobiography of Balasaheb Vikhe Patil.wav")
#use audiofile as source
r=sr.Recognizer()    #initialise the recognizer
with sr.AudioFile(Audio_File) as source:
    audio=r.record(source)
#reads the audio file
try:
    print("audio file contains : "+r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from Google Speech Recognition")