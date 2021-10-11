# EC601-Project2

-------------------------------------------------------------------------------

## TWEETITUDE!

-------------------------------------------------------------------------------

An app that allows users to find out what the average emotional feelings are from other users that @ them. All that's needed is to enter a twitter username and the number of recent tweets mentioning them to count. Then each tweet pulled is run through Google's NLP to determine the general emotional sentiment of the tweet. Each result is weighted, added, and then the overall average is presented to the user, along with a quick summary of what the result means.

To use the program, run the following from the command line while in the same directory as the application:

    python tweetitude.py

### The following python libraries are required in order to run this application:

* requests
* os
* json
* google.cloud-language

### Links used for reference while writing this application
* https://cloud.google.com/natural-language/docs/basics
* https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
* https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users#cURL
* https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets
* https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
* https://developer.twitter.com/en/docs/twitter-api/tweets/counts/quick-start/recent-tweet-counts
* https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Tweet-Counts/recent_tweet_counts.py
* https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2
* https://github.com/twitterdev/search-tweets-python

-------------------------------------------------------------------------------

## About the overall Process and Research before developing the App

-------------------------------------------------------------------------------

Testing Twitter API and Google NLP

For this project I tested a few of the example codes available from the twitter API github repository
https://github.com/twitterdev/Twitter-API-v2-sample-code

Specifically I tested displaying tweets by specifying their tweet ID, as well as counting recent tweets made by a specified user.

This involved figuring out how to get a token from my twitter dev account and then save it as a system environment variable to be used with code without saving the tokens to the code, as that would be a serious security risk.

For the Recent Tweets one, I edited the example code to prompt for input and change the output.
You are now prompted to enter a twitter account name, and then you are shown the total number of tweets that user tweeted in the past week (week is the default time span)

This involved figuring out how Python handles JSON, as the data pulled is in JSON format.

I've managed to 'flatten' the JSON input.

My understanding of how the data is pulled from Twitter and then worked with in Python:

It's pulled as a dictionary. If you then use the json.dumps() function, it converts the data to a string.

Using the json.loads() function on that string then converts it back to a dictionary, so the dumps() function from the example isn't needed if you want the
value in dictionary format.

For most purposes, outside of printing the JSON format for testing/debugging, the dictionary type is better, as it allows for accessing data using keys, rather than searching through a string.

Google NLP

Tried some example code to make sure the API was reachable.

First ran Google's Cloud SDK gcloud tool through the command line

Followed this guide: https://cloud.google.com/natural-language/docs/quickstart

God the expected JSON format result. Result: result_test1.json

Next tried running a python program that analyzes the sentiment of input text.
google-nlp-test1.py

This example was pulled from: https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3#6

Result: "result of running test1 python.txt"
