import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

key = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Bot online!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.guild is None:
        await message.channel.send(f"Olá, senhor! é um prazer estar ativo. Em qual fase do meu aprendizado estou?")
    else:
        await bot.process_commands(message)


bot.run(key)