import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say("Eu vou falar esse Texto")
engine.runAndWait()