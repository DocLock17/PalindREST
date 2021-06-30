# PalindREST
Welcome to PalindREST, a simple REST API for reversing a string. 

RUNNING PalidREST
The application is written using a simple flask server in python so download this folder and unzip if needed.
Next, simply run the following:
  **python main.py**
and a development server should begin running locally at http://127.0.0.1:5000/
you may then use your webrowser to navigate to this location where the browsers default get request should produce a simple welcome message.

To get full functionality you will need some method of submitting a PUT request to the API. For testing purposes, I used POSTMAN. Which can be found here:
  https://www.postman.com/downloads/
once your method of interaction is ready to go you may send a PUT request to the server, using the 'input' KEY 
along with any string VALUE you would like.
When the server responds it will return a JSON Object containg a single 'body' key.
The VALUE of this 'body' KEY will be the reversed input string.
