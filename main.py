# Imports that are used in this script

import random, time, timeit
from datetime import datetime
from functions import *

# Declaration of basic variables that contains the help for LCP

LCPCurrentVersion = "Beta 1.3"

LCPStartHelp = f'''Hello User! Welcome to the Lanzoor Command Panel (Version: {LCPCurrentVersion})! 
Type ?help to get help about the commands that you can use, or type ?exit to quit LCP.'''

LCPHelp = '''Welcome to LCP command help! Here are the list of all commands that you can use.
?help: Open this help message.
?exit: Exit LCP.
?info: Open the information of LCP.
?updatelog: Open the update log.
?rps or ?rockpaperscissors: Play the Rock Paper Scissors game.
?golt or ?greaterorlowerthan: Play the "Greater or Lower than" game.
?date: Get the current date based on your local timezone.
?time: Get the current time based on your local timezone.
?datetime: Get the current date and time based on your local timezone.
?ping: Pong!
?randint: Pick a random value between the maximum and minimum value that you input.'''

LCPInfo = f'''Welcome to LCP information page! Here are some informations about LCP.
Author: Lanzoor
Programming language: Python
Version (Current build): {LCPCurrentVersion}
First build: Alpha v1.0 in GMT+9 2024-04-06 3PM'''

LCPUpdateLog = f'''Welcome to the LCP update log page! Here are the log of updates that were
implemented in the LCP build. Also very simple fixes can be not listed on here.
Current version: {LCPCurrentVersion}
Alpha v1.0: The first build with basic commands like ?exit, ?help, and ?updatelog.
Alpha v1.1: The second build that added the ?rps command.
Alpha v1.2: Added the ?golt command.
Alpha v1.3: Added date and time commands.
Alpha v1.8: Added the ?randint command.
Beta v1.0: The first beta build with a more detailed executing indicator,
?ping function, and handmade ordinal function.
Beta v1.1: The second beta build that changed a lot about the code.'''

print("Initializing Program...")
time.sleep(0.25)
print("Executing Python file \"main.py\"...")
time.sleep(0.25)
print("Executing LCP...")
time.sleep(0.25)
print(LCPStartHelp)

# Command Inputs

while True:
    LCPInput = input(">>> ").replace(" ", "").lower()
    current_time = datetime.now()
    formatted_date = f"{current_time.strftime("%B")} {str(ordinal(int(current_time.strftime("%d"))))}{current_time.strftime(", %Y")}"
    formatted_time = current_time.strftime("%I:%M:%S %p")
    match LCPInput:
        case "?exit":
            print("Exiting LCP...")
            time.sleep(0.5)
            print("You exitted the LCP!")
            break
        case "?help":
            print(LCPHelp)
        case "?info":
            print(LCPInfo)
        case "?updatelog":
            print(LCPUpdateLog)
        case ("?rps" | "?rockpaperscissors"):
            rps()
        case ("?golt" | "?greaterorlowerthan"):
            golt()
        case "?date":
            print(f"Your current date is {formatted_date}!")
        case "?time":
            print(f"Your current time is {formatted_time}!")
        case "?datetime":
            print(f"Your date and time are {formatted_time} {formatted_date}!")
        case "?ping":
            latency = timeit.timeit("print('Pong!')", number = 1)
            print(f"Average latency of 100 command inputs were {latency}s!")
        case "?randint":
            x = tryIntInput("Choose your minimum number!\n    >>> ")
            y = tryIntInput("Choose your maximum number!\n    >>> ")
            print(f"My random choice between {x} and {y} is {random.randint(x, y)}!")
        case _:
            print(f"\"{LCPInput}\" is not a valid command, try something else!")
            y = tryIntInput("Choose your maximum number!\n    >>> ")
            print(f"My random choice between {x} and {y} is {random.randint(x, y)}!")
