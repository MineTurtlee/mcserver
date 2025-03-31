import asyncio
import time
import subprocess

# Startin' the server in async

async def server():
  subprocess.call("java -Xmx2G -jar server.jar nogui", shell=True)

# Proxy Async

async def proxy():
  subprocess.call("ngrok http --url=sharply-sought-chipmunk.ngrok-free.app 80", shell=True)

# Bot Async

async def bot():
  import discord.py
  
