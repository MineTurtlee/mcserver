import asyncio
import time
import subprocess
import logging
import os

# Startin' the server in async

async def server():
  try:
  process = await asyncio.create_subprocess_exec(
    "java", "-Xmx2G", "-jar", "server.jar", "nogui",
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False
  )
  return process
  except Exception as e:
  logging.error(f"Failed to start server process: {e}")
  return None
# Proxy Async

async def proxy():
  try:
    serverlink = os.getenv('SL')
    process = await asyncio.create_subprocess_exec(
      "ngrok", "http", f'--url={serverlink}', "25565", shell=False
    )
    return process
  except Exception as e:
    logging.error(f"Failed to start proxy process: {e}")
    return None

# Bot Async

async def bot():
  try:
    import discord
    from discord import errors
    import certifi

    token = os.getenv('Bot_Token')
    channelid = os.getenv('Channel_ID')
    serverlink = os.getenv('SL')

    os.environ["SSL_CERT_FILE"] = certifi.where()

    client = discord.Client(
      intents=discord.Intents.default(),
      activity=discord.Activity(name='The Minecraft server status', type=discord.ActivityType.listening)
    )

    class TheClient(discord.Client):
      async def on_ready(self):
        logging.info(f'Logged in as {self.user} (ID: {self.user.id})')
        await asyncio.sleep(120)
        logging.info("Sending started message...")
        channel = client.get_channel(int(channelid))
        if channel:
          await channel.send(f'The server is probably up at {serverlink}!')
          await asyncio.sleep(18000)
          await channel.send("Restarting to bypass the GH")
          await client.close()

    intents = discord.Intents.default()
    intents.message_content = True

    client = TheClient(intents=intents)
    await client.start(token)

  except discord.errors.LoginFailure as e:
    logging.error(f"Failed to login to Discord: {e}")
  except Exception as e:
    logging.error(f"An error occurred in the bot: {e}")

# Timer

async def Timer(server_process, proxy_process):
  await asyncio.sleep(18000)
  # Stop!!

  logging.info("Sending stop command to Minecraft server...")
  if server_process:
    server_process.stdin.write(b"stop\n")
    await server_process.stdin.drain()
  # Kill proxy
  logging.info("Terminating ngrok proxy...")
  if proxy_process:
    proxy_process.terminate()
    await proxy_process.wait()
  logging.info("All services have been stopped gracefully.")

# Running ALL of them
async def All():
  server_process = await asyncio.create_task(server())
  proxy_process = await asyncio.create_task(proxy())
  await asyncio.gather(bot(), Timer(server_process, proxy_process))

asyncio.run(All())
