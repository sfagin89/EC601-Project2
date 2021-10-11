# Tweetitude
# Python App for Users to see what recent attitudes towards their content is

import requests
import os
import json
from google.cloud import language

twit = input("Please enter the twitter name you want to search for replies to: ")
#twitterer = 'from:' + twit
twitterer = 'to:' + twit

# To set your environment variables in your terminal run the following line:
# export 'TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("TOKEN")

##Used to Search Recent Tweets directed at Specified User
search_url = "https://api.twitter.com/2/tweets/search/recent"

##Used to Search Recent Tweets directed at Specified User
query_params = {'query': twitterer, 'max_results': '10'}

def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    #print(str(sentiment.score))
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        scoreINT=sentiment.score,
        magnitude=f"{sentiment.magnitude:.1%}",
        magnitudeINT=sentiment.magnitude #Not mult 100 b/c using for weight
    )
    #for k, v in results.items():
    #    print(f"{k:10}: {v}")
    #print("\n")

    return results

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
    overallMetric = 0

    #print("Counting recent tweets from user: "+twit+"\n")

    #fetching data from dictionary
    ##Currently only use for Recent Tweet Count
    #twit_count = str(json_response['meta']['total_tweet_count'])

    ##Currently only use for Recent Tweet Count
    #print("The total number of Tweets from "+twit+" this week is "+twit_count)

    for item in json_response['data']:
        text = item['text'].replace("\n\n", "\n")
        sentiment = analyze_text_sentiment(text)
        overallMetric = overallMetric + (sentiment['scoreINT']*sentiment['magnitudeINT'])
        print("Printing test of dictionary output\n")
        print(sentiment['text'])
        print(sentiment['score'])
        print(sentiment['magnitude'])
        print("Current Total Metric: "+str(overallMetric)+"\n")
    overallMetric = f"{(overallMetric/json_response['meta']['result_count']):.1%}"
    print("Final Metric: "+overallMetric+"\n")
    #print("Final Metric: "+str(overallMetric/json_response['meta']['result_count'])+"\n")
    #text = json_response['data'][0]['text'].replace("\n\n", "\n")
    #text = text.replace("\n\n", "\n")
    #print(text)
    #analyze_text_sentiment(text)

if __name__ == "__main__":
    main()
