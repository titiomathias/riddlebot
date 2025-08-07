import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from controllers.admin import verify_admin
from database.functions import users, subs, riddles

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
        if subs.getSub(ctx.author.id):
            await ctx.send("Resposta aceita!")
        else:
            await ctx.send("Você não está inscrito e não pode responder ao enigma atual.")
    else:
        await ctx.send("Use esse comando apenas via DM.")


# Comandos administradores

# Inserir inscrito
@bot.command("admin_sub")
async def insertSub(ctx, riddle_id, user_id):
    if verify_admin(ctx.author.id):
        if not users.getUser(user_id):
            users.insertUser(user_id)
        
        inscricao = subs.insertSub(riddle_id, user_id, True)

        if inscricao:
            await ctx.send(f"A inscrição do usuário de ID:{user_id} foi um sucesso!")
        else:
            await ctx.send(f"Ocorreu um erro ao realizar a inscrição do usuário de ID:{user_id}. Acesse os logs para mais detalhes.")


# Remover inscrito
@bot.command("admin_del")
async def insertSub(ctx, user_id):
    if verify_admin(ctx.author.id):
        return


# Listar detalhes de um enigma
@bot.command("admin_info")
async def insertSub(ctx, user_id):
    if verify_admin(ctx.author.id):
        return

bot.run(key)