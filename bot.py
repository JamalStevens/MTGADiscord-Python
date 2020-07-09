import os
import time
import json
from discord import File
from discord.ext import commands
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command(name='genpool', help='Generates a pool of 24 common and 12 uncommon', pass_context=True)
async def gen_pool(ctx, setabbr: str):
    file1 = open(f"{ctx.message.author.name} card list.txt", "w")
    await ctx.send(":black_circle:Common Cards")
    for x in range(2):
        url = f"https://api.scryfall.com/cards/random?q=s%3A{setabbr}+r%3Acommon+-t%3Abasic"
        with requests.get(url) as response:
            response_string = response.content
            response = json.loads(response_string)
        print(response['name'])
        await ctx.send(f"{response['name']} ({response['set'].upper()})")
        file1.write(f"1 {response['name']}\n")
        time.sleep(.500)

    await ctx.send(":blue_circle:Uncommon Cards")
    for x in range(2):
        url = f"https://api.scryfall.com/cards/random?q=s%3A{setabbr}+r%3Auncommon+-t%3Abasic"
        with requests.get(url) as response:
            response_string = response.content
            response = json.loads(response_string)
        print(response['name'])
        await ctx.send(f"{response['name']} ({response['set'].upper()})")
        file1.write(f"1 {response['name']}\n")
        time.sleep(.500)

    file1.close()
    await ctx.send(file=File(file1.name))
    os.remove(file1.name)


@gen_pool.error
async def gen_poolerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f':warning: Please include the desired 3 letter set abbr.\n`i.e. !genpool m21`')


# random common card
@bot.command(name='randomcommon', pass_context=True)
async def ran_common(ctx, setabbr: str):
        url = f"https://api.scryfall.com/cards/random?q=s%3A{setabbr}+r%3Acommon+-t%3Abasic"
        with requests.get(url) as response:
            response_string = response.content
            response = json.loads(response_string)
        print(response['name'])
        await ctx.send(f"[[{response['name']}]]")
        time.sleep(.500)


@ran_common.error
async def gen_poolerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f':warning: Please include the desired 3 letter set abbr.\n`i.e. !randomcommon m21`')


# random uncommon card
@bot.command(name='randomuncommon', pass_context=True)
async def ran_uncommon(ctx, setabbr: str):
        url = f"https://api.scryfall.com/cards/random?q=s%3A{setabbr}+r%3Auncommon+-t%3Abasic"
        with requests.get(url) as response:
            response_string = response.content
            response = json.loads(response_string)
        print(response['name'])
        await ctx.send(f"[[{response['name']}]]")
        time.sleep(.500)


@ran_uncommon.error
async def ran_uncommonerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f':warning: Please include the desired 3 letter set abbr.\n`i.e. !randomuncommon m21`')


# random rare card
@bot.command(name='randomrare', pass_context=True)
async def ran_rare(ctx, setabbr: str):
        url = f"https://api.scryfall.com/cards/random?q=s%3A{setabbr}+r%3Arare+-t%3Abasic"
        with requests.get(url) as response:
            response_string = response.content
            response = json.loads(response_string)
        print(response['name'])
        await ctx.send(f"[[{response['name']}]]")
        time.sleep(.500)


# random rare error
@ran_rare.error
async def ran_rareerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f':warning: Please include the desired 3 letter set abbr.\n`i.e. !randomrare m21`')


# random rare card
@bot.command(name='randommythic', pass_context=True)
async def ran_mythic(ctx, setabbr: str):
        url = f"https://api.scryfall.com/cards/random?q=s%3A{setabbr}+r%3Amythic+-t%3Abasic"
        with requests.get(url) as response:
            response_string = response.content
            response = json.loads(response_string)
        print(response['name'])
        await ctx.send(f"[[{response['name']}]]")
        time.sleep(.500)


# random rare error
@ran_mythic.error
async def ran_mythicerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f':warning: Please include the desired 3 letter set abbr.\n`i.e. !randommythic m21`')


bot.run(TOKEN)
