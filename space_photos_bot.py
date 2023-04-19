from dotenv import load_dotenv
import telegram
import os
import time
import argparse
import sys
import random


def create_args(chat_id):
	parser = argparse.ArgumentParser()
	parser.add_argument('chat_id', help='id of your chat in Telegram', default=chat_id, nargs='?', type=int)
	parser.add_argument('time', help='the time interval after which the message is sent(in secs)', default=14400, type=int, nargs='?')
	parser.add_argument('image', help='image to send', nargs='?')
	args = parser.parse_args(sys.argv[1:])
	return args

if __name__ == '__main__':	
	directory ='images'
	filesindir=os.listdir(directory)
	amount_of_images = 0

	load_dotenv()

	tg_token = os.environ['TELEGRAM_BOT_TOKEN']
	tg_chat_id = os.environ['TG_CHAT_ID']
	bot = telegram.Bot(tg_token)
	args = create_args(tg_chat_id)
	
	while True:
		if args.image:
			with open(os.path.join("{}".format(directory), "{}".format(args.image)),'rb') as image:
					bot.send_document(args.chat_id, image)
					time.sleep(int(args.time))
		else:
			for image_in_dir in filesindir:
				with open(os.path.join("{}".format(directory), "{}".format(image_in_dir)),'rb') as image:
					bot.send_document(args.chat_id, image)
				time.sleep(int(args.time))
				amount_of_images += 1
			random.shuffle(filesindir)
			amount_of_images = 0