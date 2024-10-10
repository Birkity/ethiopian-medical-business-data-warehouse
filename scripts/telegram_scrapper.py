import os
import csv
import logging
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv(r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_7\.env')
telegram_api_id = os.getenv('TG_API_ID')
telegram_api_hash = os.getenv('TG_API_HASH')
user_phone = os.getenv('phone')

logging.basicConfig(
    filename='channel_scraper.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  
)
scraper_logger = logging.getLogger()

async def gather_channel_data(telegram_client, channel_handle, csv_writer, image_dir):
    try:
        channel_entity = await telegram_client.get_entity(channel_handle)
        channel_name = channel_entity.title  
        scraper_logger.info(f"Gathering data from: {channel_name} ({channel_handle})")
        
        message_count = 0  
        async for post in telegram_client.iter_messages(channel_entity, limit=10000):
            media_filepath = None
            if post.media and hasattr(post.media, 'photo'):
                
                img_filename = f"{channel_handle}_{post.id}.jpg"
                media_filepath = os.path.join(image_dir, img_filename)
                
                await telegram_client.download_media(post.media, media_filepath)
                scraper_logger.info(f"Image saved from message {post.id} at {media_filepath}")
            
            csv_writer.writerow([channel_name, channel_handle, post.id, post.message, post.date, media_filepath])
            message_count += 1

        scraper_logger.info(f"Scraped {message_count} messages from {channel_handle}")
    
    except Exception as err:
        scraper_logger.error(f"Failed to scrape {channel_handle}: {err}")

telegram_client = TelegramClient('scraper_session', telegram_api_id, telegram_api_hash)