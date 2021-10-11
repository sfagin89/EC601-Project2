# Tweetitude
# Python App for Users to see what recent attitudes towards their content is

import requests
import os
import json
from google.cloud import language

twit = input("Please enter the twitter name you want to search a tweet count for: ")
twitterer = 'from:' + twit


# To set your environment variables in your terminal run the following line:
# export 'TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("TOKEN")

search_url = "https://api.twitter.com/2/tweets/counts/recent"

# Optional params: start_time,end_time,since_id,until_id,next_token,granularity
#query_params = {'query': 'from:Asmongold','granularity': 'day'}
query_params = {'query': twitterer,'granularity': 'day'}

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
    json_response = connect_to_endpoint(search_url, query_params)
    print(type(json_response))
    print(json.dumps(json_response, indent=4, sort_keys=True))

    sample_object = json.dumps(json_response, indent=4, sort_keys=True)
    print(sample_object)
    print(type(sample_object))
    data = json.loads(sample_object)
    print(type(data))
    print(data)
    print("Counting recent tweets from user: "+twit+"\n")

    #fetching data from dictionary
    print(data.get('meta'))
    twit_count = str(data['meta']['total_tweet_count'])

    print("The total number of Tweets from "+twit+" this week is "+twit_count)

    text = "Guido van Rossum is great!"
    analyze_text_sentiment(text)

if __name__ == "__main__":
    main()
