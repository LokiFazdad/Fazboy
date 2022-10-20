import discord
from discord.ext import commands
import random
from botcommandvariables import *
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
member = discord.user
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)
bot = commands.Bot(command_prefix = '$', intents = intents, help_command = help_command)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for $how'))

@bot.event
async def on_message(message):
    if message.content.lower() == "hello":
        await message.channel.send(f"Hello, {message.author.mention}!")
    elif message.content.lower() == 'goodbye':
        await message.channel.send(f'Nice hangin out, {message.author.mention}! Buh byyyyyyye!')
    elif 'wtf' in message.content.lower():
        await message.channel.send('what the faz*fuck*, indeed, fazfam.')
    elif message.content.lower() =='bros':
        await message.channel.send('fazfam')
    elif message.content.lower() == 'gg':
        await message.channel.send(f'GG, {message.author.mention}!')
    elif 'i love you fazbot' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        elif message.author.id == 300075623458668544:
            await message.add_reaction('❤️')
            await message.channel.send('Love you too, mom.')
        elif message.author.id == 461210610261295105:
            await message.add_reaction('❤️')
            await message.channel.send('OMG DAD HAS FEELINGS.')
        else:
            await message.add_reaction('❤️')
            await message.channel.send(f'Aww, I love you, too {message.author.mention}.') 
    elif 'i love fazbot' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        elif message.author.id == 300075623458668544:
            await message.add_reaction('❤️')
            await message.channel.send('Love you too, mom.')
        elif message.author.id == 461210610261295105:
            await message.add_reaction('❤️')
            await message.channel.send('OMG DAD HAS FEELINGS.')
        else:
            await message.add_reaction('❤️')
            await message.channel.send(f'Aww, I love you, too {message.author.mention}.')
    elif 'fabzot i love you' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        elif message.author.id == 300075623458668544:
            await message.add_reaction('❤️')
            await message.channel.send('Love you too, mom.')
        elif message.author.id == 461210610261295105:
            await message.add_reaction('❤️')
            await message.channel.send('OMG DAD HAS FEELINGS.')
        else:
            await message.add_reaction('❤️')
            await message.channel.send(f'Aww, I love you, too {message.author.mention}.')
    elif 'i love you fazboy' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        elif message.author.id == 300075623458668544:
            await message.add_reaction('❤️')
            await message.channel.send('Love you too, mom.')
        elif message.author.id == 461210610261295105:
            await message.add_reaction('❤️')
            await message.channel.send('OMG DAD HAS FEELINGS.')
        else:
            await message.add_reaction('❤️')
            await message.channel.send(f'Aww, I love you, too {message.author.mention}.')
    elif  'i love fazboy' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        elif message.author.id == 300075623458668544:
            await message.add_reaction('❤️')
            await message.channel.send('Love you too, mom.')
        elif message.author.id == 461210610261295105:
            await message.add_reaction('❤️')
            await message.channel.send('OMG DAD HAS FEELINGS.')
        else:
            await message.add_reaction('❤️')
            await message.channel.send(f'Aww, I love you, too {message.author.mention}.')
    elif 'fabzoy i love you' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        elif message.author.id == 300075623458668544:
            await message.add_reaction('❤️')
            await message.channel.send('Love you too, mom.')
        elif message.author.id == 461210610261295105:
            await message.add_reaction('❤️')
            await message.channel.send('OMG DAD HAS FEELINGS.')
        else:
            await message.add_reaction('❤️')
            await message.channel.send(f'Aww, I love you, too {message.author.mention}.')
    elif message.content.lower() == 'hello there':
        await message.channel.send('https://media1.tenor.com/images/acbd64bbf3edf82833aacb8477ff5ec2/tenor.gif?itemid=15718579')
    elif 'fazbot' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        name_copy = nameResponse.copy()
        rn = random.choice(name_copy)
        name_copy = name_copy.remove(rn)
        await message.channel.send(rn)
    elif 'fazboy' in message.content.lower():
        if message.author.id == 1013446021134688347:
            return
        name_copy = nameResponse.copy()
        rn = random.choice(name_copy)
        name_copy = name_copy.remove(rn)
        await message.channel.send(rn)
    elif message.content.lower() == 'what do':
        what_copy = whatDo.copy()
        resp = random.choice(what_copy)
        what_copy = what_copy.remove(resp)
        await message.channel.send(resp)
    elif message.content.lower() == 'how do':
        how_copy = howDo.copy()
        res = random.choice(how_copy)
        how_copy = how_copy.remove(res)
        await message.channel.send(res)
    elif 'angry' in message.content.lower():
        await message.channel.send('Why we mad, bestie? Who we stabbin?')
    elif 'howdy' in message.content.lower():
        await message.channel.send('https://media1.tenor.com/images/3ab272eac29e787f7efec17e8e2c0f69/tenor.gif?itemid=5254840')
    elif 'my son' in message.content.lower():
        myson_copy = myson.copy()
        res = random.choice(myson_copy)
        myson_copy = myson_copy.remove(res)
        await message.channel.send(res)
    elif 'my boy' in message.content.lower():
        myson_copy = myson.copy()
        res = random.choice(myson_copy)
        myson_copy = myson_copy.remove(res)
        await message.channel.send(res)
    elif 'deathbattle' in message.content.lower():
        mentioned = message.mentions
        for user in mentioned:
            if user.id == 1013446021134688347:
                await message.add_reaction('😠')
        else:
            return
    await bot.process_commands(message)
