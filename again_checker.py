def check_for_again(message, last_triggered):
    if(last_triggered != None):
        if(message.content.find("again") != -1 or message.content.find("powtórz") != -1 or message.content.find("powtórzyć") != -1 or message.content.find("one more") != -1 or message.content.find("jeszcze raz") != -1):
            return last_triggered
    return ""