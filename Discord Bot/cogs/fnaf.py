import discord
from discord.ext import commands
import random
from botcommandvariables import *
class fnafCog(commands.Cog, name='FNAF'):
    def __init__(self, bot):
        self.bot = bot 
    @commands.command(pass_context = True,
        help='posts a picture of the OG fazdad',
        brief='for when you want a picture of freddy'
        )    
    async def freddy(ctx):
        freddyfotos_copy = freddyfotos.copy()
        rff = random.choice(freddyfotos_copy)
        freddyfotos_copy = freddyfotos_copy.remove(rff)
        await ctx.message.delete()
        await ctx.channel.send(rff)
    @commands.command(pass_context = True,
        help='post a picture of chica',
        brief='for when you wanna look at a pizza obsessed chicken(or maybe markiplier\'s dog?)'
        )
    async def chica(ctx):
        chicafotos_copy = chicafotos.copy()
        rcf = random.choice(chicafotos_copy)
        chicafotos_copy = chicafotos_copy.remove(rcf)
        await ctx.message.delete()
        await ctx.channel.send(rcf)
    @commands.command(pass_context = True,
        help='posts a picture of foxy',
        brief='I feel like you should understand this at this point.'
        )
    async def foxy(ctx):
        foxyfotos_copy = foxyfotos.copy()
        rfx = random.choice(foxyfotos_copy)
        foxyfotos_copy = foxyfotos_copy.remove(rfx)
        await ctx.message.delete()
        await ctx.channel.send(rfx)
    @commands.command(pass_context = True,
        help='posts a picture of bonnie',
        brief='Bonnie the bunny. From FNAF. As a photo.'
        )
    async def bonnie(ctx):
        bonniefotos_copy = bonniefotos.copy()
        rbf = random.choice(bonniefotos_copy)
        bonniefotos_copy = bonniefotos_copy.remove(rbf)
        await ctx.message.delete()
        await ctx.channel.send(rbf)
    @commands.command(pass_context = True,
        help='posts a photo from the fnaf/afton nonsense.',
        brief='fnaf + afton = fnafton or something.'
         )
    async def fnafton(ctx):
        fnaftonfotos_copy = fnaftonfotos.copy()
        rfa = random.choice(fnaftonfotos_copy)
        fnaftonfotos_copy = fnaftonfotos_copy.remove(rfa)
        await ctx.message.delete()
        await ctx.channel.send(rfa)


async def setup(bot):
    await bot.add_cog(fnafCog(bot))