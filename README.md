# PyOMy
# Open AI based Voice Chatbot in Raspberry Pi

## Installation

To install the required libraries, run the following commands in your terminal:

```bash
git clone https://github.com/Dx-Machina/PyOMy.git
sudo apt-get install  portaudio19-dev
sudo apt-get install python3-pyaudio
pip install --break-system-packages speechrecognition
pip install --break-system-packages pyttsx3
pip install --break-system-packages openai==0.28
sudo apt-get install espeak
sudo apt-get install flac
``````
** note: only use the "--break-system-packages" flag if your machine is unable to pip.
# To Run

```bash
python PyOMy.py
``````
