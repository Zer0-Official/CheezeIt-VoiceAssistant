import pyttsx3
import speech_recognition as sr
import time
wait = 60

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query_in = r.recognize_google(audio, language='en-in')
        print("User said:" + query_in + "\n")
    except Exception as e:
        print(e)
        return "None"
    return query_in


if __name__ == '__main__':

    time.sleep(5)
    while True:
        speak('Advanced Artificial Intelligence and Machine Learning Systems have detected that it is time for you to '
              'consume a cheese it. Would you like one now?')
        query = take_command().lower()
        if 'yes' in query:
            speak('Ok! Here is a cheese it.')
            print('  ____________________   ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  . □   .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  | .  .  .  .  .  .  |  ')
            print('  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  ')
            wait -= 2
        else:
            speak('It is acceptable to reject food. Another time i guess.')
            wait += 2
        time.sleep(wait)
