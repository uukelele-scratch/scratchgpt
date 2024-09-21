import nltk
nltk.download('punkt_tab')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('ScratchGPT')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)

trainer.train("chatterbot.corpus.english","chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations")

trainer2.train(["Hello!","Hi there, Scratcher!","How are you?","I am good.","That is good to hear!","Thank you!","You are welcome!"])


def respondto(msg, usr):
	if msg != "" and msg != " ":
		return chatbot.get_response(msg)

