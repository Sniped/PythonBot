import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = client.Bot(command_prefix = "!")

@client.event
async def on_ready();
    print("Bot is ready!")

@client.event
async def on_message(message);
if message.content == "hello":
    await client.send_message(message.channel, "goodbye")


client.run("")
