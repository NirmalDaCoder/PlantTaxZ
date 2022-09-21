import pyttsx3

class speech_engine:
    def __init__(self, speech_rate, volume, voice_id) -> None:
        # initializing engine
        self.engine = pyttsx3.init()
        # variable definition
        self.speech_rate = speech_rate
        self.volume = volume
        self.voice_id = voice_id
        # speech rate
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.speech_rate)
        # speech volume
        volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume',self.volume)
        # language and accent
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.voice_id].id)

    def __repr__(self) -> str:
        return f"speech rate : {self.speech_rate} speech volume : {self.volume} voice id : {self.voice_id}"

    # speak function
    def speak(self, text) -> None:
        self.engine.say(str(text))
        self.engine.runAndWait()
        self.engine.stop()

# testing the speech engine
if __name__ == '__main__':
    engine = speech_engine(190, 0.8, 11)
    print(engine)
    engine.speak("Hello! This is a small test of the speech engine . I have printed some details about the test")

