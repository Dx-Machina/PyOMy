# Project: PyOMy
# Description: 
	AI-voice assistant fused with OpenAI's ChatGPT. It produces voice and written responses.
# Hardware Requirements:
	Raspberry Pi4(8gb),
	Microphone,
	Speakers,
	Keyboard.
	Mouse.
# Software Requirements:
	OpenAI Account (free tier will suffice),
	RPiOS (64-bit),
	Python 3.6 or Later,
	Linux Terminal,
	pip,
	bash,
	git,
	nano.
# Installation
	01- Go to OpenAI.com
 	02- Create an account if you don't already have one, otherwise Log-in with your credintials.
  	03- Go to 'API'
   	04- From the left pane, choose 'API Keys'
	05- Generate an API Key, and save it in a secure note (be sure not put it in a public repo, or it will be revoked immediately).
 	06- Download the run.sh file hosted on this repository, and save it to the desktop.
  	07- Open a new terminal window in your linux environment.
   	08- Make sure to navigate to where you downloaded the file (that is, if you didn't download it to the desktop).
	09- type nano run.sh to edit the file.
 	10- Navigate to line 14 (or where it says "export OPENAI_API_KEY='Your Personal OpenAI API Key'")
  	11- Paste your OpenAI API Key within the single quotes, and make sure there's no spaces
   	12- Save the file and exit by using command+x then pressing Y, then Enter.
	13- Type 'chmod +x run.sh' in your terminal to give the shell file permission to run
 	14- Type './run.sh' 
  	15- The shell file will run, install all the necessary packages and will start listening afterwards.
   	16- when it says listening, invoke the listener by saying 'Jarvis' and asking a question.
	17- to quit the program click command+c two times.
 	18- Voila, your personal intelligent AI-Assistant program is working on your Raspberry Pi.
