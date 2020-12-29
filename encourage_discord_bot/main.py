import discord
import os
# make http request, get data from api
# data is json
import requests
import json
import random
# use database from replit
from replit import db 

from keep_alive import keep_alive

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements =[
  "Cheer up!",
  "Hang in there",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  # request data from api
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def update_encouragements(encouraging_message):
  if "encouraging_message" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    # save back to database
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements


# register an event
@client.event

# called when bot is ready to use
async def on_ready():
  # get user name
  print('We have logged in as {0.user}'.format(client))

@client.event
# called when a message is received
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$inspire'):
    quote = get_quote()
    # return a message back to discord using await
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements=[]
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on")
    else:
      db["responding"] = False
      await message.channel.send("Responding is false")


keep_alive()

# run bot, put bot token here from .env
client.run(os.getenv('TOKEN'))


