# main.py
import asyncio
from .twitter import RaidTweet
from .config import config
from . import logging

logger = logging.setup_custom_logger(__name__)

async def fetch_and_print_latest_tweets(raid, user):
    try:
        tweet_id, user = raid.fetch_latest_tweets([user])
        if tweet_id:
            tweet_content = raid.client.get_tweet(id=tweet_id, tweet_fields=["text"])
            if tweet_content and tweet_content.data:
                logger.info(f"Latest tweet from @{user}: {tweet_content.data.text}")
                print(f"Latest tweet from @{user}: {tweet_content.data.text}")
            else:
                logger.warning(f"Could not fetch tweet content for @{user}")
        else:
            logger.warning(f"No tweet found for @{user}")
    except Exception as e:
        logger.error(f"Error in fetch_and_print_latest_tweets for @{user}: {e}")
    await asyncio.sleep(960)  # Sleep for 16 minutes

async def main():
    raid = RaidTweet()
    users_to_raid = config.users_to_raid
    
    logger.info("Starting Twitter Raid...")
    
    tasks = []
    for user in users_to_raid:
        try:
            task = asyncio.create_task(fetch_and_print_latest_tweets(raid, user))
            tasks.append(task)
        except Exception as e:
            logger.error(f"Failed to create task for @{user}: {e}")

    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        logger.error(f"Error gathering tasks: {e}")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")
    
    logger.info("Twitter Raid completed.")