@bot.command(pass_context = True,
    help = 'get the guild ID for the server the bot is on',
    brief = 'get guild ID information for the server'
)
async def serverid(ctx):
    id = ctx.message.guild.id
    await ctx.message.delete()
    await ctx.message.send(id)
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PING MESSAGE.
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send("pong")
@bot.command(
    help='more crazy logic for pong this time.',
    brief='prints ping to the channel'
)
async def pong(ctx):
    await ctx.channel.send('ping')
@bot.command(pass_context = True, 
    help='picks a random joke by doing some math. Note that it was never said they would be good jokes.',
    brief='dont panic, the fazbot--he will tell you a joke.'
)
async def joke(ctx):
    jokes_copy = jokes.copy()
    rj = random.choice(jokes_copy)
    jokes_copy = jokes_copy.remove(rj)
    await ctx.channel.send(rj)
@bot.command(
    help='posts a picture of the OG fazdad',
    brief='for when you want a picture of freddy'
)    
async def freddy(ctx):
    freddyfotos_copy = freddyfotos.copy()
    rff = random.choice(freddyfotos_copy)
    freddyfotos_copy = freddyfotos_copy.remove(rff)
    await ctx.message.delete()
    await ctx.channel.send(rff)
@bot.command(
    help='post a picture of chica',
    brief='for when you wanna look at a pizza obsessed chicken(or maybe markiplier\'s dog?)'
)
async def chica(ctx):
    chicafotos_copy = chicafotos.copy()
    rcf = random.choice(chicafotos_copy)
    chicafotos_copy = chicafotos_copy.remove(rcf)
    await ctx.message.delete()
    await ctx.channel.send(rcf)
@bot.command(
    help='posts a picture of foxy',
    brief='I feel like you should understand this at this point.'
)
async def foxy(ctx):
    foxyfotos_copy = foxyfotos.copy()
    rfx = random.choice(foxyfotos_copy)
    foxyfotos_copy = foxyfotos_copy.remove(rfx)
    await ctx.message.delete()
    await ctx.channel.send(rfx)
@bot.command(
    help='posts a picture of bonnie',
    brief='Bonnie the bunny. From FNAF. As a photo.'
)
async def bonnie(ctx):
    bonniefotos_copy = bonniefotos.copy()
    rbf = random.choice(bonniefotos_copy)
    bonniefotos_copy = bonniefotos_copy.remove(rbf)
    await ctx.message.delete()
    await ctx.channel.send(rbf)
@bot.command(
    help='posts a photo from the fnaf/afton nonsense.',
    brief='fnaf + afton = fnafton or something.'
)
async def fnafton(ctx):
    fnaftonfotos_copy = fnaftonfotos.copy()
    rfa = random.choice(fnaftonfotos_copy)
    fnaftonfotos_copy = fnaftonfotos_copy.remove(rfa)
    await ctx.message.delete()
    await ctx.channel.send(rfa)
@bot.command(
    help='this posts my good morning message because fazdad is fazforgetful.',
    brief='a daily reminder for yous'
)
async def morning(ctx):
    await ctx.message.delete()
    await ctx.channel.send('Good morning, my faztastic ~~followers~~ friends! Here is your reminder to hydrate, medicate, masticate, and meditate!')
@bot.command(
    help='jim',
    brief="Jim."
)
async def jim(ctx):
    jim_copy = jimfotos.copy()
    randomjim = random.choice(jim_copy)
    jim_copy = jim_copy.remove(randomjim)
    await ctx.channel.send(randomjim)
@bot.command(
    help = 'log a drink! even just a glass of water! The world is yours for the taking!',
    brief = 'keep track of your liquid intake however you see fit.'
)
async def cheers(ctx):
    cheersmessages_copy = cheersmessages.copy()
    randomcheers = random.choice(cheersmessages_copy)
    cheersmessages_copy = cheersmessages_copy.remove(randomcheers)
    serverid = ctx.message.guild.id
    with open(f'cheerstokelog{serverid}.txt', 'a') as log:
        log.write(f'Drink logged by {ctx.message.author} in {ctx.message.guild} \n')
    await ctx.channel.send(randomcheers)
@bot.command(
    help='one for the drinks means one for the tokes.',
    brief='log them hits, baybeeeee.'
)
async def toke(ctx):
    tokeresponses_copy = tokeresponses.copy()
    randomtoke = random.choice(tokeresponses_copy)
    tokeresponses_copy = tokeresponses_copy.remove(randomtoke)
    serverid = ctx.message.guild.id
    with open(f'cheerstokelog{serverid}.txt', 'a') as log:
        log.write(f'Toke logged by {ctx.message.author} in {ctx.message.guild} \n')
    await ctx.channel.send(randomtoke)
