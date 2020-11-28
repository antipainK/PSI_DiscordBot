from datetime import datetime

def check_for_time(message):
    if(message.content.find("what time is it") != -1 or message.content.find("która jest godzina") != -1 or message.content.find("która godzina") != -1 or message.content.find("tell me the time") != -1 or message.content.find("tell time") != -1 or message.content.find("what's the time") != -1):
        return "Currently: " + str(datetime.now())[:-6]
    return ""
