# biblioteca - pip install chatterbot 
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
import random
from spacy.cli import download
download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
bot = ChatBot("python", tagger_language=ENGSM)
trainer = ListTrainer(bot)
conversa = []

json = json.loads(open('json.json', 'r').read())
for iterador in json:
    if len(iterador['mensagens']) <= 1:
        conversa.append(" ".join(iterador['mensagens']))      
    conversa.append((iterador['resposta']))

bot = ChatBot("python", tagger_language=ENGSM)
trainer = ListTrainer(bot)

trainer.train(conversa)

while True:
    resposta = bot.get_response(input('voce: ').lower())
    if float(resposta.confidence) > 0.7:
        print('python: ', resposta)
    else:
        n_reconheceu = ['não tenho certeza', 'n entendi', 'poderia digitar novamente?']
        print(random.choice(n_reconheceu))