#modules
from unicodedata import name
import nextcord
from nextcord.ext import commands
import logging
import dotos

#logging
logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='onuwbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s |  %(message)s'))
logger.addHandler(handler)

def get_prefix(bot, message):
    prefixes = ['~']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)

loadup_extensions = ['cogs.simple']

bot = commands.Bot(command_prefix=get_prefix, owner_id=dotos.OWNER_ID)

if __name__ == '__main__':
    for extension in loadup_extensions:
        bot.load_extension(extension)
        ext = extension.strip('cogs.')
        print(extension, 'commands have been loaded successfully')

@bot.event
async def on_ready():
    print(f'\n\nLogged in as {bot.user.name} - {bot.user.id}\nVersion: {nextcord.__version__}')
    game = nextcord.Game('Among Us')
    await bot.change_presence(status=nextcord.Status.online, activity=game)
    print('Successfully logged in and booted...!')

bot.run(dotos.TOKEN, reconnect=True)