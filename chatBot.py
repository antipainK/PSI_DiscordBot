import discord
import configparser
from datetime import date, timedelta

from text_helper import *
from weather_checker import *

client = discord.Client()
configParser = configparser.RawConfigParser()
configParser.read("settings.txt")

def read_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

token = read_token()

@client.event
async def on_message(message):
    if(message.channel.name=="psi_bot_chat" and message.author.bot==False):
        print(message.content)
        temp = check_for_weather(message, api_key=configParser.get("weather", "api_key"), city=configParser.get("weather", "city"))
        if(temp != ""):
            await message.channel.send(temp)
        if(message.content.find("jak") !=-1):
            await message.channel.send("kokokokoo")





client.run(token)