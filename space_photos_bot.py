from dotenv import load_dotenv
import telegram
import os
import time
import argparse
import sys
import random


def create_args(chat_id):
	
	parser = argparse.ArgumentParser()
	parser.add_argument('chat_id', help='id of your chat in Telegram', default=chat_id ,type=int)
	parser.add_argument('time', help='the time interval after which the message is sent(in secs)', default=14400, type=int, nargs='?')
	parser.add_argument('image', help='image to send', nargs='?')
	args = parser.parse_args(sys.argv[1:])
	return args
	

if __name__ == '__main__':	
	directory ='images'
	filesindir = os.listdir(directory)
	amount_of_images = 0

	load_dotenv()
	TG_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
	TG_CHAT_ID = os.environ['TG_CHAT_ID']
	bot = telegram.Bot(TG_TOKEN)
	args = create_args(TG_CHAT_ID)
	

	while True:
		if args.image == None:
			for image_in_dir in filesindir:
				with open(os.path.join("{}".format(directory), "{}".format(image_in_dir)),'rb') as image:
					bot.send_document(args.chat_id, image)
					time.sleep(int(args.time))
					image.close()
					amount_of_images += 1
			random.shuffle(filesindir)
			amount_of_images = 0
		else:
			with open(os.path.join("{}".format(directory), "{}".format(args.image)),'rb') as image:
					bot.send_document(args.chat_id, image)
					time.sleep(int(args.time))
					image.close()
					