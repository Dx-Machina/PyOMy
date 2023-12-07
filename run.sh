git clone https://github.com/Dx-Machina/PyOMy.git # Clone the repository
sudo apt-get install  portaudio19-dev # Install the dependencies
sudo apt-get install python3-pyaudio # Install the dependencies
pip install --break-system-packages speechrecognition # Install the dependencies
pip install --break-system-packages pyttsx3 # Install the dependencies
pip install --break-system-packages openai==0.28 # Install the dependencies
sudo apt-get install espeak # Install the dependencies
sudo apt-get install flac   # Install the dependencies

# Set the environment variables
export VOICE_RATE=100 # words per minute
export VOICE_VOLUME=1.0 # float between 0 and 1
export VOICE='english' # sets the language to english
export OPENAI_API_KEY='Your Personal OpenAI API Key' # put your OpenAI API key between the quotes.

# Go to the PyOMy directory
cd PyOMy
# Run the python file
python PyOMyCoPi.py