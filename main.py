import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios, ten un buen dia!')

@bot.command()
async def estado(ctx):
    await ctx.send(f'Me encuentro en excelentes condiciones y tu?')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)
    
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Si, soy muy cool.  :sunglasses:')
 
@bot.command()
async def coinflip(ctx):
        x = random.randint(0, 1)
        if x == 0:
            resultado = 'sello'
        else:
            resultado = 'cara'
        await ctx.send(f'He lanzado tu moneda, y cayó en...  ' + resultado )

bot.run("token")
