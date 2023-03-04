import discord
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello, world!')

@bot.command(name='ping')
async def ping(ctx):
    latency = bot.latency * 1000  # convert to milliseconds
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')

@bot.command(name='load')
async def load_commands(ctx, filename):
    with open(filename, 'r') as f:
        commands = f.readlines()

    for command in commands:
        command = command.strip()

        # Only add the command if it's not already registered
        if command not in bot.commands:
            bot.command()(lambda _: ctx.send(command), name=command)

    await ctx.send(f'Loaded {len(commands)} commands from {filename}')

@bot.command(name='weather')
async def weather(ctx, location):
    url = f'https://wttr.in/{location}?format=%C+%t'
    response = requests.get(url)

    if response.status_code == 200:
        weather = response.text.strip()
        await ctx.send(f'The weather in {location} is: {weather}')
    else:
        await ctx.send(f'Error getting weather data for {location}')

bot.run('your_bot_token_here')


# Notes/Explaination 
# Custom Commands Notes
# This new command is named `load` and takes a single argument: the name of a text file containing a list of custom commands, one per line. When it receives a `load` command, the bot will read the file and create new commands for each line that isn't already registered. Each new command will simply send a message back to the user with the contents of the line.
# To use this feature, create a text file containing the custom commands you want to load (e.g., `custom_commands.txt`). 
#
# Each command should be on a separate line. For example:
#
# !greet
# !help
# !stats
#
# Then, send the `load` command to the bot with the filename as an argument:
#
# !load custom_commands.txt
# The bot will then load each command from the file and respond with a message indicating how many commands were loaded. You can now use the new commands just like the built-in commands, by sending messages starting with the command prefix (! in this case) followed by the command name (e.g., `!greet`, `!help`, `!stats`).
# 
# Weather Command Notes
# This command is named `weather` and takes a single argument: the name of a location to get the weather for. When it receives a weather command, the bot will make a request to the wttr.in API (https://wttr.in/) to get the current weather for the specified location. It will then send a message back to the user with the weather information.
# To use this feature, simply send a message to the bot starting with the command prefix (`!` in this case) followed by the command name (`weather`) and the location you want to get the weather for. For example:
# !weather Nashville, TN
# The bot will then make a request to the wttr.in API for the weather in San Francisco and respond with a message indicating the weather conditions. Note that the location argument can be any string that wttr.in understands as a location (e.g., a city name, a zip code, etc.). You can find more information on the wttr.in API documentation page: https://github.com/chubin/wttr.in#one-liner-weather