import nextcord
from nextcord.ext import commands
import dotos

class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['hi', 'hai', 'hallo', 'hey', 'hola'])
    async def do_hello(self, ctx):
        await ctx.send('hai!')

    @commands.command(name='ping', aliases=['pong', 'pding'])
    async def do_ping(self, ctx):
        await ctx.send('Pong!')

    if

def setup(bot):
    bot.add_cog(SimpleCog(bot))