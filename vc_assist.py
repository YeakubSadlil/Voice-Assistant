import pywhatkit  # Library for playing music and searching the web
import wikipedia  # Library for accessing Wikipedia data
import speech_recognition as spr  # Library for speech recognition
import pyttsx3  # Library for text-to-speech synthesis
import datetime  # Library for working with dates and times

# Create a speech recognizer object
listener = spr.Recognizer()

# Create a text-to-speech engine object
neptune = pyttsx3.init()

def speak(text):
    """Convert text to speech and play it using the text-to-speech engine."""
    neptune.say(text)
    neptune.runAndWait()

def take_command():
    """Listen for and recognize a voice command."""
    try:
        with spr.Microphone() as mic:
            print('listening...')
            voice = listener.listen(mic)
            command = listener.recognize_google(voice)
            command = command.lower()
            # Remove "neptune" from the beginning of the command if present
            if 'neptune' in command:
                command = command.replace('neptune', '')
    except:
        # If there is an error, return an empty string
        command = ''
    return command

def run_neptune():
    """Handle a voice command by determining the appropriate response."""
    command = take_command()
    if 'time' in command:
        # Get the current time and convert it to a string in a human-readable format
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        speak('Current time is ' + current_time)
    elif 'your name' in command:
        info = "My name is Neptune"
        print(info)
        speak(info)
    elif 'play' in command:
        # Get the name of the song to play
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.play
