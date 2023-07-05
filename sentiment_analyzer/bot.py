import telebot
import string
import fasttext
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


class SentimentAnalyzerBot:
    def __init__(self, api_token, model_path):
        self.tokenizer = RegexTokenizer()
        self.model = FastTextSocialNetworkModel(tokenizer=self.tokenizer)
        self.API_token = api_token
        self.bot = telebot.TeleBot(self.API_token)
        fasttext.FastText.eprint = lambda x: None
        FastTextSocialNetworkModel.MODEL_PATH = model_path

        @self.bot.message_handler(commands=['start'])
        def start(message):
            '''output a greeting after /start'''
            message_with_user_name = f'Привет, <b>{message.from_user.first_name}</b>. Я бот для анализа настроения твоего сообщения. Отправь мне любой текст'
            self.bot.send_message(message.chat.id, message_with_user_name, parse_mode='html')

        @self.bot.message_handler()
        def analyze_message(message):
            '''call the preprocessing function and conduct a sentiment-analysis'''
            preprocessed_message = self.preprocess_message(message)

            message_tokens = self.tokenizer.split(preprocessed_message)
            results = self.model.predict([str(message_tokens)])

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

            if positive > negative and positive > neutral:
                response = 'Ваше сообщение позитивное'
            elif negative > positive and negative > neutral:
                response = 'Ваше сообщение негативное'
            elif neutral > positive and neutral > negative:
                response = 'Ваше сообщение нейтральное'

            self.bot.reply_to(message, response)

    def preprocess_message(self, message):
        '''Lowercase text and remove punctuation'''
        low_message = message.text.lower()
        clean_punct_mess = low_message.translate(str.maketrans("", "", string.punctuation))
        return clean_punct_mess

    def run_bot(self):
        '''launch a bot'''
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    API_token = 'token_text'
    model_path = r'model_path'
    bot = SentimentAnalyzerBot(API_token, model_path)
    bot.run_bot()
