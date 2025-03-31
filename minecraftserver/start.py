import asyncio
import time
import subprocess

# Startin' the server in async

async def server():
  subprocess.call("java -Xmx2G -jar server.jar nogui", shell=True)

# Proxy Async

async def proxy():
  subprocess.call("ngrok http --url=sharply-sought-chipmunk.ngrok-free.app 25565", shell=True)

# Bot Async

async def bot():
  import discord
  from   discord import errors
  import os
  import certifi
  
  token = os.getenv('Bot_Token')
  channelid= os.getenv('Channel_ID')

  os.environ["SSL_CERT_FILE"] = certifi.where()

  client = discord.Client(intents=discord.Intents.default(),activity=discord.Activity(name='The Minecraft server status', type=discord.ActivityType.listening))

  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user.id})')
    asyncio.sleep(120)
    print("Sending started message...")
    channel = client.get_channel(channelid)
    await channel.send("The server is probably up at https://sharply-sought-chipmunk.ngrok-free.app!")
  
