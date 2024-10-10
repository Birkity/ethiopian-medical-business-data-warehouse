import os
import csv
import logging
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv(r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_7\.env')
telegram_api_id = os.getenv('TG_API_ID')
telegram_api_hash = os.getenv('TG_API_HASH')
user_phone = os.getenv('phone')
