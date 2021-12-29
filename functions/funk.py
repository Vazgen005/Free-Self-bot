from client import client, anecdote
from collections import OrderedDict
from speedtest import Speedtest
from faker import Faker
from ping3 import ping
import contextlib
from art import *
import requests
import asyncio
import discord
import random
import string
import nekos
import json
import io

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
                ''


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
async def aci(ascii_send, acii):
    await ascii_send.message.delete()
    await ascii_send.send(embed=discord.Embed(description=('```\n' + text2art(acii) + '\n```'), color=0x2F3136))


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
    await cumm.send(file=discord.File(fp=io.BytesIO(requests.get(json.loads(requests.request(
        'GET',
        'https://api.thecatapi.com/v1/images/search').text)[0]['url']).content), filename='cat.png'))


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
    await spi.message.edit(content="",
                           embed=discord.Embed(
                               title='Please wait the internet speed is being measured...',
                               color=0xFF0000))
    try:
        def tofixed(numObj, digits=0):
            return f"{numObj:.{digits}f}"

        def pingg():
            a = []
            for i in range(5):
                a.append(ping('discord.com') * 1000)

            return str(int(sum(a) / len(a)))

        embspeed = discord.Embed(title='My internet speed', color=0xFF0000)
        embspeed.add_field(name='Ping: ',
                           value=pingg(),
                           inline=False)
        embspeed.add_field(name='Download speed: ',
                           value=str(f'{tofixed(Speedtest().download() / 8e+6, 1)} mb/s'),
                           inline=False)
        embspeed.add_field(name='Upload speed: ',
                           value=str(f'{tofixed(Speedtest().upload() / 8e+6, 1)} mb/s'),
                           inline=False)
        await spi.message.edit(embed=embspeed)
    except:
        await spi.message.edit(embed=discord.Embed(title='An error occurred during speedtest', color=0xFF0000))

@client.command()
async def ai(msg):
    inf = msg.message.content
    await msg.message.edit(content='', embed=discord.Embed(title='Loading...', color=0xfff500))

    def bab(textx):
        response = urllib.request.urlopen(urllib.request.Request("https://zeapi.yandex.net/lab/api/yalm/text3",
                                                                 data=json.dumps(
                                                                     {"query": textx, "intro": 0, "filter": 1}).encode(
                                                                     "utf-8"),
                                                                 headers={'Content-Type': 'application/json'}))
        textxx = json.loads(response.read().decode('utf-8'))['text']
        if textxx == '':
            return 'Err'
        else:
            return f"**{textx}** {textxx}"

    await msg.message.edit(content='', embed=discord.Embed(title='Balaboba', description=bab(inf[4:]), color=0xfff500))


@client.command()
async def rule(msg):
    await msg.message.delete()

    def porn():
        cum = json.loads(requests.get(
            url=f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit=1000&tags=-trap+-futanari+-furi+-big_breasts+-sketch+-gay+-gay_sex+-anthro+-breast_expansion+-breasts_bigger_than_head+-massive_breasts+-abs+-1boy+-2boys+-male_only+-animal_genitalia&pid={random.randint(1, 200)}').content)
        r = random.randint(0, 999)
        return requests.get(url=cum[r]['file_url']).content, cum[r]['image']

    porno = porn()
    try:
        await msg.send(file=discord.File(fp=io.BytesIO(porno[0]), filename=porno[1]))
    except discord.errors.HTTPException:
        m = await msg.send(
            embed=discord.Embed(
                title="Unfortunately, it didn't work out to send the content because someone has a media scanner turned on or you sent the message not to the NTFS channel",
                color=0xFF0000))
        await asyncio.sleep(10)
        await m.delete()