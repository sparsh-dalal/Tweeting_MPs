import tweepy
import config

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth)
user = api.get_user("BarackObama")
answer = user.verified
print(answer)
