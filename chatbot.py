from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(
    name="bot",
    read_only=True,
    logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch']
)

list_trainer = ListTrainer(my_bot)
list_trainer.train(['hi there!',
                    'hi!',
                    'how do you do?',
                    'how are you?',
                    'i\'m cool.',
                    'fine, you?',
                    'always cool.',
                    'i\'m ok',
                    'glad to hear that.',
                    'i\'m fine',
                    'glad to hear that.',
                    'i feel awesome',
                    'excellent, glad to hear that.',
                    'not so good',
                    'sorry to hear that.',
                    'what\'s your name?',
                    'i\'m a bot. ask me a math question, please.'])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train("chatterbot.corpus.english")

while True:
    try:
        answer = my_bot.get_response(input("User: "))
        if float(answer.confidence) > 0.2:
            print("Bot: ", answer)
        else:
            print("I can\'t understand you.")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
