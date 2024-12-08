from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot=ChatBot('chatbot',read_only=False,
            logic_adapters=[
                {
                'import_path':'chatterbot.logic.BestMatch',
                'dedault_response':'Sorry, I don\'t know what that means',
                'maximum_similarity_threshold':0.90,

                }
                ])

list_to_train = [

    "Hi",
    "Hi,There.",
    "What's your name?",
    "I'm a Quick.", 
    "What is your fav food? ",
    "I like questions.",
    
]


ChatterBotCorpusTrainer=ChatterBotCorpusTrainer(bot)


#list_trainer=ListTrainer(bot)
#list_trainer.train(list_to_train)
ChatterBotCorpusTrainer.train('chatterbot.corpus.english')


def members(request):
    return render(request,'first.html')

def getResponse(request):
    userMessage=request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)