# python-discord-bot
A very simple discord bot written in python 3.10

## To Install and Use this bot, you will need to follow these steps:

1.) Install Python 3.10 or later on your computer if you haven't already done so. You can download the latest version of Python from the official website: https://www.python.org/downloads/ <br>
2.) Create a new Discord application and bot account by following the instructions in the Discord developer portal: https://discord.com/developers/docs/intro <br>
3.) Once you have created your bot account, copy the bot token.<br>
4.) Create a new Python file in your preferred code editor, and paste the code I provided into the file.<br>
5.) Replace the your_bot_token_here placeholder with the bot token you copied in step 3.<br>
6.) Save the file with a .py extension (e.g., my_bot.py).<br>
7.) Open a terminal or command prompt window and navigate to the directory where you saved the file.<br>
8.) Install the required packages by running the following command:<br>
`pip install discord requests`
9.) Start the bot by running the following command:<br>
`python my_bot.py`<br><br>

Your bot should now be online and ready to respond to commands in any Discord servers it has been invited to! You can test it by sending a message starting with the command prefix (! in this case) followed by one of the command names (e.g., !hello, !ping, !weather).
<br><br>
## Notes / Features / Commands
<br>
Custom Commands Notes<br><br>

This new command is named `load` and takes a single argument: the name of a text file containing a list of custom commands, one per line. When it receives a `load` command, the bot will read the file and create new commands for each line that isn't already registered. Each new command will simply send a message back to the user with the contents of the line.<br>

To use this feature, create a text file containing the custom commands you want to load (e.g., `custom_commands.txt`). <br>

Each command should be on a separate line. For example:<br>

!greet<br>
!help<br>
!stats<br>

Then, send the `load` command to the bot with the filename as an argument:<br>

!load custom_commands.txt<br>

You can easily create your own custom commands using text files.<br>

The bot will then load each command from the file and respond with a message indicating how many commands were loaded. You can now use the new commands just like the built-in commands, by sending messages starting with the command prefix (! in this case) followed by the command name (e.g., `!greet`, `!help`, `!stats`).<br>

Weather Command Notes<br>

This command is named `weather` and takes a single argument: the name of a location to get the weather for. When it receives a weather command, the bot will make a request to the wttr.in API (https://wttr.in/) to get the current weather for the specified location. It will then send a message back to the user with the weather information. <br>

To use this feature, simply send a message to the bot starting with the command prefix (`!` in this case) followed by the command name (`weather`) and the location you want to get the weather for. For example:<br>

!weather Nashville, TN<br>

The bot will then make a request to the wttr.in API for the weather in San Francisco and respond with a message indicating the weather conditions. Note that the location argument can be any string that wttr.in understands as a location (e.g., a city name, a zip code, etc.). You can find more information on the wttr.in API documentation page: https://github.com/chubin/wttr.in#one-liner-weather



**This Discord Bot was made for Educational Purposes as an Example**
