import speech_recognition as sr 
import pyaudio as pa
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
# import gTTs

def aiProcess(command):
    client = OpenAI(api_key="[your api key]",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://www.google.com/")
   elif "open facebook" in c.lower():
      webbrowser.open("https://www.facebook.com/")
   elif "open youtube" in c.lower():
      webbrowser.open("https://www.youtube.com/")
   elif "open tiktok" in c.lower():
      webbrowser.open("https://www.tiktok.com/")
   elif "open linkdein" in c.lower():
      webbrowser.open("https://www.linkedin.com/")
   elif c.lower().startswith('play'):
      song=c.lower().split(' ')[1]
      link= musicLibrary.music[song]
      webbrowser.open(link)
   elif "news" in c.lower():
      r=requests.get("https://newsapi.org/v2/top-headlines?country=np&apiKey=0c425f8ac853490983347608fbd48063")
      if r.status_code==200:
         data=r.json()

         #wxtract the article
         articles=data.get('articles',[])
         #print the headlines
         for article in articles:
            speak(article['title'])

      else:
         #open ai handle the request
         output=aiProcess(c)
         speak(output)


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="0c425f8ac853490983347608fbd48063"
def speak(text):
    engine.say(text)
    engine.runAndWait()

    

if __name__=="__main__":
    speak('Initializing jarvis....')
    #listen for the word jarvis
    while True:
        r=sr.Recognizer()
        

        #reconize speech using Sphinx
        try:
            with sr.Microphone() as source:
              print("Listening..")
              audio=r.listen(source,timeout=3,phrase_time_limit=1)

            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
             speak("yaa")
             #listen for command
             with sr.Microphone() as source:
              print("jarvis active.")
              audio=r.listen(source)
              command=r.recognize_google(audio)
              processCommand(command)

        
        except Exception as e:
             print("error{0}".format(e))



