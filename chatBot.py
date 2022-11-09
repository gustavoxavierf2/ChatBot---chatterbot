# biblioteca - pip install chatterbot 
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from spacy.cli import download
download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

   
bot = ChatBot("python", tagger_language=ENGSM)
conversa = ['eae', 'blz?', 'tudobem?', 'eu estou bem']
conversa2 = ['qual seu fime preferido?', 'de volta pro futuro']

trainer = ListTrainer(bot)
trainer.train(conversa)
trainer.train(conversa2)


while True:
    resposta = bot.get_response(input('voce: '))
    if float(resposta.confidence) > 0.7:
        print('python: ', resposta)
    else:
        print('não tenho certeza')