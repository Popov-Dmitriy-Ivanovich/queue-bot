import telebot
import queue
from telebot import types
TOKEN="5320961889:AAE8mFuqE0SlrEeR9ZhDm1kHQNHcqmUSKPc"


bot = telebot.TeleBot(TOKEN)
cur='nobody'
stud_queue = queue.Queue()
long_queue = queue.Queue()
@bot.message_handler(func= lambda m: m.text[:4] == '/add')
def add_user_to_queue (message):
    if len(message.text.split()) > 2:
        new_user = message.text.split()
        if (int(new_user[2])<3):
            stud_queue.put(message.text[4:])
        else:
            long_queue.put(message.text[4:])
        bot.send_message(message.chat.id, message.text[4:] + ' added to queue')
    else:
        bot.send_message(message.chat.id, 'name is empty')

@bot.message_handler(func= lambda m: m.text == '/cur')
def show_cur(message):
    global cur
    bot.send_message(message.chat.id,'current user is' + cur)

@bot.message_handler(func= lambda m: m.text == '/next')
def show_next(message):
    try:
        global cur
        if not stud_queue.empty() :
            cur=stud_queue.get()
        else:
            cur=long_queue.get()
        bot.send_message(message.chat.id,'next user is' + cur)
    except:
        bot.send_message(message.chat.id,'something went wrong, queue might be empty')

bot.polling()