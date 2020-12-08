import time
import threading
import re

def timer_helper(time_in_seconds, messages_queue):
    messages_queue.put("\t*RRRRYNG* \t*RRRRYNG*\nThe selected time (" + str(time_in_seconds) +"s) is over.")
    return


def check_for_timers(message):
    if(message.content.find("timer") != -1 or message.content.find("stoper") != -1 or message.content.find("minutnik") != -1 or message.content.find("przypomnij") != -1):
        if (message.content.find("start") != -1 or message.content.find("włącz") != -1 or message.content.find("uruchom") != -1 or message.content.find("begin") != -1 or message.content.find("przypomnij") != -1):
            words_in_message = message.content.split()
            i = 0
            word = words_in_message[i]
            while(len(re.findall(r"\d+[\.\d+]?", word)) < 1 and i < len(words_in_message) - 1):
                i += 1
                word = words_in_message[i]

            if(i == len(words_in_message)-1):
                return ""
            else:   #znalazło czas, teraz szukam, czy sprecyzowano czy minuty, czy sekundy
                time_number = re.findall(r"\d+[\.\d+]?", word)
                if len(time_number) > 1:
                    time_number = float(time_number[0]) + float(time_number[1])/10
                else:
                    time_number = time_number[0]
                words_in_message = message.content.split()
                i = 0
                found_flag = False
                while (found_flag == False and i < len(words_in_message)):
                    word = words_in_message[i]
                    if(word.find("sec") != -1 or word.find("sek") != -1):
                        found_flag = True
                    i += 1

                if(found_flag):
                    return str(float(time_number)/60)
                else:
                    return str(time_number)
    return ""
