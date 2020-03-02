import tweepy

consumer_key = "wayDs6V0Csv63NFS5JNVXpcg0"
consumer_secret = "ETHHLlJtxvBzFFt1iEArLrveaVfsPmxtp7VlJ6yTeyuoqqKeIV"
access_key = "3826955894-Aydp0zLK0NnzTZ4qoGE0TMuu4nEEYHI3SKYvsSj"
access_secret = "avnCxRixSXztNG0rqRVq5e4dW3kxMmI4V0UYfACqUopcX"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=20)
    alltweets.extend(new_tweets)
    outtweets = [[tweet.id_str, tweet.created_at,
                  tweet.text.encode("utf-8")] for tweet in alltweets]

    return outtweets
