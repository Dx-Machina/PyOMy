import os
import pyttsx3
import speech_recognition as sr
import openai

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Get the list of voices
voices = engine.getProperty('voices')

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

messages = []  # Define the messages list

def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        print("Jarvis: " + ChatGPT_reply)
    except Exception as e:
        print(f"Error getting response from OpenAI: {e}")
        ChatGPT_reply = "Sorry, I couldn't process your request."

    return ChatGPT_reply

def listen_and_respond():
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5.0)
            response = recognizer.recognize_google(audio)
            print(response)

            if "jarvis" in response.lower():   
                response_from_openai = get_response(response)
                engine.setProperty('rate', 120)
                engine.setProperty('volume', 0.8)
                engine.setProperty('voice', voices[0].id)  # Set the voice
                engine.say(response_from_openai)
                engine.runAndWait()               
            else:
                print("Didn't recognize 'jarvis'.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

listening = True
while listening:
    listen_and_respond()