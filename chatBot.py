import discord
import configparser
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from datetime import date, timedelta

client = discord.Client()
configParser = configparser.RawConfigParser()
configParser.read("settings.txt")

def read_token():
    with open("token.txt", "r") as file:
        return file.readlines()[0].strip()

token = read_token()

def create_line_of_chars(character):
    return "" + character * 50 + "\n"


one_call = None
one_call_acquire_date = None

def check_for_weather(message, api_key, city):
    if(message.content.find("pogoda") != -1 or message.content.find("weather") != -1 or message.content.find("forecast") != -1):

        owm = OWM(api_key)
        mgr = owm.weather_manager()

        global one_call
        global one_call_acquire_date
        if (one_call == None or one_call_acquire_date != date.today()):
            one_call = mgr.one_call(float(configParser.get("weather", "city_lat")), float(configParser.get("weather", "city_lon")))
            one_call_acquire_date = date.today()

        message_to_send = create_line_of_chars("=") + "Weather\n"


        if(message.content.find("dzisiaj") != -1 or message.content.find("dziś") != -1 or message.content.find("today") != -1):
            observation = mgr.weather_at_place(city)
            w = observation.weather
            message_to_send += city + " - " + str(date.today()) + " (today)\n"
            message_to_send += "Status: " + w.detailed_status.capitalize() + "\n"
            message_to_send += "Temperature: "+ " \tMin:" + str(w.temperature("celsius")["temp_min"]) + "°C \tCurrent:" + str(w.temperature("celsius")["temp"]) + "°C \tMax:" + str(w.temperature("celsius")["temp_max"]) + "°C\n"
            message_to_send += "Cloudiness: " + str(w.clouds) + "%\n"
            if (str(w.rain) != "{}"):
                message_to_send += "Rain: " + str(w.rain) + " (mm)\n"
            else:
                message_to_send += "Rain: 0mm\n"
            if (str(w.snow) != "{}"):
                message_to_send += "Snow: " + str(w.snow) + " (mm)\n"
            else:
                message_to_send += "Snow: 0mm\n"
            message_to_send += create_line_of_chars("=")
            return message_to_send



        elif(message.content.find("jutro") != -1 or message.content.find("tomorrow") != -1):
            w = one_call.forecast_daily[0]
            message_to_send += city + " - " + str(date.today() + timedelta(days=1)) + " (tomorrow)\n"

        elif(message.content.find("pojutrze") != -1):
            w = one_call.forecast_daily[1]
            message_to_send += city + " - " + str(date.today() + timedelta(days=2)) + " (in 2 days)\n"

        elif(message.content.find("monday") != -1 or message.content.find("poniedziałek") != -1):
            days_missing = (0 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"

        elif(message.content.find("tuesday") != -1 or message.content.find("wtorek") != -1):
            days_missing = (1 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"

        elif(message.content.find("wednesday") != -1 or message.content.find("środa") != -1):
            days_missing = (2 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"

        elif(message.content.find("thursday") != -1 or message.content.find("czwartek") != -1):
            days_missing = (3 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"

        elif(message.content.find("friday") != -1 or message.content.find("piątek") != -1):
            days_missing = (4 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"

        elif(message.content.find("saturday") != -1 or message.content.find("sobota") != -1):
            days_missing = (5 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"

        elif(message.content.find("sunday") != -1 or message.content.find("niedziela") != -1):
            days_missing = (6 - date.today().weekday()) % 7
            if(days_missing == 0):
                days_missing += 7
            w = one_call.forecast_daily[(days_missing-1) % 7]
            message_to_send += city + " - " + str(date.today() + timedelta(days=days_missing)) + " (in "+ str(days_missing) + " days)\n"
        else:
            return ""

        message_to_send += "Status: " + w.detailed_status.capitalize() + "\n"
        message_to_send += "Temperature: " + " \tMin:" + str(w.temperature("celsius")["min"]) + "°C \tDay:" + str(w.temperature("celsius")["day"]) + "°C \tMax:" + str(w.temperature("celsius")["max"]) + "°C\n"
        message_to_send += "Cloudiness: " + str(w.clouds) + "%\n"
        if (str(w.rain) != "{}"):
            message_to_send += "Rain: " + str(w.rain) + " (mm)\n"
        else:
            message_to_send += "Rain: 0mm\n"
        if (str(w.snow) != "{}"):
            message_to_send += "Snow: " + str(w.snow) + " (mm)\n"
        else:
            message_to_send += "Snow: 0mm\n"
        message_to_send += create_line_of_chars("=")
        return message_to_send
    return ""

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