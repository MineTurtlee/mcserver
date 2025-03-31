import asyncio
import time
import subprocess
import logging
import os
import aiohttp

# Startin' the server in async
async def server():
    try:
        process = await asyncio.create_subprocess_exec(
            "java", "-Xmx2G", "-jar", "server.jar", "nogui",
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False
        )
        return process
        print("Minecraft:" + stdout)
    except Exception as e:
        logging.error(f"Failed to start server process: {e}")
        return None

# Proxy Async
async def proxy():
    try:
        process = await asyncio.create_subprocess_exec(
            "ngrok", "tcp", "7272", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False
        )
        await asyncio.sleep(5)  # Give ngrok time to initialize
        return process
        print("NGROK:" + stdout)
    except Exception as e:
        logging.error(f"Failed to start proxy process: {e}")
        return None

async def get_ngrok_tunnel_url():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:4040/api/tunnels') as response:
            data = await response.json()
            tunnel_url = data['tunnels'][0]['public_url']
            return tunnel_url

# Bot Async
async def bot(tunnel_url):
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
                await asyncio.sleep(75)
                logging.info("Sending started message...")
                channel = self.get_channel(int(channelid))
                if channel:
                    await channel.send(f'The server is probably up at {tunnel_url}!')
                    await asyncio.sleep(18000)
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
    tunnel_url = await get_ngrok_tunnel_url()
    await asyncio.gather(bot(tunnel_url), Timer(server_process, proxy_process))

asyncio.run(All())
