API_KEY = "YOUR API KEY HERE"

import os
import telebot
import subprocess
import time




bot = telebot.TeleBot(API_KEY)
users = ['AragAggrawal', 'SaintlyPioneer']

@bot.message_handler(commands=['test'])
def test(message):
    user = message.from_user.username
    if user in users:
        txt = message.text[6:]
        process = subprocess.Popen(txt, shell=True, stdout=subprocess.PIPE)
        # print (message)
        reply = bot.reply_to(message, "Processing...")
        while True:
            time.sleep(5)
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                # print(output.strip())
                reply = bot.edit_message_text(text=output.strip(), chat_id=reply.chat.id, message_id=reply.message_id)
                # reply = bot.reply_to(message, output.strip())
                # time.sleep(5)
                # bot.edit_message_text(text="Hey There", chat_id=reply.chat.id, message_id=reply.message_id)



@bot.message_handler(commands=['magnet'])
def start(message):
    user = message.from_user.username
    if user in users:
        previousMessage = ""
        reply = bot.reply_to(message, "Downloading...")
        txt = message.text[8:]
        process = subprocess.Popen("aria2c -c --seed-time=0.1 \"" + txt + "\"", shell=True, stdout=subprocess.PIPE)
        print (previousMessage)
        while True:
            print ("In Loop")
            # time.sleep(5)
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                replyTxt = output.strip().decode()
                if previousMessage == replyTxt or replyTxt == "":
                    continue
                reply = bot.edit_message_text(text=replyTxt, chat_id=reply.chat.id, message_id=reply.message_id)
                previousMessage = replyTxt
        reply = bot.edit_message_text(text="Downloaded... Please Verify.", chat_id=reply.chat.id, message_id=reply.message_id)

bot.polling()
