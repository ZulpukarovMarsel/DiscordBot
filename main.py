import discord
import config

class MyClient(discord.Client):
    def __init__(self, intents=None, **options):
        super().__init__(intents=intents, **options)

    async def on_ready(self):
        print(f"We have logged in as {self.user}")

    async def on_message(self, message):
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')


intents = discord.Intents.default()
intents.messages = True
client = MyClient(intents=intents)

client.run(config.TOKEN)
