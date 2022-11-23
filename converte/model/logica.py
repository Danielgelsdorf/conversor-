#import entrada
import pyttsx3  
class Meio:
    def transformaTV(self,meuTexto):
        trans=pyttsx3.init()
        aumentar=trans.getProperty('rate')
        trans.setProperty('aumentar',aumentar+100)
        trans.say(meuTexto)
        trans.runAndWait()
    def transformaVT(self, audio,rec):
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
