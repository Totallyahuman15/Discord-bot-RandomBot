import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import asyncio
import os
import typing
import random

bot = commands.Bot(command_prefix="uwu", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("idk something random"))
    print("Successfully connected to server!")

@bot.command(name="info")
async def _info(ctx, arg1: typing.Optional[str] = None):
    async with ctx.typing():
        await asyncio.sleep(1)
        if arg1 == None:
            await ctx.reply("uwuinfo commands for commands everything else is random idk")
        elif arg1 == "commands":
            await ctx.reply("no")
        elif arg1 == "game":
            await ctx.reply("uwugame <game>; makes bot play a game (WARNING: ANYTHING INAPPROPRIATE MIGHT GET YOU KICKED OR BANNED!!!")

@bot.command(name="lol")
async def _lol(ctx, user: discord.User = None):
    async with ctx.typing():
        await asyncio.sleep(1)
        if user == None:
            await ctx.reply("lol")
        else:
            await ctx.reply(f"lol {user.mention}")

@bot.command(name="but")
async def _but(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("No buts, no cuts, no coconuts!")

@bot.command(name="hehehe")
async def _hehehe(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("ha!")

@bot.command(name="mute")
async def _mute(ctx, user: discord.Member = None):
    async with ctx.typing():
        await asyncio.sleep(1)
        if user == None:
            await ctx.reply("no user was specified")
        elif user != None and discord.utils.get(user.guild.roles, name="Muted") in user.roles:
            await user.remove_roles(discord.utils.get(user.guild.roles, name="Muted"))
            await ctx.reply(f"lol {user.mention} is free to go now")
        else:
            await ctx.reply("lol no")

@bot.command(name="random")
async def _random(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        x = random.randint(1, 10)
        if x == 7:
            await ctx.reply("UwU")
        else:
            await ctx.reply("lol no")

@bot.command(name="fuckyou")
async def _fuckyou(ctx):
    await ctx.author.kick(reason="fuck you too")
    await ctx.reply(f"Fuck you too {ctx.author.mention}")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user and message.content == "uwugame <game>; makes bot play a game (WARNING: ANYTHING INAPPROPRIATE MIGHT GET YOU KICKED OR BANNED!!!":
        await asyncio.sleep(3)
        await message.edit(content="uwugame <game>; makes bot play a game (WARNING: ANYTHING INAPPROPRIATE MIGHT GET YOU KICKED OR BANNED!!!)")
    else:
        if message.content == "uwu":
            await message.channel.send("UwU")
        else:
            return

@bot.command(name="game")
async def _game(ctx, game = None):
    if game == None:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("lol no")
    elif game == "uwu rule 34 eee.eeeeee.e game = reset":
        await ctx.message.delete()
        await bot.change_presence(activity=discord.Game("idk something random"))
        return
    else:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("lol no")
        await asyncio.sleep(3)
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("ugh, ok Fine. :rolling_eyes:")
            await asyncio.sleep(2)
            await bot.change_presence(activity=discord.Game(game))

@bot.command(name="randomcommandthatdoesabsolutelynothing")
async def _randomcommandthatdoesabsolutelynothing(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("lol")
    await asyncio.sleep(2)
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("that did absolutely nothing!")

@bot.command(name="Owo")
async def _Owo(ctx):
    async with ctx.typing():
        await ctx.message.delete()
        await asyncio.sleep(1)
        await ctx.send("Owo")

@bot.command(name="randomBot.py")
async def _randomBotdotpy(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("lol")
    await asyncio.sleep(2)
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("o wait...")
    await asyncio.sleep(0.1)
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("ur serious")
    await asyncio.sleep(1)
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("lol + ratio + XD")

@bot.command(name="giveRole")
@commands.has_permissions(administrator=True)
async def _giveRole(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("lol no")

@_giveRole.error
async def _giveRole_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Ok!")
        await asyncio.sleep(1)
        async with ctx.typing():
            await asyncio.sleep(1)
            msg = await ctx.reply("lol get trollwd XD")
            await asyncio.sleep(2.5)
            await msg.edit(content="lol get trolled XD")

@bot.command(name="gibBotToken")
async def _gibBotToken(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("Ok the token is:")
    await asyncio.sleep(1)
    async with ctx.typing():
        await asyncio.sleep(1)
        msg = await ctx.reply("lol get trooled XD")
    await asyncio.sleep(4)
    await msg.edit(content="lol get trolles XD")
    await asyncio.sleep(3)
    await msg.edit(content="lol get trolled XD")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)