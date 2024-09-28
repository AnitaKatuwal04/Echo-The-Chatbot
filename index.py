from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import nltk
from nltk.tokenize import word_tokenize
import yaml

nltk.download('punkt')

chatbot = ChatBot(
    "echo",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///:memory:"
)

trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.FAQs")

print("Hi, I am echo the ChatBot")

while True:
    query=input(">>>")
    print(chatbot.get_response(Statement(text=query, search_text=query)))