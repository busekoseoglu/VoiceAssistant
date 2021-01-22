import wikipedia
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wolframalpha

#text = input("Enter searching value: ")

#result = wikipedia.summary(text, sentences=2)
#print(result)

class voiceAssistant():

    def __init__(self):
        self.main()


    def speak(self,result):
        self.engine = pyttsx3.init()
        self.engine.say(result)
        self.engine.runAndWait()

    def wish(self):
        self.hour = datetime.datetime.now().hour
        if self.hour >= 0 and self.hour < 12:
            self.speak("Good Morning")
        elif self.hour >=12 and self.hour < 19:
            self.speak("Good Afternoon")
        else: 
            self.speak("Good Evening")

    def listen(self):
        self.speak("How can i help you")
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            print("talk")
            self.audio = self.r.listen(source)
        return self.audio

    def search_wiki(self, audio):
            
        self.phrase = self.r.recognize_google(audio, language="en-US")
        print(f"phrase: {self.phrase}\n")
        self.result = wikipedia.summary(self.phrase, sentences=2)
        return self.result

    def open_tabs(self,audio):
        self.phrase = self.r.recognize_google(audio, language="en-US").lower()
        if "open youtube" in self.phrase:
            webbrowser.open_new_tab("https://www.youtube.com")
            self.speak("I am opening youtube")
        elif "open google" in self.phrase:
            webbrowser.open_new_tab("https://www.google.com")
            self.speak("I am opening google")
        elif "open twitter" in self.phrase:
            webbrowser.open_new_tab("https://www.twitter.com")
            self.speak("I am opening twitter")
        elif "open github" in self.phrase:
            webbrowser.open_new_tab("https://github.com")
            self.speak("I am opening github")

    def wolfram(self,audio):
        client = wolframalpha.Client("U84E24-3QRQXA62A2")
        self.res = client.query(audio)
        self.speak(next(self.res.results).plainText)

    def main(self):
        while True:
            self.wish()
            audio = self.listen()
            self.phrase = self.r.recognize_google(audio, language="en-US")
            self.phrase.lower()
            if "open" in self.phrase:
                self.open_tabs(self.listen())
            elif "wikipedia" in self.phrase:
                self.search_wiki(self.listen())
            else:
                self.wolfram(self.listen())
            self.speak("bye bye")
            break



va = voiceAssistant()