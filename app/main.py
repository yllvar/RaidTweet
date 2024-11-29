# main.py
from .twitter import RaidTweet

def main():
    raid = RaidTweet()
    users_to_raid = ['TheCryptoLark', 'moneyl0rd', 'Ashcryptoreal']
    
    for user in users_to_raid:
        tweet_id, user = raid.fetch_latest_tweets([user])
        if tweet_id:
            raid.reply_to_tweet(tweet_id, user)

if __name__ == "__main__":
    main()