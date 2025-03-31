import asyncio
import time
import subprocess

# Startin' the server in async

async def server():
  process = await asyncio.create_subprocess_exec("java", "-Xmx2G", "-jar", "server.jar", "nogui", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
  return process
# Proxy Async

async def proxy():
  process = await asyncio.create_subprocess_exec("ngrok", "http", "--url=sharply-sought-chipmunk.ngrok-free.app", "25565", shell=False)
  return process
# Bot Async

async def bot():
  import asyncio
  import discord
  from   discord import errors
  import os
  import certifi
  
  token = os.getenv('Bot_Token')
  channelid= os.getenv('Channel_ID')
  serverlink = os.getenv('SL')

  os.environ["SSL_CERT_FILE"] = certifi.where()

  client = discord.Client(intents=discord.Intents.default(),activity=discord.Activity(name='The Minecraft server status', type=discord.ActivityType.listening))

  class TheClient(discord.Client):
    @client.event
    async def on_ready(self):
      print(f'Logged in as {self.user} (ID: {self.user.id})')
      await asyncio.sleep(120)
      print("Sending started message...")
      channel = client.get_channel(int(channelid))
      if channel:
        await channel.send(f'The server is probably up at {serverlink}!')
        await asyncio.sleep(18000)
        await channel.send("Restarting to bypass the GH")
        await client.close()

  intents = discord.Intents.default()
  intents.message_content = True

  client = TheClient(intents=intents)
  client.start(token)

# Timer

async def Timer(server_process, proxy_process):
  await asyncio.sleep(18000)
  # Stop!!
  
  print("Sending stop command to Minecraft server...")
  server_process.stdin.write(b"stop\n")
  server_process.stdin.flush()
  # Kill proxy
  print("Terminating ngrok proxy...")
  proxy_process.terminate()
  proxy_process.wait()
  print("All services have been stopped gracefully.")
# Running ALL of them
async def All():
  server_process = await asyncio.create_task(server())
  proxy_process = await asyncio.create_task(proxy())
  await asyncio.gather(bot(), Timer(server_process, proxy_process))
asyncio.run(All())
