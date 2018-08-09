from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot('test')
convo = open('text1.txt','r').readlines()
bot.set_trainer(ListTrainer)
bot.train(convo)
while True:
	request = input('You: ')
	response = bot.get_response(request)
	print('Bot: ',response)