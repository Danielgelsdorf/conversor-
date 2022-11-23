import speech_recognition as sr
from converte.model.logica import Meio
class Entrada(Meio):
    def ler(self):
        texto=(input("Digite um texto para ser convertido em voz"))
        self.transformaTV(texto)
    def ouvir(self):
        rec=sr.Recognizer()
        # print(sr.Microphone().list_microphone_names())
        with sr.Microphone(1) as mic:
            rec.adjust_for_ambient_noise(mic)
            print("ouvindo")
            audio = rec.listen(mic)
            meuTexto=self.transformaVT(audio,rec)
        return meuTexto
