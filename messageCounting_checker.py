async def check_for_messageCounting(message):
    if(message.content.find("count") != -1 or message.content.find("policz") != -1 or message.content.find("get") != -1 or message.content.find("sent") != -1 or message.content.find("wysłanych") != -1 or message.content.find("wysłali") != -1):
        if (message.content.find("message") != -1 or message.content.find("wiadomoś") != -1 or message.content.find("text") != -1 or message.content.find("tekst") != -1):
            if (message.content.find("ile") != -1 or message.content.find("how") != -1 or message.content.find("many") != -1 or message.content.find("much") != -1 or message.content.find("ilu") != -1):
                counter = 0
                async for msg in message.channel.history(limit=10000):
                    counter += 1
                return "On this channel there is a total of " + str(counter) + " messages. "
    return ""