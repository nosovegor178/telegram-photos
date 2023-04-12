from dotenv import load_dotenv
import telegram
import os
import time
import argparse
import sys
import random


load_dotenv()
TG_TOKEN=os.environ['TELEGRAM_BOT_TOKEN']
chat_id = '-1001986682480'
bot = telegram.Bot(TG_TOKEN)

parser = argparse.ArgumentParser()
parser.add_argument('chat_id', help='id of your chat in Telegram', type=int)
parser.add_argument('time', help='the time interval after which the message is sent(in secs)', default=14400, type=int, nargs='?')
parser.add_argument('directory', help='directory where placed pictures', default='images', nargs='?')
args = parser.parse_args(sys.argv[1:])
filesindir = os.listdir(args.directory)

parser.add_argument('image', help='image to send', default=random.choice(filesindir), nargs='?')
args = parser.parse_args(sys.argv[1:])

while True:
	bot.send_document(args.chat_id, open('{1}\{0}'.format(args.image, args.directory), 'rb'))
	time.sleep(int(args.time))