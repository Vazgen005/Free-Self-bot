import aiofiles
import asyncio
import contextlib
import discord
import io
import json
import nekos
import numpy
import os
import random
import requests
import string
import sys
from art import *
from collections import OrderedDict
from discord.ext import commands
from faker import Faker
from ping3 import ping
from speedtest import Speedtest
from termcolor import colored


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()

client = commands.Bot(command_prefix='.', self_bot=True)
token = ""
anecdote = []

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
          "\nemb\nauthor\nnuz\nclear\naci\neval\ninfo\nnig\nrand\ncat\ndog\nopr\nspeed\nduck\nfox\nneko\n",
          (colored("\n Any command start with a dot\n", "blue")))
    print(colored('SelfBot launched on account -', 'magenta'), (colored('{0.user}'.format(client), 'red')))


try:
    f = open('anecdote.txt', 'r', encoding='utf-8')
    anecdote = f.readlines()
    f.close()
except:
    None


@client.command()
async def emb(emb_send, *, text):
    await emb_send.message.delete()
    await emb_send.send(embed=discord.Embed(description=text, color=0xff0000))


embedVar2 = discord.Embed(
    title="Free Discord SelfBot",
    description="special thanks ZertMARK#9934 and voidptr_t#1488 for helping in creating this bot",
    color=0xff0000)
embedVar2.set_author(name="Vazgen005#0001",
                     icon_url="https://i.imgur.com/lyqGACo.gif")


@client.command()
async def author(author_send):
    await author_send.message.delete()
    await author_send.send(embed=discord.Embed(
        title="Free Discord SelfBot",
        description="special thanks ZertMARK#9934 and voidptr_t#1488 for helping in creating this bot",
        color=0xff0000).set_author(
        name="Vazgen005#0001",
        icon_url="https://i.imgur.com/lyqGACo.gif"))


@client.command()
async def nuz(n_send):
    if anecdote.__len__() != 0:
        await n_send.message.delete()
        await n_send.send(embed=discord.Embed(
            title=(str("**Нуждик № " + ''.join(random.choice(string.digits) for _ in range(3)) + "**")),
            description=random.choice(anecdote), color=0xFF0000))
    else:
        await n_send.message.delete()
        m = await n_send.send(
            embed=discord.Embed(
                title="create anecdote.txt with anecdotes to use this command",
                color=0xFF0000))
        await asyncio.sleep(5)
        await m.delete()


@client.command()
async def clear(ctx, limit: int = None):
    async for msg in ctx.message.channel.history(limit=(limit + 1)):
        if msg.author.id == client.user.id:
            try:
                await msg.delete()
            except:
                None


@client.command()
async def eval(ctx, code):
    await ctx.message.delete()
    str_obj = io.StringIO()
    try:
        with contextlib.redirect_stdout(str_obj):
            exec(code)
    except Exception as e:
        return await ctx.send(
            embed=discord.Embed(title='An error occurred while executing the code', description=(
                f"```py\n{e.__class__.__name__}: {e}\n```"),
                                color=0xFF0000))
    if not str_obj.getvalue():
        await ctx.send(
            embed=discord.Embed(title='Code was executed', description=f'```\nno output\n```', color=0xC79800))
    else:
        await ctx.send(embed=discord.Embed(title='Code was executed', description=f'```py\n{str_obj.getvalue()}\n```',
                                           color=0x00FF00))


@client.command()
async def aci(ascii_send, *, aci):
    await ascii_send.message.delete()
    Art = text2art(aci)
    await ascii_send.send(embed=discord.Embed(description=(('```\n' + Art + '\n```')), color=0x2F3136))


@client.command()
async def info(inf, user: discord.User = None):
    await inf.message.delete()
    if not user:
        user = inf.author
    embinfo = discord.Embed(title='Account information - ' + user.display_name + '#' + user.discriminator,
                            color=0xFF0000)
    embinfo.add_field(name="Created at", value=str(user.created_at)[:-7], inline=False)
    embinfo.set_thumbnail(url=user.avatar_url)
    embinfo.add_field(name='ID', value=user.id, inline=False)
    await inf.send(
        embed=discord.Embed(
            title='Account information - ' + user.display_name + '#' + user.discriminator,
            color=0xFF0000).add_field(
            name="Created at", value=str(user.created_at)[:-7], inline=False).set_thumbnail(
            url=user.avatar_url).add_field(
            name='ID', value=user.id, inline=False))


@client.command()
async def nig(contex):
    await contex.message.delete()
    for i in list("🇳🇮🇬🇪🇷🇸"):
        await contex.message.reference.resolved.add_reaction(i)


locales = OrderedDict([
    ('en-US', 1),
    ('ru_RU', 2),
])


@client.command()
async def rand(rand_s):
    await rand_s.message.delete()
    fake1 = Faker(locales)
    await rand_s.send(
        embed=discord.Embed(
            description=f'1: {fake1["en-US"].name()}\n2: {fake1["en-US"].address()}\n3: {fake1["en-US"].job()}\n4: {fake1["ru_RU"].phone_number()}\n',
            color=0xFF0000))


@client.command()
async def cat(cumm):
    await cumm.message.delete()
    cumer = requests.request('GET', 'https://api.thecatapi.com/v1/images/search')
    cum = (json.loads(cumer.text))
    r = requests.get(cum[0]['url'])
    g = await cumm.send(file=discord.File(fp=io.BytesIO(r.content), filename='cat.png'))


