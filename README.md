# Crypto_GoogleExtension

This Repository hosts all the neccesary code to run my crypto extension on my computer.
The note, "my computer", is important because most of the code in this repository is specific to 
my google chrome, my coinbase account, and virtual environmnets that only exist on my computer that 
enables the code to run. 

Files:
Manifest.json and Background.js enable the program to run on google chrome. They communicate using codes
that are specofic to my google chrome. Popup.html runs the extension creating the window, text, and buttons.
Main-sublime.py runs the API code that retrieves current price data and displays it on my computer.

To run the python code:

1. Make sure python is intalled on your computer
 	-  if you don't know go to this link to download th most recent version: https://www.python.org/

2. open pycharm and folloe this youtube tutorial, but when he types numpy, type "coinbase"

3. replace:
		cb_API_key = '**********'
		cb_secret = '**********'
	
	with:
		cb_API_key = '5uR0RaWqzNLdqhAT'
		cb_secret = 'ZvcCjLlDEuscoPl9JLak2NAIxoy5meSV'

3. the code should run as shown in the picture

to setup the chrome extension:

1. watch this video but only the parts that deal with google itself

2. https://www.youtube.com/watch?v=FB2gJBoSshM