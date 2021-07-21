# Stop Automator

Made in python using Selenium webdriver

## How it Works?

The program is now fragmented in 3 different files:

GameCreator.py - This one effectively creates the game on the site (https://stopots.com.br/), going with some pre-defined categories

Google.py - The existence of this program is probably temporary as I want to make some kind of repository for this, but what this one does is pretty straight foward, it takes a list of Strings and a letter and look for it in Google as: "List[i] with the letter Letter", I still have to figure out how to get the awnsers from it

GameHacker.py - This one is made to read the letter defined by the game and the order of the categories, them it calls the Google.py program and write the awnsers in the correct order


## Problems for now

The program is still too instable as of time, and the reason for that is, I used the library Time to set the entire thing, so if someone delay some step too much during the game, the program might break

I don't know yet if I´ll continue with the Google.py thing, because I want to implement a database to the program, but I don't really know how to do it yet

In case I implement a Database, I would want some way to construct it faster, because going from letter to letter in each cattegory would take a lot of time
