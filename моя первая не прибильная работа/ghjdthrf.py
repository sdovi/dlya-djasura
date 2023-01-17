import telebot

client = telebot.TeleBot("5836893149:AAHLdcl3TUlXLytwJnC8X0-UBButTSxjroQ")
@client.message_handler(commands= ['start'])
def start(message):
    client.message_handler(message.chat.id, 'иди гуляй, толку нету что ты сюда зашел по этому выходи отсюда нахуй')

client.polling(none_stop=True)
