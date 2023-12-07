# Installation
# Please see The Documentation file for Project Description.
# Setup your environment.
	01- Go to OpenAI.com
 	02- Create an account if you don't already have one, otherwise Log-in with your credintials.
  	03- Go to 'API'
   	04- From the left pane, choose 'API Keys'
	05- Generate an API Key, and save it in a secure note (be sure not put it in a public repo, or it will be revoked immediately).
 	06- Download the start.sh file hosted on this repository, and save it to the desktop.
  	07- Open a new terminal window in your linux environment.
   	08- Make sure to navigate to where you downloaded the file (that is, if you didn't download it to the desktop).
	09- type nano start.sh to edit the file.
 	10- Navigate to line 13 (or where it says "export OPENAI_API_KEY='Your Personal OpenAI API Key'"
  	11- Paste your OpenAI API Key within the single quotes, and make sure there's no spaces
   	12- Save the file and exit by using command+x then pressing Y, then Enter.
	13- Type 'chmod +x start.sh' in your terminal to give the bash file permission to run
 	14- Type './start.sh' 
  	15- The bash file will run, install all the necessary packages and will start listening afterwards.
   	16- when it says listening, invoke the listener by saying 'Jarvis' and asking a question.
	17- to quit the program click command+c two times.
 	18- Voila, your personal intelligent AI-Assistant program is working on your Raspberry Pi.
