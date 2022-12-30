import nextcord
from nextcord.ext import commands
from nextcord.ext import application_checks

class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['hi', 'hai', 'hallo', 'hey', 'hola'])
    async def do_hello(self, ctx):
        await ctx.send('hai!')

    @commands.command(name='ping', aliases=['pong', 'pding'])
    async def do_ping(self, ctx):
        await ctx.send('Pong!')

    bot = commands.Bot(command_prefix="~", owner_id="398821987277078529")
    @commands.is_owner()
    @commands.command(name='bonk')
    async def do_bonk(self, ctx):
        await ctx.send('Shutting the bot down!')
        await self.bot.close()

def setup(bot):
    bot.add_cog(SimpleCog(bot))