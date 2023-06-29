Sometimes it can be really useful to understand which messages have negative or positive coloring. Especially if we’re talking about chat moderation. Instead of calling an admin (house chats are a sore topic!), it’s more convenient to enable automation of cleaning messages with a negative component, for example, insults or obscene language. So, this bot can be used for this aim.

Since I decided to work with the Russian language, the choice fell on the Dostoevsky python library. This model was trained on RuSentiment dataset and achieves up to ~0.71 F1 score.

So, lemmatization and stop-word removing depend on the specifics of your task. I decided not to use these two aspects. Moreover, Dostoevsky provides a model for sentiment-analysis that can work with raw texts. It means that you can transfer texts directly to the library without steps mentioned above.

However, lemmatization and stop-word removing can increase accuracy. If your task requires an accurate sentiment-analysis and you are dealing with a large amount of texts, in this case you should lemmatize and delete stop words before transferring texts to the Dostoevsky library. 

The library classifies the text into 5 classes:
- Negative;
- Positive;
- Neutral;
- speech act (formal greetings, thank-you and congratulatory posts);
- The "skip" class is for unclear cases.

In this project I’m interested only in negative, positive and neutral classes. Also remember that Dostoevsky doesn’t consider emojis as a component of tonality.

Let’s have a look at the algorithm of sentiment-analyzer implemented as a telegram-bot.
![sentiment-analyzer algorithm](https://github.com/NataliaKalinina13/tg_bot_sentiment_analyzer/assets/85068191/0fbc7207-d473-4d6b-8a74-03e2ecb78abf)


And this is the result! In the future I’ll improve and test new models, but now that’s it))
<img width="598" alt="Pasted Graphic" src="https://github.com/NataliaKalinina13/tg_bot_sentiment_analyzer/assets/85068191/69851699-4beb-4815-ae5b-0b2bcc8703ef">


Don't forget to install requirements and download model weights for sentiment analysis (https://storage.b-labs.pro/models/fasttext-social-network-model.bin)

FastTextSocialNetworkModel.MODEL_PATH = '/<some_folders>/fasttext-social-network-model.bin' model = FastTextSocialNetworkModel(tokenizer=tokenizer)
