import discord
from discord.ext import commands
from botcommandvariables import *
class adminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    commands.command(pass_context = True,
        help = 'clean up some spammy messages! Default value is 5 messages! [$purge (#)]',
        brief = 'easy clean-up.'
        )
    async def purge(ctx, amount=5):
        admins = [300075623458668544, 380829848932843531, 461210610261295105]
        if ctx.message.author.id not in admins:
            await ctx.message.delete()
            await ctx.channel.send('Sorry, you do not have the required perms for that command!') 
        elif amount > 50:
            await ctx.channel.send('Whoa! 50 or less at a time, please! I am small.')
        else:
            amount += 1 
            await ctx.channel.purge(limit=amount)
async def setup(bot):
    await bot.add_cog(adminCog(bot))