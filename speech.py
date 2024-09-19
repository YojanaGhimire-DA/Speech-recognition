import speech_recognition as sr
import distutils


# Initialize recognizer
recognizer = sr.Recognizer()

#SOS commands to listen for
SOS_COMMANDS = ["help", "emergency", "sos"]

def listen_for_command():
    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        # Reduce the effect of ambient noise
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for voice commands...")

        try:
            # Listen  first phrase and extract the audio 
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing speech...")
            
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio).lower()
            print(f"said: {command}")

            # Check if the recognized command is in the SOS_COMMANDS list
            if any(sos_command in command for sos_command in SOS_COMMANDS):
                trigger_sos_alert()
            else:
                print("No SOS command detected.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def trigger_sos_alert():
    print("SOS Alert Triggered!")
     #push_notification()

if __name__ == "__main__":
    listen_for_command()