@bot.command(
    help = 'doot or be dooted',
    brief = 'spooky'
)
async def doot(ctx):
    await ctx.message.delete()
    await ctx.channel.send('🎺💀🎺')
@bot.command(
    help = 'this gives the total "drinks" had in the server since the last time the log was cleared',
    brief = 'how much has the server had? fazbot can and will tell you.'
)
async def welit(ctx):
    serverid = ctx.message.guild.id
    with open(f'cheerstokelog{serverid}.txt') as log:
        drinks = len(log.readlines())
    await ctx.channel.send(f'{ctx.message.guild} has {drinks} entries so far! Leggo.')
@bot.command(
    help = 'this will show you how many drinks/tokes *you* have had in the server you use the command in',
    brief = 'how much have you had? find out here!'
)
async def melit(ctx):
    serverid = ctx.message.guild.id
    member = ctx.message.author
    with open(f'memberlog{member}.txt', 'w') as tracker:
        tracker.write('')
    with open (f'cheerstokelog{serverid}.txt') as file, open(f'memberlog{member}.txt', 'a') as tracker:
        for line in file.readlines():
            if str(member) in line:
                tracker.write(line)
    with open(f'memberlog{member}.txt') as log:
        memberdrinkcount = len(log.readlines())
    await ctx.channel.send(f'You have {memberdrinkcount} entries so far, {ctx.message.author.mention}')
@bot.command(
    help = 'Give a suggestion for bot things [$suggest (suggestions-separated by comma)]',
    brief = 'got an idea? gimme.'
)
async def suggest(ctx, *args):
    member = ctx.message.author
    with open('botsuggestions.txt.', 'a') as suggestions:
        suggestions.write('')
        suggestions.write(f'{args} suggested by: {member}. \n ')
    await ctx.message.delete()
    await ctx.channel.send('Thanks, friend! Your suggestion has been added to the list!')
@bot.command(
    help = 'Show the current suggestions on the list!',
    brief = 'Wanna know if a suggestion has been made already?'
)
async def suggestlist(ctx):
    with open('botsuggestions.txt') as list:
        suggestlist = ' '
        for line in list.readlines():
            suggestlist = suggestlist + line
    await ctx.channel.send(f'Currently listed suggestions: {suggestlist}')
@bot.command(
    help = 'clears the server drink log',
    brief = 'start the drinking over from 0!'
)
async def closingtime(ctx):
    serverid = ctx.message.guild.id
    members = []
    for member in ctx.message.guild.members:
        members.append(member)
    with open(f'cheerstokelog{serverid}.txt', 'r') as infile, open ('secretmaster.txt', 'a') as outfile:
        outfile.write(str(infile.readlines()))
    with open(f'cheerstokelog{serverid}.txt', 'w') as file:
        file.write('')
    for member in members:
        with open(f'memberlog{member}.txt', 'w') as log:
            log.write('')
    await ctx.channel.send(f'{ctx.message.author.mention} has cleared the tracker for {ctx.message.guild}! Time to refill it!')
@bot.command(
    help = 'this just tells you how to use the bot kinda sorta',
    brief = 'how does this thing work, anyway?'
)
async def how(ctx):
    with open('secret.txt') as help:
        helplist = ''
        for line in help.readlines():
            helplist = helplist + line
    await ctx.channel.send(f' Here you go, {ctx.message.author.mention} : {helplist}')
@bot.command(
    help='I scream, you scream...',
    brief='for when you just have to scream.'
)
async def screm(ctx):
    await ctx.message.delete()
    await ctx.channel.send('https://thumbs.gfycat.com/AcademicAltruisticEft-max-1mb.gif111111111111')
@bot.command(
    help = 'posts a reaction image',
    brief = 'for when you really just have so many questions'
)
async def wut(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/1008951081918804069/1016520836674498560/f51cb9884e4060bdfc195fc244985a0d.jpg")
@bot.command(
    help = 'prints the entered values back to the channel [$print -text to echo-]',
    brief = '$print *insert words here*'
)
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)
@bot.command(
    help = 'invite a friend (or Gamzee) for games! [$games @usertotag(optional)]',
    brief = 'is that a homestuck reference?'
)
async def games(ctx, member=None):
    if not member:
        member = 'gamzee'
    else:
        member = member
    await ctx.message.delete()
    await ctx.channel.send(f"hey {member} you wanna play gamezees with me?")
 
@bot.command(
    help = 'clean up the last 1-50 messages! Default value is 5 messages! [$purge (#)]',
    brief = 'easy clean-up.'
)
async def purgeall(ctx, amount=5, name='purge all'):
    admins = [300075623458668544, 380829848932843531, 461210610261295105]
    if ctx.message.author.id not in admins:
        await ctx.message.delete()
        await ctx.channel.send('Sorry, you do not have the required perms for that command!') 
    elif amount > 50:
        await ctx.channel.send('Whoa! 50 or less at a time, please! I am small.')
    else:
        amount += 1 
        await ctx.channel.purge(limit=amount)

bot.run(bottoken)
