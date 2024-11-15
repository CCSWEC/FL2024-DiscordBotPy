from discord_bot_token import ACCESS_TOKEN

# Just a comment to tech git to github push -- will remove ...


# This example requires the 'message_content' intent.

import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)


@bot.event
async def on_ready():
    print("Logged in and ready.")
    try:
        #synchronizes the slash commands with the bot user
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        # prints errors
        print(e)

#defines slash command with the @bot decorator
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!", ephemeral=True)

bot.run(ACCESS_TOKEN)
