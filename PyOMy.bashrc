git clone https://github.com/Dx-Machina/PyOMy.git
sudo apt-get install  portaudio19-dev
sudo apt-get install python3-pyaudio
pip install --break-system-packages speechrecognition
pip install --break-system-packages pyttsx3
pip install --break-system-packages openai==0.28
sudo apt-get install espeak
sudo apt-get install flac

export VOICE_RATE=100
export VOICE_VOLUME=0.8
export VOICE='english'
export OPENAI_API_KEY='YOUR_API_KEY'

#Run the python file
python PyOMyCoPi.py