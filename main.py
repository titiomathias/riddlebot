import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

key = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='+', intents=intents, help_command=None)

# Eventos

@bot.event
async def on_ready():
    print("Bot online!")

# Comandos

# Respondendo via DM
@bot.command("resposta", aliases=["responder", "answer"])
async def answer(ctx, answer):
    if ctx.guild is None:
        if answer == "1235":
            await ctx.send("✅ Resposta correta!")
        else:
            await ctx.send("❌ Resposta incorreta.")
    else:
        await ctx.send("Use esse comando apenas via DM.")


# Comandos administradores

# Inserir inscrito
@bot.command("admin_sub")
async def insertSub(ctx, user_id):
    return

# Remover inscrito
@bot.command("admin_del")
async def insertSub(ctx, user_id):
    return

# Listar detalhes de um enigma
@bot.command("admin_info")
async def insertSub(ctx, user_id):
    return

bot.run(key)