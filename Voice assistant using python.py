
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

# this function is write to change the voice into text format
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
             print("Recognizing....")
             data = recognizer.recognize_google(audio)  
             return data                              #change return into print while printing the speech into text
        except sr.Unknown_valueError:
            print("not understanding")
            
# this function is write to change the text format into speech            
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()  
    
#for separating two functions differently
if __name__ == '__main__':
    data1 = sptext().lower()
    if "hello siri" in data1:
        myname = "hello myself siri"
        speechtx(myname)
    elif "time" in data1:
        time = datetime.datetime.now().strftime("%I%M%p")
        speechtx(time)
    elif "youtube" in data1:
        webbrowser.open("https://www.youtube.com/")
    elif "joke" in data1:
        joke_1 = pyjokes.get_joke(language="en",category="neutral")
        print(joke_1)
        speechtx(joke_1)



