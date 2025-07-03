import pyttsx3 as pyt 
from gtts import gTTS

class Convert:
    def __init__(self, path):
        self.engine = pyt.init()
        
        with open(path, 'r') as file:
            self.file = file.read()
        
    def say(self):
        self.engine.say(self.file)
        self.engine.runAndWait()
    
    def save(self,filename):
        tts = gTTS(text=self.file, lang='ru')
        tts.save(filename)
    