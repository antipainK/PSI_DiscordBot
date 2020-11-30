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
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_1.png)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_2.png)
 
2. Rolling a dice, choosing a random number
 - you can use a variety of questions, like:
  - ***Can you roll a dice for me?***
  - ***Wylosuj proszę liczbę do 22***
  - ***Give me random number smaller than 1000***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_3.png)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_4.png)
 
3. Telling a joke
 - you can use a variety of questions, like:
  - ***Tell me a joke!***
  - ***Opowiedz mi kawał!***
  - ***I wanna hear a joke***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_5.png)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_6.png)

4. Asking for a picture of a cat (or just wanting to see some online cat photos)
 - uses [AWS Random Cat](http://aws.random.cat/) API to get new cat photos each time you trigger this intent
 - everyone who talks about cats on Discord server clearly wants to see cats
 - you can use a variety of questions, like:
  - ***Give me cats, mrrr...***
  - ***Kotki!!!***
  - ***Can you supply me with the newest picture of a cat? Pretty please?***
  - ***Zapodaj zdjęcie kota, nie bądź sztywny***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_7.png)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_8.png)
 
5. Repeating a message
 - meant to be triggered, when the user forgot, what the bot said last time
 - can be used to trigger even more cat photos
 - you can use a variety of questions, like:
  - ***Can you repeat?***
  - ***Again, please?***
  - ***Czy możesz powtórzyć?***
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_9.png)
 - ![](https://github.com/GabenRulez/PSI_DiscordBot/readMePictures/screenshot_10.png)
