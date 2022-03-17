import os
import discord
#from webserver import keep_alive
from neuralintents import GenericAssistant
import nltk
import sys

bot_token = os.environ['DISCORD_TOKEN']

prefix = "!" # prefix del bot

# Perchè devi funzionare cosi? che palle
print("[NLTK] Checking data..")
try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    print("[NLKT] Trying to download pack...")
    nltk.download('omw-1.4') # Spero che funzioni...
    print("[SYS] Stopping")
    sys.exit(0)

# Come creare un chatbot in 3 righe yay! (levando i print ovviamente)
print("[AI] Inizializzazione variabili...")
chatbot = GenericAssistant('intents.json')
print("[AI] Starting del Training...")
print(" ")
chatbot.train_model()
print(" ")
print("[AI] Salvataggio Modello...")
print(" ")
chatbot.save_model()

client = discord.Client()

@client.event
async def on_ready():
    print("[BOT] Pronto")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == 952274623989436476:
        #await message.channel.send("I checked and verified the channel.")
        #if message.content.startswith(f"{prefix}aibot"):
        response = chatbot.request(message.content)
        await message.channel.send(f"{message.author.mention} {response}")


#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith(f"{prefix}aibot"):
#        response = chatbot.request(message.content[7:])
#        await message.channel.send(f"{message.author.mention} {response}")

#keep_alive()
print(" ")
# print(f"Running on {client.user.id}")
print(f"Token: {bot_token}")
client.run(bot_token)