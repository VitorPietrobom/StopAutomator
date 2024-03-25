# Stop Automator

Made in Python using Selenium webdriver and the OpenAI API, Stop Automator is a project aimed at automating a popular game known as "Stop" using the power of AI.

## How it Works?

The program is divided into four different files:

- **StopAutomator.py**: This serves as the main file of the program, creating the GUI and coordinating the functionalities of the other files.
  
- **GameCreator.py**: Responsible for creating the game on the site [Stopots](https://stopots.com.br/), it allows for predefined categories that can be modified.
  
- **GameHacker.py**: Designed to read the letter assigned by the game and the order of the categories, this file calls the OpenAI API to generate answers and writes them in the correct order.
  
- **OpenAPIUsing.py**: This file handles the integration with the OpenAI API, making a call to retrieve the correct answers.

## Future Work

- Enhance the user interface to be more visually appealing and modern, while also providing additional customization options such as player name, categories, and game link.
  
- Implement a feature to input only a single category, offering more flexibility to users.
  
- Strengthen the category fetching mechanism to make it more robust and secure, addressing potential bugs within the program.
