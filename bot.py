from discord_bot_token import ACCESS_TOKEN
import get_bash

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

@bot.tree.command(name="say")
@app_commands.describe(phrase = "What to say?")
async def say(interaction: discord.Interaction, phrase:str):
    await interaction.response.send_message(phrase)

@bot.tree.command(name="quote")
#@app_commands.describe(phrase = "Pulls a random quote off of bash.")
async def say(interaction: discord.Interaction):
    await interaction.response.send_message("```"+get_bash.get_random_bash_post()+"```")

bot.run(ACCESS_TOKEN)