@client.command()
async def dog(cumm):
    await cumm.message.delete()
    cumer = requests.request('GET', 'https://api.thedogapi.com/v1/images/search')
    cum = (json.loads(cumer.text))
    r = requests.get(cum[0]['url'])
    await cumm.send(file=discord.File(fp=io.BytesIO(r.content), filename='dog.png'))


@client.command()
async def duck(cumm):
    await cumm.message.delete()
    cumer = requests.request('GET', 'https://random-d.uk/api/v2/random')
    cum = (json.loads(cumer.text))
    r = requests.get(cum['url'])
    await cumm.send(file=discord.File(fp=io.BytesIO(r.content), filename='duck.png'))


@client.command()
async def fox(cumm):
    await cumm.message.delete()
    cumer = requests.request('GET', 'https://randomfox.ca/floof/')
    cum = (json.loads(cumer.text))
    r = requests.get(cum['image'])
    await cumm.send(file=discord.File(fp=io.BytesIO(r.content), filename='fox.png'))


@client.command()
async def neko(ee, dd=None):
    await ee.message.delete()
    if dd is None:
        await ee.send(embed=discord.Embed(color=0xFF0000).add_field(
            value='trap\nfutanari\nhololewd\nlewdkemo\nsolog\nfeetg\ncum\nerokemo\nles\nwallpaper\nlewdk\nngif\ntickle\nlewd\nfeed\ngecg\neroyuri\neron\ncum_jpg\nbj\nnsfw_neko_gif\n',
            name='All categories:').add_field(
            value='solo\nkemonomimi\nnsfw_avatar\ngasm\npoke\nanal\nslap\nhentai\navatar\nerofeet\nholo\nketa\nblowjob\npussy\ntits\nholoero\nlizard\npussy_jpg\npwankg\nclassic\nkuni\n',
            name='‌').add_field(
            value='waifu\npat\n8ball\nkiss\nfemdom\nneko\nspank\ncuddle\nerok\nfox_girl\nboobs\nrandom_hentai_gif\nsmallboobs\nhug\nero\nsmug\ngoose\nbaka\nwoof\nfeet\nyuri',
            name='‌').set_thumbnail(
            url='https://cdn.discordapp.com/attachments/800761015797022740/896185585667035177/unknown.png'))
    else:
        try:
            cum = nekos.img(dd)
        except:
            await ee.send(embed=discord.Embed(title='Unknown category', color=0xFF0000).add_field(
                value='trap\nfutanari\nhololewd\nlewdkemo\nsolog\nfeetg\ncum\nerokemo\nles\nwallpaper\nlewdk\nngif\ntickle\nlewd\nfeed\ngecg\neroyuri\neron\ncum_jpg\nbj\nnsfw_neko_gif\n',
                name='All categories:').add_field(
                value='solo\nkemonomimi\nnsfw_avatar\ngasm\npoke\nanal\nslap\nhentai\navatar\nerofeet\nholo\nketa\nblowjob\npussy\ntits\nholoero\nlizard\npussy_jpg\npwankg\nclassic\nkuni\n',
                name='‌').add_field(
                value='waifu\npat\n8ball\nkiss\nfemdom\nneko\nspank\ncuddle\nerok\nfox_girl\nboobs\nrandom_hentai_gif\nsmallboobs\nhug\nero\nsmug\ngoose\nbaka\nwoof\nfeet\nyuri',
                name='‌').set_thumbnail(
                url='https://cdn.discordapp.com/attachments/800761015797022740/896185585667035177/unknown.png'))
        else:
            try:
                await ee.send(file=discord.File(fp=io.BytesIO(requests.get(cum).content), filename=cum[28::]))
            except:
                m = await ee.send(
                    embed=discord.Embed(
                        title="Unfortunately, it didn't work out to send the content because someone has a media scanner turned on or you sent the message not to the NTFS channel",
                        color=0xFF0000))
                await asyncio.sleep(10)
                await m.delete()


@client.command()
async def opr(opr_send):
    await opr_send.message.delete()
    f = await opr_send.send('https://cdn.discordapp.com/attachments/743955975387611197/891414955620958208/unknown.png')
    await f.add_reaction('1️⃣')
    await f.add_reaction('2️⃣')


@client.command()
async def speed(spi):
    await spi.message.edit(content="", embed=discord.Embed(title='Please wait the internet speed is being measured...',
                                                           color=0xFF0000))
    try:
        def tofixed(numObj, digits=0):
            return f"{numObj:.{digits}f}"

        def pingg():
            a = []
            for i in range(5):
                a.append(ping('discord.com') * 1000)
            return str(int(numpy.mean(a)))

        embspeed = discord.Embed(title='My internet speed', color=0xFF0000)
        embspeed.add_field(name='Ping: ', value=pingg(), inline=False)
        embspeed.add_field(name='Download speed: ', value=str(f'{tofixed(Speedtest().download() / 8e+6, 1)} mb/s'),
                           inline=False)
        embspeed.add_field(name='Upload speed: ', value=str(f'{tofixed(Speedtest().upload() / 8e+6, 1)} mb/s'),
                           inline=False)
        await spi.message.edit(embed=embspeed)
    except:
        await spi.message.edit(embed=discord.Embed(title='An error occurred during speedtest', color=0xFF0000))


print((colored('Checking profile...\n', 'cyan')))

try:
    client.run(token, bot=False)
except:
    print((colored('Token is invalid, please try again', 'red')))
finally:
    os.system('pause')
    sys.exit()
