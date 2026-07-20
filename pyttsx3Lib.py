#It's a text to speech converter which works offline either
import pyttsx3 as ts #type: ignore  #python pyttsx3Lib.py for tts work
engine = ts.init()

#to get the properties of the engine
rate=engine.getProperty('rate')
volume=engine.getProperty('volume')
voices=engine.getProperty('voices')
print(rate,volume,voices)

#to know the voices available in the system
for voice in voices:
    print(voice.id,voice.name)

#to set the properties of the engine
engine.setProperty('rate',190)
engine.setProperty('volume',0.9)
engine.setProperty('voice',voices[1].id)

engine.say("you were lying first research the content then give the proof")
engine.runAndWait()