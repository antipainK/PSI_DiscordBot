import discord
import configparser
from datetime import date, timedelta

from text_helper import *
from weather_checker import *
from roll_checker import *
from joke_checker import *
from again_checker import *
from cats_checker import *
from interactions_checker import *
from time_checker import *

client = discord.Client()
configParser = configparser.RawConfigParser()
configParser.read("settings.txt")

def read_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

token = read_token()

async def display_image(message, image_path):
    await message.channel.send(file=discord.File(image_path))

last_triggered = None

@client.event
async def on_message(message):
    global last_triggered
    if(message.channel.name=="psi_bot_chat" and message.author.bot==False):
        message.content = message.content.lower()

        temp = check_for_again(message, last_triggered)
        if(temp != ""):
            if(temp=="#CAT"):
                await display_image(message, "cached_cat_image.png")
            else:
                await message.channel.send(temp)
            return

        temp = check_for_weather(message, api_key=configParser.get("weather", "api_key"), city=configParser.get("weather", "city"))
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        temp = check_for_roll(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        temp = check_for_joke(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        temp = check_for_cats(message)
        if(temp != ""):
            await display_image(message, temp)
            last_triggered = "#CAT"

        temp = check_for_hello(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        temp = check_for_bye(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        temp = check_for_time(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)








client.run(token)