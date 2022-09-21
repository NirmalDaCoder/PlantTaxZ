# imports
from recognition import recognize_speech
import speech
import random
from time import ctime
import webbrowser
from PIL import Image

# variables
name = 'master'
engine = speech.speech_engine(200, 0.9, 11)

# multi call values 
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

#speech function
def speak(text):
    engine.speak(text)

# respondent module
def respond(voice_data):
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {name}", f"hey, what's up? {name}", f"I'm listening {name}", f"how can I help you? {name}", f"hello {name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    if there_exists(["what is your name","what's your name","tell me your name", "can you tell about yourself"]):
        if name:
            speak("my name is Plant Tax .")

    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well sir")

    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    if there_exists(["search for", "to know about"]) and 'youtube' not in voice_data:
        if not there_exists(["search for"]):
            search_term = voice_data.split("about")[-1]
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists(["time table", "timetable"]):
        timetable = Image.open(r"/home/nirmal/Pictures/whatsapp/timetable.jpg")
        timetable.show()
        speak("sir, here is your timetable")

    if there_exists(["exit", "quit", "goodbye"]):
        speak("bye sir")
        exit()

# Loop
if __name__ == "__main__":
    while(True):
        voice_data = recognize_speech()
        respond(voice_data)
