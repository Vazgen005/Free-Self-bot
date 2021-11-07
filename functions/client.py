from discord.ext import commands
client :  object = commands.Bot(command_prefix='.', self_bot=True)
token :   str = ""
anecdote : list = []
try:
    f = open('anecdote.txt', 'r', encoding='utf-8')
    anecdote = f.readlines()
    f.close()
except:
    ''