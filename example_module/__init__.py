import GoldyBot

AUTHOR = 'Dev Goldy'
AUTHOR_GITHUB = 'https://github.com/THEGOLDENPRO'
OPEN_SOURCE_LINK = 'https://github.com/Goldy-Bot/Example-GoldyBot-Module'


class YourExtension(GoldyBot.Extension):
    """An example extension. OwO"""

    def __init__(self, package_module=None):
        super().__init__(self, package_module_name=package_module)

    def loader(self):

        @GoldyBot.command()
        async def uwu(self:YourExtension, ctx):
            await ctx.send(f'Hi, {ctx.author.mention}! UwU!')


def load():
    # This function get's executed when the module is loaded so run all your extensions in here.
    # Example: YourExtension(package_module_name=__name__)

    YourExtension(__name__)