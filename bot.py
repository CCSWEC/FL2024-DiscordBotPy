from discord_bot_token import ACCESS_TOKEN


# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == client.user:
            return
        if message.content.startswith("test"):
         channel = message.channel
         await channel.send("output_message")

#this function will send a message if the bot sees that another predefined message has been sent
async def send_message_on(message, input_message, output_message):
    
    if message.content.startswith(input_message):
         channel = message.channel
         await channel.send(output_message)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(ACCESS_TOKEN)
