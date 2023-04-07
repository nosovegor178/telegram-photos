from dotenv import load_dotenv
import telegram
import os
import ptbot


load_dotenv()
TG_TOKEN=os.environ['TELEGRAM_BOT_TOKEN']
chat_id = '-1001986682480'
bot = telegram.Bot(TG_TOKEN)
bot.send_message(chat_id, 'Hello!')