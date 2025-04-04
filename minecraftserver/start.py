import asyncio
import time
import subprocess
import logging
import os
import aiohttp
import re

logging.basicConfig(level=logging.INFO)

# Startin' the server in async
async def server():
    try:
        process = await asyncio.create_subprocess_exec(
            "java", "-Xmx2G", "-jar", "server.jar", "nogui",
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False
        )
        asyncio.create_task(log_output(process.stdout, "Minecraft"))
        asyncio.create_task(log_output(process.stderr, "Minecraft Error"))
        return process
    except Exception as e:
        logging.error(f"Failed to start server process: {e}")
        return None

# Proxy Async
async def proxy():
    try:
        process = await asyncio.create_subprocess_exec(
            "ssh", "-i", "~/.ssh/id_rsa", "-o", "StrictHostKeyChecking=no", "-R", "mineturtle2.serveo.net:443:localhost:7272", "serveo.net",
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False
        )
        await asyncio.sleep(5)  # Give ngrok time to initialize
        return process
    except Exception as e:
        logging.error(f"Failed to start proxy process: {e}")
        return None

async def log_output(stream, prefix):
    while True:
        line = await stream.readline()
        if line:
            logging.info(f"{prefix}: {line.decode().strip()}")
        else:
            break

# async def get_ngrok_tunnel_url():
    # async with aiohttp.ClientSession() as session:
        # async with session.get('http://localhost:4040/api/tunnels') as response:
           #  data = await response.json()
           #  tunnel_url = data['tunnels'][0]['public_url']
           #  def exclude(tunnel_string):
            #     matching = re.search(r'https://(.*)', tunnel_string)
            #     matching2 = re.search(r'http://(.*)', tunnel_string)
            #     if matching:
            #         link = matching.group(1)
           #          return link
         #        else:
       #              return None
     #            if matching2:
   #                  link = matching2.group(1)
 #                    return link
# 
#             tunnel_link = exclude(tunnel_url)
#             return tunnel_link

# Bot Async
async def bot(tunnel_link):
    try:
        import discord
        from discord import errors
        import certifi

        token = os.getenv('Bot_Token')
        channelid = os.getenv('Channel_ID')

        os.environ["SSL_CERT_FILE"] = certifi.where()
        
        class TheClient(discord.Client):
            async def on_ready(self):
                logging.info(f'Logged in as {self.user} (ID: {self.user.id})')
                await asyncio.sleep(20)
                logging.info("Sending started message...")
                channel = self.get_channel(int(channelid))
                if channel:
                    await channel.send(f'<@&1356936657709957150> The server is probably up at [mineturtle2.serveo.net](https://mineturtle2.serveo.net)!')
                    await asyncio.sleep(3595)
                    await channel.send("Restarting to bypass the GH")
                    await self.close()

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
    await asyncio.sleep(3600)
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
    await asyncio.gather(bot(tunnel_url), Timer(server_process, proxy_process))

asyncio.run(All())
