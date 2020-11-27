import random

random.seed()

jokes_array = ["-Why do Java programmers have to wear glasses? \n\n-Because they don't C#.",
               "3 Database SQL walked into NoSQL bar.\nA little while later... they walked out.\n\nBecause they couldn't find a table.",
               "The programmer got stuck in the shower because the instructions on the shampoo said...\n\nLather, Rinse, Repeat",
               "A SQL query goes into a bar, walks up to two tables and asks...\n\nCan I join you?",
               "Programmers don't see women as objects.\n\nThey consider each to be in a class of their own.",
               "Why does Python live on land?\n\nBecause it's above C-level.",
               "I failed my python breeding class because of a late assignment.\n\nMy homework ate my dog.",
               "Why did the Python programmer guy got rejected by a Java programmer girl?\n\nHe was not her type.",
               "What was a python's first words?\n\nprint('s'\*10)"]

def check_for_joke(message):
    if(message.content.find("tell") != -1 or message.content.find("hear") != -1 or message.content.find("opowiedz") != -1):
        if(message.content.find("joke") != -1 or message.content.find("żart") != -1 or message.content.find("kawał") != -1):
            return jokes_array[random.randrange(0, len(jokes_array))]
    return ""