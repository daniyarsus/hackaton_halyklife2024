from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    OPEN_API_KEY = os.getenv("OPEN_API_KEY")
    ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

