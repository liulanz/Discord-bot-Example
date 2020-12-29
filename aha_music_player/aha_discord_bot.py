import discord
import os
import youtube_dl
from discord.ext import commands


client = commands.Bot(command_prefix="~")


@client.command()
async def play(ctx, url: str):
  song = os.path.isfile("song.wav")
  try:
    if song:
      os.remove("song.wav")
  except PermissionError:
    await ctx.send("Wait..")
    return

  
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  
  ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    for file in os.listdir("./"):
      if file.endswith(".wav"):
        os.rename(file, "song.wav")
    voice.play(discord.FFmpegPCMAudio("song.wav"))
  


  # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  #   ydl.download([url])
  #   for file in os.listdir("./"):
  #     if file.endswith(".mp3"):
  #       os.rename(file, "song.mp3")
  #   voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def aha(ctx):
  # connecting to the voice channel
  voiceChannel=ctx.message.author.voice.channel
  await voiceChannel.connect()
  await ctx.send("哈喽！这里是 ~啊哈播放器 \n Hi this is ~AHA Music Player.")
  

@client.command()
async def leave(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_connected():
    await voice.disconnect()
    await ctx.send("~啊哈: 拜拜。\n ~AHA: BYE")


@client.command()
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
    await ctx.send("~啊哈: 已暂停\n ~AHA: PAUSED")

@client.command()
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
    await ctx.send("~啊哈: 继续播放\n ~AHA: RESUMING")

@client.command()
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.stop()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  


# keep_alive()

client.run(os.getenv('TOKEN'))


