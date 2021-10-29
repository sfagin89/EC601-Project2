# Tweetitude
# Python App for Users to see what recent attitudes towards their content is

import requests
import os
import json
from google.cloud import language

twit = input("Please enter the twitter name you want to search a tweet count for: ")
#twitterer = 'from:' + twit
twitterer = 'to:' + twit

# To set your environment variables in your terminal run the following line:
# export 'TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("TOKEN")

##Used to Search and Count Recent Tweets by Specified Tweeter
#search_url = "https://api.twitter.com/2/tweets/counts/recent"
search_url = "https://api.twitter.com/2/tweets/search/recent"

##Used to display data about the Specified Tweet
#search_url = "https://api.twitter.com/2/tweets"

##Used to display data about the user
#search_url = "https://api.twitter.com/2/users"

##Used to Search and Count Recent Tweets by Specified Tweeter
#query_params = {'query': twitterer,'granularity': 'day'}
#query_params = {'query': twitterer,'granularity': 'day'}
query_params = {'query': twitterer}

##Used to display data about the Specified Tweet
#query_params = {'ids': "1441446902768177158,1441447738978222081", 'tweet.fields': "lang,author_id"}

##Used to display data about the user
#query_params = {'ids': "147039284", 'expansions': "pinned_tweet_id", 'tweet.fields': "text"}
#147039284

def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    #Dictionary containing JSON Data
    json_response = connect_to_endpoint(search_url, query_params)
    #print(type(json_response)) ##Prints <class 'dict'>
    print(json.dumps(json_response, indent=4, sort_keys=True))

    #print("Counting recent tweets from user: "+twit+"\n")

    #fetching data from dictionary
    ##Currently only use for Recent Tweet Count
    #twit_count = str(json_response['meta']['total_tweet_count'])

    ##Currently only use for Recent Tweet Count
    #print("The total number of Tweets from "+twit+" this week is "+twit_count)

    #for item in json_response['data']:
    #    text = item['text'].replace("\n\n", "\n")
    #    analyze_text_sentiment(text)
    #text = json_response['data'][0]['text'].replace("\n\n", "\n")
    #text = text.replace("\n\n", "\n")
    #print(text)
    #analyze_text_sentiment(text)

if __name__ == "__main__":
    main()
