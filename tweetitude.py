# Tweetitude
# Python App for Users to see what recent attitudes towards their content is

import requests
import os
import json
import sys
from google.cloud import language

# To set your environment variables in your terminal run the following line:
# export 'TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("TOKEN")

# Endpoint URL: Accesses the Twitter API for searching recent tweets
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Submits text of a pulled tweet to Google NLP, to determine the likely sentiment of the text.
def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    #print(str(sentiment.score)) # For bug testing
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        scoreINT=sentiment.score,
        magnitude=f"{sentiment.magnitude:.1%}",
        magnitudeINT=sentiment.magnitude
    )

    return results

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r

def connect_to_endpoint():
    twit = input("Enter the twitter username you want to search for recent tweets about: ")
    #twit = "asmongold" #Hardcoded for testfile singleinput test
    # Used to indicate tweets made by the referenced account
    # twitterer = 'from:' + twit
    # Used to indicate tweets made to the referenced account
    twitterer = 'to:' + twit
    maxTweets = input("What's the maximum number of tweets you want to include in the calculation? (10-100): ")
    if (int(maxTweets) < 10) or (int(maxTweets) > 100) :
        print("Sorry, that's outside of the allowed range. The maximum number of tweets has been set back to the default of 10.\n")
        maxTweets = 10
    if int(maxTweets) > 15:
        print("Appologies if there's a little wait! Larger Tweet counts can take a little while, but we're working on it!\n")

    # Used to Search Recent Tweets directed at Specified User, and sets the max number of tweets to reference.
    query_params = {'query': twitterer, 'max_results': maxTweets}

    response = requests.request("GET", search_url, auth=bearer_oauth, params=query_params)
    if response.status_code != 200:
        print(f'Failed to retrieve tweets: status_code {response.status_code}, response body {response.text}')
        #raise Exception(response.status_code, response.text)
        return
    print("Tweets retrieved", file=sys.stderr)
    return response.json()


def main():
    print("Welcome to Tweetitude! Here you can track the average attitude of those talking about you or anyone else on twitter!")
    print("All you need to do is enter a twitter username, and the number of most recent tweets to include in our calculations and you're done!")
    print("Let's get started.")

    json_response = connect_to_endpoint()
    overallMetric = 0

    # Passes each pulled tweet to the NLP sentiment analyzer and updated the total score.
    for item in json_response['data']:
        text = item['text'].replace("\n\n", "\n")
        sentiment = analyze_text_sentiment(text)
        overallMetric = overallMetric + (sentiment['scoreINT']*sentiment['magnitudeINT'])

    # Averages the sentiment metric results to give an overall rating.
    overallMetric = (overallMetric/json_response['meta']['result_count'])
    print("Overall Average Sentiment based on the most recent "+str(json_response['meta']['result_count'])+" tweets: "+f"{overallMetric:.1%}")
    if overallMetric >= 0:
        if overallMetric >= 50:
            print("This indicates a very positive emotional response on average! Congrats!")
        else:
            print("This indicates a generally positive emotional response on average.")
    else:
        if overallMetric >= -50:
            print("This indicates a generally negative emotional response on average.")
        else:
            print("This indicates a very negative emotional response on average.")

if __name__ == "__main__":
    main()
