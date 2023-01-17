import telebot
from telebot import types
client = telebot.TeleBot("5836893149:AAGwVrLzM9CTQOUXVe2eIPWpC70olIfUG0A")
@client.message_handler(commands= ['start'])
def start(message):
    yazik = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yazik.add(types.KeyboardButton('Русский🇷🇺'),types.KeyboardButton('English🇺🇸'))

    perevod = client.send_message(message.chat.id, 'Выберите язык🏳️ Select a language🏳️', reply_markup=yazik)
    client.register_next_step_handler(perevod, vibyaz)

def vibyaz(message):
    vopros = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vopros.add(types.KeyboardButton('Хочу задать вопрос🙂'), types.KeyboardButton('Хочу скидку на комиссию😠'), types.KeyboardButton('Я крупный майнер \n'
                                                                                                                                 '(у меня больше 1 Ph/s)'
                                                                                                                                 'и хочу VIP-условия'))
    voprosen = types.ReplyKeyboardMarkup(resize_keyboard=True)
    voprosen.add(types.KeyboardButton('I want to ask a question🙂'), types.KeyboardButton('I want a pool fee discount😠'),
               types.KeyboardButton('I am a large miner \n'
                                    '(I have more than 1 Ph/s)'
                                    'and I want VIP conditions'))

    if message.text == 'Русский🇷🇺':
        client.send_message(message.chat.id, 'Приветсвую✋')
        perevod = client.send_message(message.chat.id, 'Выберите один из пунктов⬇️', reply_markup=vopros)
        client.register_next_step_handler(perevod,Punkto)
    elif message.text == 'English🇺🇸':
        client.send_message(message.chat.id, 'Hello✋')
        perevod = client.send_message(message.chat.id, 'Select one of the following items⬇️', reply_markup=voprosen)
        client.register_next_step_handler(perevod, Punktoen)





def Punkto(message):
    if message.text == 'Хочу задать вопрос🙂':
        client.send_message(message.chat.id, 'Отлично🥳')
        client.send_message(message.chat.id, f'В нашем чате майнеров EMCD вы можете задать свой вопрос,\n'
                                             'наша служба поддержки ответит на русском языке за 3 минуты', )

    elif message.text == 'Хочу скидку на комиссию😠':
        client.send_message(message.chat.id, 'Отлично🥳')
        client.send_message(message.chat.id, 'Ваша скидку 20% на комиссию майнинг пула на 30 дней\n'
                                             'Получить скидку можно одним из способов ниже:')
        client.send_message(message.chat.id, '1. Скачать приложение EMCD и ввести промокод TELEGRAM при регистрации\n'
                                             '2. Зарегистрироваться на официальном сайте майнинг пула по этой ссылке \n'
                                             '3. Отсканировать QR-код с телефона и ввести промокод TELEGRAM при регистрации ')
        client.send_photo(message.chat.id, 'https://imgurhd.ru/i/8sd1.png',)

    elif message.text == 'Я крупный майнер \n'\
            '(у меня больше 1 Ph/s)'\
            'и хочу VIP-условия':
        client.send_message(message.chat.id, 'Да-да, мы платим экстра-вознаграждение за каждый 1 Ph/s. \n'
                                             'Я уже передал ваш контакт аккаунт менеджеру EMCD, скоро он с вами свяжется. \n'
                                             'А пока вы можете просмотреть презентацию о нашем сотрудничестве.')
        client.send_photo(message.chat.id, 'https://i.ibb.co/d7NGxjc/1.png',)
        client.send_message(message.chat.id, 'сорян за ошибку в фото')






def Punktoen(message):


    if message.text == 'I want to ask a question🙂':
        client.send_message(message.chat.id, 'Great🥳')
        client.send_message(message.chat.id, f'In our EMCD miners chat, you can ask your question,\n'
                                             'our support service will respond in Russian in 3 minutes', )
    elif message.text == 'I want a pool fee discount😠':
        client.send_message(message.chat.id, 'Great🥳')
        client.send_message(message.chat.id, 'Get a 20% discount on the mining pool commission for 30 days. \n'
                                             'ou can get a discount in one of the ways below:')
        client.send_message(message.chat.id, '1. Download the EMCD app and enter the TELEGRAM promo code when registering\n'
                                             '2. Register on the official website of the mining pool using this link\n'
                                             '3. Scan the QR code from your phone and enter the TELEGRAM promo code when registering')
        client.send_photo(message.chat.id, 'https://imgurhd.ru/i/8sd1.png')

    elif message.text == 'I am a large miner \n' \
                         '(I have more than 1 Ph/s)and I want VIP conditions':

        client.send_message(message.chat.id, 'Yeah, we pay an extra reward for every 1 Ph/s \n'
                                             'I have already passed your contact to the EMCD account manager, he will contact you soon. \n'
                                             'In the meantime, you can view the presentation about our cooperation.')





client.polling(none_stop=True)



