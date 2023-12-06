import os
import speech_recognition as sr
import pyttsx3
import openai

listening = True
# Initialize pyttsx3
def initialize_pyttsx3():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    return engine

# Initialize speech recognition
def initialize_speech_recognition():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = 3000
    recognizer.adjust_for_ambient_noise(source)
    return recognizer

#Set your openai api key and customizing the chatgpt role
openai.api_key = os.getenv('OPENAI_API_KEY')
messages = [{"role": "system", "content": "Your name is Jarvis and give answers in 2 lines"}]


# Get response from OpenAI
def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply}) 
    print("Jarvis: " + ChatGPT_reply)# Print the response to the console
    return ChatGPT_reply
# Set voice properties
def set_voice_properties(engine, rate=120, volume=1.0, voice='greek'):
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.setProperty('voice', voice)

# Main loop
while listening:
    with sr.Microphone() as source:
        engine = initialize_pyttsx3()
        recognizer = initialize_speech_recognition()

        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5.0)
            response = recognizer.recognize_google(audio)
            print(response)
           
            if "jarvis" in response.lower():   
                response_from_openai = get_response(response)
                set_voice_properties(engine)
                engine.say(response_from_openai)
                engine.runAndWait()               
            else:
                print("Didn't recognize 'jarvis'.")
        except sr.WaitTimeoutError:
            print("Timeout; no speech heard")
        except Exception as e:
            print(f"An error of type {type(e).__name__} occurred: {e}")
