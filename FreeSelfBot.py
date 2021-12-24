from functions.client import client
from termcolor import colored
from ping3 import ping
from art import *
import aiofiles
import discord
import sys
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()

print((colored('Free Discord SelfBot By', 'magenta')), (colored('Vazgen005#0001\n', 'red')))
try:
    file = open("token.txt", "r")
    token = file.readline()
    file.close()
    os.remove("token.txt")
except FileNotFoundError:
    token = (input(colored('Enter your authorization token to continue - ', 'cyan')))

clearConsole()

print((colored('Free Discord SelfBot By', 'magenta')), (colored('Vazgen005#0001\n', 'red')))


async def save_token_in_file(tok: str, filename: str):
    async with aiofiles.open(filename, 'w+') as a:
        await a.write(tok)


@client.event
async def on_ready():
    await save_token_in_file(token, "token.txt")
    clearConsole()
    await client.change_presence(status=discord.Status.offline)
    print((colored('Free Discord SelfBot By', 'magenta')), (colored('Vazgen005#0001\n', 'red')))
    print(colored(" Available commands:", "blue"),
          '''\nemb\nauthor\nnuz\nclear\naci\neval\ninfo\nnig\nrand\ncat\ndog\nopr\nspeed\nduck\nfox\nneko\n''',
          (colored("\n Any command start with a dot\n", "blue")))
    print(colored('SelfBot launched on account -', 'magenta'), (colored('{0.user}'.format(client), 'red')))


print((colored('Checking profile...\n', 'cyan')))

try:
    client.run(token, bot=False)
except:
    print((colored('Token is invalid, please try again', 'red')))
finally:
    os.system('pause')
    sys.exit()
