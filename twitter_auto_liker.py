from api_keys import *
import tweepy
import time

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
apiData = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def like_by_user():
    user_id = input('Enter Users Twitter ID : ')
    user_data = apiData.get_user(user_id)
    user_name = user_data.name
    user_screen_name = user_data.screen_name
    for tweet in tweepy.Cursor(apiData.user_timeline, screen_name=user_screen_name).items():
        try:
            print('Liking '+user_name+ ' Tweets..')
            tweet.favorite()
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def like_by_hashtag():
    terms_list = []
    n = int(input('Enter Number of Hastags : '))
    for  i in range(0, n):
        elt = input('Enter Hashtag '+(str(i+1))+' : ')
        terms_list.append('#'+elt)
    terms_list_str = ' OR '.join(terms_list)
    for tweet in tweepy.Cursor(apiData.search, terms_list_str).items():
        try:
            print('Liking Tweets with Hashtags '+terms_list_str)
            tweet.favorite()
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def main(choice):
    if choice==1:
        like_by_user()
    elif choice==2:
        like_by_hashtag()

if __name__=="__main__":
    print('1. Like Tweets by Username')
    print('2. Like Tweets by Hashtags (Dont Enter #)')
    n = int(input('Enter Choice : '))
    main(n)