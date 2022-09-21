import speech_recognition as sr # recognize speech ( python module )
from speech import speech_engine

recognizer = sr.Recognizer() # initialise a recognize
engine = speech_engine(190, 0.8, 11)

def recognize_speech(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine.speak(ask)
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('Unable to Recognize Voice')
        except sr.RequestError:
            print('Connection Error') # error: recognizer is not connected
        print(f">>> {voice_data}")
        return voice_data.lower()

# testing ...
if __name__ == '__main__':
    recognize_speech()
