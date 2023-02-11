# biblioteca - pip install chatterbot 
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
import random
from spacy.cli import download
#download("en_core_web_sm")
DADOS_DE_TREINO = ['C:\\Users\\gulos\\OneDrive\\Documentos\\Projetos\\chat bot\ChatBot---chatterbot\\dadosDeTreino\\arquivo.json']
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
    
bot = ChatBot("python", tagger_language=ENGSM)
trainer = ListTrainer(bot)
conversa = []

for dados in DADOS_DE_TREINO:
    with open(dados, 'r', encoding='utf-8') as arq:
        todosDados = json.load(arq)
        conversa.append(todosDados['conversas'])
        arq.close()
        
for dados in conversa:
    for perguntas_respostas in dados:
        perguntas = perguntas_respostas['pergunta']
        resposta = perguntas_respostas['resposta']
        for pergunta in perguntas:
            trainer.train([pergunta, resposta])

while True:
    botResposta = bot.get_response(input('voce: ').lower())
    if float(botResposta.confidence) > 0.7:
        print('python: ', botResposta)
    else:
        n_reconheceu = ['não tenho certeza', 'n entendi', 'poderia digitar novamente?']
        print(random.choice(n_reconheceu))