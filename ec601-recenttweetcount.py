# Useful Links
# https://www.programiz.com/python-programming/nested-dictionary
# https://realpython.com/python-dicts/#dgetkey-default

import requests
import os
import json

twit = input("Please enter the twitter name you want to search a tweet count for: ")
twitterer = 'from:' + twit

# To set your environment variables in your terminal run the following line:
# export 'TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("TOKEN")

search_url = "https://api.twitter.com/2/tweets/counts/recent"

# Optional params: start_time,end_time,since_id,until_id,next_token,granularity
#query_params = {'query': 'from:Asmongold','granularity': 'day'}
query_params = {'query': twitterer,'granularity': 'day'}

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
    #print(type(json_response))
    #print(json.dumps(json_response, indent=4, sort_keys=True))

    sample_object = json.dumps(json_response, indent=4, sort_keys=True)
    #print(sample_object)
    #print(type(sample_object))
    data = json.loads(sample_object)
    #print(type(data))
    #print(data)
    print("Counting recent tweets from user: "+twit+"\n")

    #fetching data from dictionary
    #print(data.get('meta'))
    twit_count = str(data['meta']['total_tweet_count'])

    print("The total number of Tweets from "+twit+" this week is "+twit_count)

if __name__ == "__main__":
    main()
