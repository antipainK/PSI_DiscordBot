import random

random.seed()

hello_array = ["Yo, wassup?",
               "Oh, hi Mark.",
               "Hello world!",
               "Hi!",
               "Hello! How are you today?",
               "Why, Hi! How are you doing?",
               "Hello from the other sideee...",
               "Sieeeemanko, witam w mojej kuchni!"]

def check_for_hello(message):
    if(message.content.startswith("hi") or message.content.startswith("hello") or message.content.startswith("cześć") or message.content.startswith("siema") or message.content.startswith("yo") or message.content.startswith("witaj") or message.content.startswith("good morning") or message.content.startswith("good evening")):
        if(message.content.find("bot") != -1 or message.content.find("bocie") != -1 or message.content.find("psi") != -1):
            return hello_array[random.randrange(0, len(hello_array))]
    return ""

bye_array = ["Oh, too bad. Have a nice day!",
             "Have a nice day!",
             "Bye bye!",
             "I'm gonna miss you.",
             "I'll never forget about the time we spent together. Au revoir!"]

def check_for_bye(message):
    if(message.content.startswith("bye") or message.content.startswith("papa") or message.content.startswith("do widzenia") or message.content.startswith("dobranoc")):
        if(message.content.find("bot") != -1 or message.content.find("bocie") != -1 or message.content.find("psi") != -1):
            return bye_array[random.randrange(0, len(bye_array))]
    return ""