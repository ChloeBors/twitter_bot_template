import tweepy
import random
import os

def tweet():
    # authentication
    # make a twitter developer account first on developer.twitter.com/ to get authentication.
    auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
    auth.set_access_token(f'access_token', 'acces_token_secret')
    api = tweepy.API(auth)

    # specify text that you want to tweet
    tweet = "This is my Python tweet!"

    # add files, for example pictures. In this example it adds a random file/picture.
    # for more functions you can read the Tweepy documentation.
    path = r'filepath'
    files = os.listdir(path)
    random_pic = random.choice(files)

    # posting the tweet
    api.update_with_media(rf'{path}\{random_pic}', tweet)
    print("All done!")

    # run function
    tweet()



