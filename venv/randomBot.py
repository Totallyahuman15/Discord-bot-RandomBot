import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import asyncio
import os
import typing
import random
import time

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

timmyTimer: int = 0
timmyReady = 1
timmyCanReply = 1

@bot.command(name="show")
async def _show(ctx, time: typing.Optional[int] = 5):
    global timmyTimer, timmyReady
    try:
        if time <= 0:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply("nah im good")
        elif time > 60:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply("Max time limit is 60 seconds (1 min)")
        elif timmyTimer <= 0 and timmyReady == 1:
            timr = time + 25
            timmyReady = 0
            async with ctx.typing():
                await asyncio.sleep(1)
                msg1 = await ctx.send(":eye: :lips: :eye:")
                msg2 = await ctx.send(":thumbsdown:             :thumbsup: ")
                msg3 = await ctx.send(":foot:         :foot:")
            original = 1
            while time > 0:
                await asyncio.sleep(1)
                if original == 1:
                    await msg2.edit(content=":thumbsup:             :thumbsdown: ")
                    original = 0
                    time -= 1
                else:
                    await msg2.edit(content=":thumbsdown:             :thumbsup: ")
                    original = 1
                if time == 0:
                    await msg1.delete()
                    await msg2.delete()
                    await msg3.delete()
                    timmyReady = 1
                    timmyTimer = timr
                    async with ctx.typing():
                        await asyncio.sleep(1)
                        await ctx.reply("Timmy is tired now :c")
        elif timmyTimer > 0:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply(f"Timmy is still tired! {timmyTimer} seconds left untill Timmy's next show!")
        elif timmyReady != 1 or timmyReady == 0:
            await ctx.message.delete()
        else:
            return
        while timmyTimer > 0:
            await asyncio.sleep(1)
            timmyTimer -= 1
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

@bot.command(name="nickName")
async def _nickName(ctx, newNick: str = None):
    try:
        if newNick == None:
            await ctx.author.edit(nick=ctx.author.name)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply("Successfully reset your username!")
        else:
            await ctx.author.edit(nick=newNick)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply(f"Successfully changed your username to {newNick}")
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

@bot.command(name="nick")
@commands.has_permissions(administrator=True)
async def _nick(ctx, user: discord.Member = None, *, nick: str = None):
    if nick == None:
        async with ctx.typing():
            await asyncio.sleep(1)
            await user.edit(nick=user.name)
            await ctx.reply(f"Successfully changed {user.mention}'s name to {nick}")
    else:
        async with ctx.typing():
            await asyncio.sleep(1)
            await user.edit(nick=nick)
            await ctx.reply(f"Successfully changed {user.mention}'s nickname to {nick}")

