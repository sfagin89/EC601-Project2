# EC601-Project2
Testing Twitter API and Google NLP

For this project I tested a few of the example codes available from the twitter API github repository
https://github.com/twitterdev/Twitter-API-v2-sample-code

Specifically I tested displaying tweets by specifying their tweet ID, as well as counting recent tweets made by a specified user.
For the Recent Tweets one, I edited the example code to prompt for input and change the output.
This involved figuring out how Python handles JSON, as the data pulled is in JSON format.
I've managed to 'flatten' the JSON input.
My understanding of how the data is pulled from Twitter and then worked with in Python:
It's pulled as a dictionary. If you then use the json.dumps() function, it converts the data to a string.
Using the json.loads() function on that string then converts it back to a dictionary, so the dumps() function from the example isn't needed if you want the
value in dictionary format.
