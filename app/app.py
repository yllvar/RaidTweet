import tweepy
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(filename='raid.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class RaidTweet:
    def __init__(self):
        # Initialize Tweepy client with the API credentials
        self.client = tweepy.Client(
            bearer_token=os.getenv('X_BEARER_TOKEN'),
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_KEY_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_TOKEN_SECRET')
        )

    def fetch_latest_tweets(self, users):
        """Fetch the latest tweet from each user in the list."""
        for user in users:
            try:
                # Get user's ID
                user_info = self.client.get_user(username=user)
                if user_info.data:
                    user_id = user_info.data.id
                    # Fetch the latest tweet
                    tweets = self.client.get_users_tweets(id=user_id, max_results=1)
                    if tweets.data:
                        tweet = tweets.data[0]
                        return tweet.id, user
                logging.info(f"No tweet found for user: {user}")
            except Exception as e:
                logging.error(f"Failed to fetch tweet for {user}: {str(e)}")
        return None, None

    def reply_to_tweet(self, tweet_id, user):
        """Reply to the tweet with a predefined message."""
        reply_text = "What an insight, fire! 🔥 "
        try:
            self.client.create_tweet(in_reply_to_tweet_id=tweet_id, text=reply_text)
            logging.info(f"Successfully replied to tweet {tweet_id} from @{user}")
            print(f"Successfully replied to tweet {tweet_id} from @{user}")
        except Exception as e:
            logging.error(f"Failed to reply to tweet {tweet_id} from @{user}: {str(e)}")

if __name__ == "__main__":
    raid = RaidTweet()
    users_to_raid = ['TheCryptoLark', 'moneyl0rd', 'Ashcryptoreal']
    
    for user in users_to_raid:
        tweet_id, user = raid.fetch_latest_tweets([user])
        if tweet_id:
            raid.reply_to_tweet(tweet_id, user)