@bot.command(name="hsow")
async def _hsow(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("lol")
    await asyncio.sleep(1)
    async with ctx.typing():
        await asyncio.sleep(1)
        msg = await ctx.reply("Imagine spelling hsow wrong")
    await asyncio.sleep(2)
    await msg.edit(content="Imagine spelling show wrong")

@bot.command(name="hswo")
async def _hswo(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("Bru-")
    await asyncio.sleep(1)
    async with ctx.typing():
        await asyncio.sleep(1)
        msg = await ctx.reply("How do you spwll show that wrong?")
    await asyncio.sleep(2)
    await msg.edit(content="How do you spell show that wrong?")

@bot.command(name="shwo")
async def _shwo(ctx):
    async with ctx.typing():
        await asyncio.sleep(1)
        await ctx.reply("...")
    await asyncio.sleep(1)
    async with ctx.typing():
        await asyncio.sleep(1)
        msg = await ctx.reply("HOE DOES ONE SPELL SHOW WRONG?!?!?!?!?!?!?!!11/1?1?!")
    await asyncio.sleep(2)
    await msg.edit(content="HOW DOES ONE SPELL SHOW WRONG?!?!?!?!?!?!?!!11/1?1?!")

@bot.command(name="boo")
async def _boo(ctx):
    if timmyReady == 0 and timmyCanReply == 1:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("HOW DARE YOU BOO TIMMY!")
    elif timmyReady == 0 and timmyCanReply == 0:
        return
    else:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.reply("?")

@bot.command(name="cheer")
async def _cheer(ctx):
    if timmyReady == 0 and timmyCanReply == 1:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("You got 1 Timmy Token (TT)!")
        await asyncio.sleep(1)
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("You can do absolutely nothing with TTs!")
    elif timmyReady == 0 and timmyCanReply == 0:
        return
    else:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("?")

@bot.command(name="cookie")
async def _cookie(ctx, *, amount: typing.Optional[int] = 1):
    try:
        if amount > 222:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply("Max is 222")
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                cookies = []
                while amount > 0:
                    cookies.append(":cookie:")
                    amount -= 1
                if amount == 0:
                    await ctx.reply(" ".join(cookies))
                else:
                    pass
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

@bot.command(name="ttscookie")
async def _ttscookie(ctx, *, amount: typing.Optional[int] = 1):
    try:
        if amount > 222:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply("Max is 222")
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                cookies = []
                while amount > 0:
                    cookies.append(":cookie:")
                    amount -= 1
                if amount == 0:
                    await ctx.reply(" ".join(cookies), tts=True)
                else:
                    pass
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

@bot.command(name="W")
async def _w(ctx):
    try:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Agreed")
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

@bot.command(name="death")
async def _death(ctx):
    try:
        async with ctx.typing():
            sec = random.randint(0, 59)
            min = random.randint(0, 59)
            hour = random.randint(0, 23)
            day = random.randint(0, 364)
            month = random.randint(0, 11)
            year = random.randint(0, 75)
            await asyncio.sleep(1)
            await ctx.reply(f"You will die in {year} year(s), {month} month(s), {day} day(s), {hour} hour(s), {min} minute(s), and {sec} second(s)")
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

@bot.command(name="trap")
async def _trap(ctx):
    try:
        msg = await ctx.reply(":mouse_trap:")
        await msg.add_reaction("🧀")
        def check(reaction, user):
            return user != bot.user and str(reaction.emoji) in ["🧀"] and reaction.message == msg
        reaction, confirmation = await bot.wait_for("reaction_add", check=check, timeout=60)
        if confirmation:
            await msg.clear_reactions()
            await ctx.send(f"{confirmation.mention} fell for the trap!")
            await confirmation.add_roles(discord.utils.get(confirmation.guild.roles, name="Gullible"))
    except asyncio.TimeoutError:
        return

@bot.command(name="smort")
@commands.has_permissions(administrator=True)
async def _smort(ctx, *, user: discord.Member):
    try:
        if discord.utils.get(user.guild.roles, name="Gullible") in user.roles:
            async with ctx.typing():
                await asyncio.sleep(1)
                await user.remove_roles(discord.utils.get(user.guild.roles, name="Gullible"))
                await ctx.reply(f"{user.mention} is now smort and goodly edumacated!")
        else:
            return
    except:
        return

@bot.command(name="fastergame")
async def _fastergame(ctx):
    try:
        async with ctx.typing():
            await asyncio.sleep(1)
            msg = await ctx.reply("Whoever reacts first wins!")
            await msg.add_reaction("⏩")
        def check(reaction, user):
            return user != bot.user and str(reaction.emoji) in ["⏩"] and reaction.message == msg
        reaction, confirm = await bot.wait_for("reaction_add", check=check, timeout=60)
        if confirm:
            await msg.clear_reactions()
            await ctx.send(f"{confirm.mention} Wins!!!")
    except:
        return

@bot.command(name="reactionMessage")
async def _reactionMessage(ctx, emoji: str, message: str):
    try:
        msg = await ctx.reply(message)
        await msg.add_reaction(emoji)
        def check(reaction, user):
            return user != bot.user and str(reaction.emoji) in [emoji] and reaction.message == msg
        reaction, wait = await bot.wait_for("reaction_add", check=check)
        if wait:
            await msg.remove_reaction(emoji=emoji, member=wait)
    except:
        return

@bot.command(name="mrr")
@commands.has_permissions(administrator=True)
async def _mrr(ctx, emoji: str, role: discord.Role, times: typing.Optional[int] = 1):
    await ctx.message.delete()
    msg = await ctx.send(f"React for '{role}' role!")
    await msg.add_reaction(emoji)
    def check(reaction, user):
        return user != bot.user and str(reaction.emoji) in [emoji] and reaction.message == msg
    while times > 0:
        reaction, wait = await bot.wait_for("reaction_add", check=check)
        if wait:
            await msg.remove_reaction(emoji=emoji, member=wait)
            await wait.add_roles(role)
            times -= 1

@bot.command(name="happy")
async def _happy(ctx, wink: typing.Optional[bool] = False):
    try:
        if wink != True:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply(":grinning: :thumbsup: ")
        else:
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.reply(":wink: :thumbsup: ")
    except:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.reply("Error!")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)