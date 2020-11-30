import random

#TODO more natural message types

random.seed()
def throw_a_dice():
    return "I'm throwing a dice. I got <" + str(random.randrange(1, 6)) + ">"

def check_for_roll(message):
    if(message.content.find("losuj") != -1 or message.content.find("roll") != -1 or message.content.find("rzuć") != -1 or message.content.find("rzucić") != -1):
        if(message.content.find("dice") != -1 or message.content.find("kości") != -1 or message.content.find("kość") != -1):
            return throw_a_dice()

    if (message.content.find("losuj") != -1 or message.content.find("get") != -1 or message.content.find("give") != -1 or message.content.find("podaj") != -1 or message.content.find("podać") != -1 or message.content.find("losować") != -1):
        if(message.content.find("losow") != -1 or message.content.find("random") != -1 or message.content.find("liczb") != -1):
            message.content = message.content.replace("?", "")
            if(len(message.content.split()) >= 2):
                for string in message.content.split():
                    if(string.isnumeric()):
                        number = int(string)
                        if(number <= 1):
                            return throw_a_dice()
                        return "I'm starting a random number generator (numbers from 1 to " + str(number) + "). I got <" + str(random.randrange(1, number)) + ">"
    return ""