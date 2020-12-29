# Discord-bot-Example

Creating two Discord Bot with Python

## Encourage disord bot

This program is written based on [**Code a Discord Bot with Python - Host for Free in the Cloud**](https://youtu.be/SPTfmiYiuok)

It uses a cloud computing platform called [**repl.it**](https://repl.it/@LiuLanLan/Discord-Bot#main.py), **repl.it database**, **discord library**, [**Random Quotes API**](https://zenquotes.io/) to create a Discord Bot that sends back encouraging messages based on user request. When a user types a sad word that is contained in ``["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]``, bot will return a random encouraging messgae from the databse.

It uses **Flask** to create a web server and [**Uptime Robot**](https://uptimerobot.com/) to ping the server every 5 mins, so the bot can be run continuously.

### Requirements:
- repl.it
- Uptime Robot
- Discord Server

A user can enter :
- ``$inspire`` : to get a random inspirational quote from an API
- ``$list``: to get a list of current enouraging phrases
- ``$new <message>``: to add a new encouraging phrase to database
- ``$responding true``: to enable bot returning encouraging message when it sees a sad phrase
- ``$responding false``: to disable bot returning encouraging message when it sees a sad phrase
- ``$del <index>``: to delete a encouraging message from the database


## AHA Music Player

This program is modified based on [**Make a Discord Bot with Python (Part 7: Music Bot) | Latest Discord Py Version**](https://youtu.be/ml-5tXRmmFk)

A music bot that has the ability to join and play music in server voice channel. 
A user can enter :
- ``~aha`` : to join the voice channel
- ``~play <url>`` : to play music. Program will convert it into .wav
- ``~pause`` : to pause current playing music
- ``~resume`` : to resume current playing music
- ``~stop`` : to stop current playing music
- ``~leave`` : to leave voice channel

### Requirements:
- Discord Server
- discord library
- youtube_dl
- FFmpeg


**P.S. Bot token needs to be added in .env**
