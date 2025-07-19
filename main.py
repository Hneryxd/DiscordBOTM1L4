import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
comandos_lista = ['!bye - Te despides del Bot',
                   '!estado - Le preguntas al Bot como esta', 
                   '!heh - Reperita la palabra "heh" cantidad de veces que quieras si pones el numero despues', 
                   '!add - Se encargara de sumar los numeros que escribas(solo pueden ser 2 numeros)', 
                   '!repeat - El Bot repetira la palabra que escribas la cantidad de veces que quieras', 
                   '!bot - Descubrelo', 
                   '!coinflip - El Bot lanzara una moneda al aire, y te dira que salio']

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
        await ctx.send('He lanzado tu moneda, y cayó en...  ' + resultado )
@bot.command()
async def comandos(ctx):
    await ctx.send("Aquí te dejo una lista de los comandos disponibles:")
    for comando in comandos_lista:
        await ctx.send(comando)
    await ctx.send('Recuerda usar "!" para que tu comando funcione.')

bot.run("token")
