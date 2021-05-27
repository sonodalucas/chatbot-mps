from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(
    name="bot",
    logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch']
)

list_trainer = ListTrainer(my_bot)
list_trainer.train([

    'Oi?',  # User
    'Oi, eu sou o chatbot mais curioso dos cinemas, conta pra mim sobre um filme que você assistiu :)',  # bot
    'Qual o seu nome?',  # User
    'Conta pra mim, bot feito para conversar sobre filmes.',  # bot
    'Prazer em te conhecer',  # User
    'Igualmente, tem algum filme legal para conversar sobre?',  # bot
    'Quantos anos você tem?',  # User
    'Eu nasci em 2021.',  # bot
    'Você gosta de filmes?',  # User
    'Adoro, me conte um pouco sobre o que você tem assistido.',  # bot
    'Qual o seu personagem favorito?',  # User
    'Gandalf, o mago.',  # bot
    'Você gosta de pipoca?',  # User
    'Sim, melhor coisa para comer assistindo filmes, apesar de que bot não comem.',  # bot
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.portuguese')

print("Bot: Eu sou Conta pra mim, chatbot dedicado a conversar com você sobre os filmes que assistiu.")
while True:
    try:
        answer = my_bot.get_response(input("User: "))
        if float(answer.confidence) > 0.1:
            print("Bot: ", answer)
        else:
            print("Não entendo.")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
