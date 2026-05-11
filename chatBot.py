# Install library first
# pip install chatterbot
# pip install chatterbot-corpus
# pip install sqlalchemy==1.3.24

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
bot = ChatBot('Bot')

# Create trainer
trainer = ListTrainer(bot)

# Train chatbot
trainer.train([
    "Hi, can I help you",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "Where do you operate?",
    "We operate from Singapore",
    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",
    "I would like to speak to your customer service agent",
    "Please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
])

trainer.train([
    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",
    "How to contact customer service agent",
    "Please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
])

# Chat loop
while True:

    request = input("You: ")

    if request == 'OK' or request == 'ok':
        print("Bot: Bye")
        break

    else:
        response = bot.get_response(request)
        print("Bot:", response)