# twitter.py
import tweepy
from .config import config
import logging  # Standard library import

logger = logging.getLogger(__name__)  # Get a logger for this module

class RaidTweet:
    def __init__(self):
        # Initialize Tweepy client with the API credentials from config
        self.client = tweepy.Client(
            bearer_token=config.X_BEARER_TOKEN,
            consumer_key=config.X_API_KEY,
            consumer_secret=config.X_API_KEY_SECRET,
            access_token=config.X_ACCESS_TOKEN,
            access_token_secret=config.X_ACCESS_TOKEN_SECRET
        )

    def fetch_latest_tweets(self, users):
        """Fetch the latest tweet from each user in the list."""
        for user in users:
            try:
                # Get user's ID
                user_info = self.client.get_user(username=user)
                if user_info.data:
                    user_id = user_info.data.id
                    # Fetch the latest tweet, using 5 for max_results as minimum allowed value
                    tweets = self.client.get_users_tweets(id=user_id, max_results=5)
                    if tweets.data:
                        tweet = tweets.data[0]
                        return tweet.id, user
                logger.info(f"No tweet found for user: {user}")
            except tweepy.errors.BadRequest as e:
                logger.error(f"API Error for {user}: {str(e)}")
            except Exception as e:
                logger.error(f"Failed to fetch tweet for {user}: {str(e)}")
        return None, None

    def reply_to_tweet(self, tweet_id, user):
        """Reply to the tweet with a predefined message."""
        reply_text = "What an insight, fire! 🔥 "
        try:
            self.client.create_tweet(in_reply_to_tweet_id=tweet_id, text=reply_text)
            logger.info(f"Successfully replied to tweet {tweet_id} from @{user}")
            print(f"Successfully replied to tweet {tweet_id} from @{user}")
        except Exception as e:
            logger.error(f"Failed to reply to tweet {tweet_id} from @{user}: {str(e)}")