import discord
import configparser
from datetime import date, timedelta
import threading
import queue
from discord.ext import commands, tasks
import asyncio


from text_helper import *
from weather_checker import *
from roll_checker import *
from joke_checker import *
from again_checker import *
from cats_checker import *
from interactions_checker import *
from time_checker import *
from timers_checker import *
from usersOnChannel_checker import *


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
configParser = configparser.RawConfigParser()
configParser.read("settings.txt")

def read_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

token = read_token()

async def display_image(message, image_path):
    await message.channel.send(file=discord.File(image_path))

messages_queue = queue.Queue()
last_triggered = None
last_message_channel = None

async def check_message_queue():
    while(True):
        await asyncio.sleep(1)
        if(last_message_channel != None):
            if(messages_queue.empty() == False):
                await last_message_channel.send(messages_queue.get())



@client.event
async def on_message(message):
    global last_message_channel
    last_message_channel = message.channel
    global last_triggered
    if(message.channel.name=="psi_bot_chat" and message.author.bot==False):
        message.content = message.content.lower()

        #1
        temp = check_for_again(message, last_triggered)
        if(temp != ""):
            if(temp=="#CAT"):
                await display_image(message, "cached_cat_image.png")
            else:
                await message.channel.send(temp)
            return

        #2
        temp = check_for_weather(message, api_key=configParser.get("weather", "api_key"), city=configParser.get("weather", "city"))
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #3
        temp = check_for_roll(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #4
        temp = check_for_joke(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #5
        temp = check_for_cats(message)
        if(temp != ""):
            await display_image(message, temp)
            last_triggered = "#CAT"

        #6
        temp = check_for_hello(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #7
        temp = check_for_bye(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #8
        temp = check_for_time(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #9
        temp = check_for_timers(message)
        if(temp != ""):
            last_triggered = "#TIMER"
            seconds = float(temp)*60
            messages_queue.put("New timer started! I will alert you in " + str(seconds) + " seconds!")
            t = threading.Timer(seconds, timer_helper, [seconds, messages_queue])
            t.start()

        #10
        temp = check_for_compliment(message)
        if(temp != ""):
            last_triggered = temp
            await message.channel.send(temp)

        #11
        temp = check_for_usersOnChannel(message)
        if (temp != ""):
            last_triggered = temp
            await message.channel.send(temp)



@client.event
async def on_ready():
    client.loop.create_task(check_message_queue())
    print(create_line_of_chars("#") + "\tBot is now fully working.\n" + create_line_of_chars("#"))

client.run(token)