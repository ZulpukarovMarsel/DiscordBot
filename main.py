import discord
import config
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='$', intents=intents)


class MyClient(discord.Client):
    def __init__(self, intents=None, **options):
        super().__init__(intents=intents, **options)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


client = MyClient(intents=intents)

# Замените 'your_bot_token_here' на фактический токен вашего бота
client.run(config.TOKEN)
