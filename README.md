# PSI_DiscordBot
A Discord chat bot written for PSI course at AGH University.

#### This repository is missing "token.txt" - you need to create it and put your bot's token inside.

A Discord bot with implemented intents.

Fully working in both English and Polish languages.

Intents:
- questions about weather (and daily forecast)
- rolling a dice, choosing random number
- telling a joke
- asking for a picture of a cat
- repeating a message
- welcoming messages
- goodbye messages
- asking for the time
- asking for running timers / notifiers
- telling a compliment
- telling about the amount of users on the channel
- counting how many messages were sent

___

1. Questions about weather and daily forecast
 - uses [OpenWeatherMap](https://openweathermap.org/) API to get both current weather data, as well as forecast for the next 7 days
 - you can use a variety of questions, like:
    - ***What's the weather like on monday?***
    - ***What's the weather?***
    - ***Jaka będzie pojutrze pogoda?***
    - ***Jaka pogoda będzie w następny czwartek?***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_1.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_2.png?raw=true)
 
2. Rolling a dice, choosing a random number
 - you can use a variety of questions, like:
    - ***Can you roll a dice for me?***
    - ***Wylosuj proszę liczbę do 22***
    - ***Give me random number smaller than 1000***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_3.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_4.png?raw=true)
  
3. Telling a joke
 - you can use a variety of questions, like:
    - ***Tell me a joke!***
    - ***Opowiedz mi kawał!***
    - ***I wanna hear a joke***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_5.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_6.png?raw=true)
 
4. Asking for a picture of a cat (or just wanting to see some online cat photos)
 - uses [AWS Random Cat](http://aws.random.cat/) API to get new cat photos each time you trigger this intent
 - everyone who talks about cats on Discord server clearly wants to see cats
 - you can use a variety of questions, like:
    - ***Give me cats, mrrr...***
    - ***Kotki!!!***
    - ***Can you supply me with the newest picture of a cat? Pretty please?***
    - ***Zapodaj zdjęcie kota, nie bądź sztywny***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_7.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_8.png?raw=true)
 
5. Repeating a message
 - meant to be triggered, when the user forgot, what the bot said last time
 - can be used to trigger even more cat photos
 - you can use a variety of questions, like:
    - ***Can you repeat?***
    - ***Again, please?***
    - ***Czy możesz powtórzyć?***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_9.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_10.png?raw=true)
 
6. Welcoming messages
 - meant to be triggered, whenever you welcome the bot
 - you can use a variety of questions, like:
   - ***Hello bot!***
   - ***Yo, bocie!***
   - ***Siema, psi_chat_bot!***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_11.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_12.png?raw=true)
 
7. Goodbye messages
 - meant to be triggered, whenever you say "goodbye" of sorts towards the bot
 - you can use a variety of questions, like:
   - ***Bye bot!***
   - ***Dobranoc bocie!***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_13.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_14.png?raw=true)
 
8. Asking for the time
 - you can use a variety of questions, like:
   - ***What's the time?***
   - ***Która godzina?***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_15.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_16.png?raw=true)
 
9. Asking for running a timer / notification
 - you can ask a bot to start a timer for a specified amount of time
 - bot distinguishes questions for seconds and minutes
 - none of the running timers are blocking (bot keeps on working and multiple timers can work in parallel)
 - you can use a variety of questions, like:
   - ***Can you start a timer for 2 minutes?***
   - ***Włącz proszę minutnik na 15 sekund***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_17.png?raw=true)

10. Asking for a compliment
 - if you ask for it, the bot will compliment you :)
 - you can use a variety of questions, like:
   - ***Please, tell me a compliment***
   - ***Skomplementuj mnie!***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_18.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_19.png?raw=true)
 
11. Telling about the amount of users on the channel
 - the bot can count up how many users are currently on the channel
   - ***Can you tell me, how many people are on this channel?***
   - ***Ile osób jest na kanale?***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_20.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_21.png?raw=true)
 
12. Counting how many messages were sent
 - the bot can go back "in time" and scroll through the entirety of the text channel and count
   - ***How many messages were sent on this channel?***
   - ***Ile wiadomości zostału ty wysłanych?***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_22.png?raw=true)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/blob/master/readMePictures/screenshot_23.png?raw=true)
 