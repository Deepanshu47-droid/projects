import pandas as pd
import datetime
from plyer import notification
import pyttsx3

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def notification1(title,msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon="C:\\Users\Lenovo\Desktop\project\\birthday notifier\\happy_birthday_penguin.ico",
        timeout=8
    )

flag=0
df=pd.read_excel("C:\\Users\Lenovo\Desktop\project\\birthday notifier\Birthday-dates.xlsx")
today=datetime.datetime.now().strftime("%d-%m")
for index,item in df.iterrows():
    bd=item["Birthday"]
    if today==bd:
        flag=1
        a=item["Name"]

        notification1("Birthday Alert",f"It's {a}'s birthday today.")
        speak(f"Deepanshu !! It's {a}'s birthday today.")
        print("press a key for continue..")
        input()
    if bd == "END" and flag==0:
        notification1("Birthday Alert", "There is no one's birthday today.")
        speak("Deepanshu !! There is no one's birthday today.")