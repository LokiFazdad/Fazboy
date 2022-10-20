import discord
from discord.ext import commands
from botcommandvariables import *
class funCog(commands.Cog, name='For Funsies'):
    def __init__(self, bot):
        self.bot = bot 
    @commands.command(pass_context = True,
        help='jim',
        brief="Jim."
        )
    async def jim(ctx):
        jim_copy = jimfotos.copy()
        randomjim = random.choice(jim_copy)
        jim_copy = jim_copy.remove(randomjim)
        await ctx.channel.send(randomjim)
    @commands.command(pass_context = True,
	    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	    brief="Prints pong back to the channel."
        )
    async def ping(ctx):
        await ctx.channel.send("pong")
    @commands.command(pass_context = True,
        help='more crazy logic for pong this time.',
        brief='prints ping to the channel'
        )
    async def pong(ctx):
        await ctx.channel.send('ping')
    @commands.command(pass_context = True, 
        help='picks a random joke by doing some math. Note that it was never said they would be good jokes.',
        brief='dont panic, the fazbot--he will tell you a joke.'
        )
    async def joke(ctx):
        jokes_copy = jokes.copy()
        rj = random.choice(jokes_copy)
        jokes_copy = jokes_copy.remove(rj)
        await ctx.channel.send(rj)
async def setup(bot):
    await bot.add_cog(funCog(bot))