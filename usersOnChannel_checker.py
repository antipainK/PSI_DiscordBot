def check_for_usersOnChannel(message):
    if(message.content.find("user") != -1 or message.content.find("gamer") != -1 or message.content.find("player") != -1 or message.content.find("gracz") != -1 or message.content.find("użytkowni") != -1  or message.content.find("ludz") != -1 or message.content.find("people") != -1 or message.content.find("osób") != -1):
        if (message.content.find(" on ") != -1 or message.content.find(" na ") != -1 or message.content.find(" tu ") != -1 or message.content.find(" in ") != -1 or message.content.find("channel") != -1 or message.content.find("kanal") != -1):
            if (message.content.find("ile") != -1 or message.content.find("how") != -1 or message.content.find("many") != -1 or message.content.find("much") != -1 or message.content.find("ilu") != -1):
                return "There is a total of " + str(message.guild.member_count) + " people registered on this channel."
    return ""