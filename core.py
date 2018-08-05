from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
from random import choice

updater = Updater(token='ur token here')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Заказал себе 40 см пиццу флорентину за 5000 рублей и "
                                                          "чяавэлли,"
                                                          " Jack Daniels + мою любимую порцию маринованных перчиков "
                                                          "чили."
                                                          " Сейчас вот думаю, сэвэн ап заказать или пепси. Пожалуй всё"
                                                          "таки сэвэн ап, в нём нет кофеина и он не так вреден как пеп"
                                                          "си. Привезут только через час, а у меня уже текут слюнки,"
                                                          " как и подобает настоящему эстету. А вы продолжайте считать "
                                                          "деньги и голодать, всратые нищебродские ничтожества.")


# функции
# TODO make talk to distortion bot
# TODO чекать лобас dota api
# TODO youtube links
# TODO google search
# TODO сделать по человечески это все(бтв думаю что так нельзя сингл тоном ебашить, хотя это же питон))


def RandomPaste(bot, update):
    with open('resource/OldsNotepad.txt', encoding="utf-8") as f:
        paste = f.readlines()
        textPaste = random.choice(paste)
        # if len(paste) else 'нах иди нема тексту))'
        bot.send_message(chat_id=update.message.chat_id, text=textPaste)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def CoinFlip(bot, update):
    if random.randint(0, 100) == 69:
        answer = 'ребро нахуй'
    else:
        answer = choice(['Орёл', 'Решка'])
    bot.send_message(chat_id=update.message.chat_id, text=answer)


RandomPaste_handler = CommandHandler('PastaOlda', RandomPaste)
CoinFlip_handler = CommandHandler('flip', CoinFlip)
start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(CoinFlip_handler)
dispatcher.add_handler(RandomPaste_handler)

updater.start_polling()
