from cats_checker import *

def check_for_again(message, last_triggered):
    if(last_triggered != None):
        if(message.content.find("repeat") != -1 or message.content.find("again") != -1 or message.content.find("powtórz") != -1 or message.content.find("powtórzyć") != -1 or message.content.find("one more") != -1 or message.content.find("jeszcze raz") != -1 or message.content.find("inne") != -1 or message.content.find("więcej") != -1):
            if(last_triggered=="#CAT"):
                get_new_cat()
                return "#CAT"
            if(last_triggered=="#TIMER"):
                return ""
            return last_triggered
    return ""