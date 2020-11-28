import random

#TODO more natural message types

random.seed()
def throw_a_dice():
    return "I'm throwing a dice. I got <" + str(random.randrange(1, 6)) + ">"

def check_for_roll(message):
    if(message.content.find("losuj") != -1 or message.content.find("roll") != -1 or message.content.find("random") != -1 or message.content.find("dice") != -1 or message.content.find("kości") != -1):
        return throw_a_dice()
    if(message.content.startswith("losuj") or message.content.startswith("roll") or message.content.startswith("random")):
        if(len(message.content.split()) <= 2):
            if(message.content.split()[1].isnumeric()):
                number = int(message.content.split()[1])
                if(number <= 1):
                    return throw_a_dice()
                return "I'm starting a random number generator (numbers from 1 to " + str(number) + "). I got <" + str(random.randrange(1, number)) + ">"
    return ""