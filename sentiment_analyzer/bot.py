import telebot
from telebot import types
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import fasttext

fasttext.FastText.eprint = lambda x: None
tokenizer = RegexTokenizer()
FastTextSocialNetworkModel.MODEL_PATH = r'/Users/nataliakalinina/PycharmProjects/sentiment_analyzer/fasttext-social-network-model.bin'
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


API_token = 'token_text'

bot = telebot.TeleBot(API_token)


@bot.message_handler(commands=['start'])
def start(message):
    message_with_user_name = f'Привет, <b>{message.from_user.first_name}</b>. Я бот для анализа настроения твоего сообщения. Отправь мне любой текст'
    bot.send_message(message.chat.id, message_with_user_name, parse_mode='html')


@bot.message_handler()
def analyze_message(message):
    message_text = message.text

    results = model.predict([message_text])

    positive = 0
    negative = 0
    neutral = 0

    response = ''

    for result in results:
        try:
            positive += result['positive']
        except KeyError:
            pass

        try:
            negative += result['negative']
        except KeyError:
            pass

        try:
            neutral += result['neutral']
        except KeyError:
            pass

    if round(positive) > 0 and round(negative) == 0 and round(neutral) == 0:
        response = 'Ваше сообщение позитивное'
    elif round(positive) == 0 and round(negative) > 0 and round(neutral) == 0:
        response = 'Ваше сообщение негативное'
    elif round(positive) == 0 and round(negative) == 0 and round(neutral) > 0:
        response = 'Ваше сообщение нейтральное'

    bot.reply_to(message, response)


bot.polling(none_stop=True)
