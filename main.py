# Imports that are used in this script

import random, time, timeit
from datetime import datetime
from functions import *

# Declaration of basic variables that contains the help for LCP

LCPCurrentVersion = "Beta 1.0"

LCPStartHelp = f'''Hello User! Welcome to the Lanzoor Command Panel (Version: {LCPCurrentVersion})! 
Type ?help to get help about the commands that you can use, or type ?exit to quit LCP.'''

LCPHelp = f'''Welcome to LCP command help! Here are the list of all commands that you can use.
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
First build: Alpha v1.0.0 in GMT+9 2024-04-06 3PM
Last updated: Now'''

LCPUpdateLog = f'''Welcome to the LCP update log page! Here are the log of updates that were
implemented in the LCP build. Also very simple fixes can be not listed on here.
Current version: {LCPCurrentVersion}
Alpha v1.0.0: The first build with basic commands like ?exit, ?help, and ?updatelog.
Alpha v1.0.1: The second build that added the ?rps command.
Alpha v1.0.2: Added the ?golt command.
Alpha v1.0.3: Added date and time commands.
Alpha v1.0.6: Little Changes, a combined version of Alpha v1.0.4 and v1.0.5.
Alpha v1.0.8: Added the ?randint command, a combined version of Alpha v1.0.7.
Beta v1.0: The first beta build with a more detailed executing indicator,
?ping function, and handmade ordinal function that is combined with Alpha v1.0.9.'''

print("Executing LCP...\n")
time.sleep(0.5)
print(LCPStartHelp)

# Command Inputs

while True:
    LCPInput = input(">>> ").replace(" ", "").lower()
    current_time = datetime.now()
    formatted_date = f"{current_time.strftime("%B")} {str(ordinal(int(current_time.strftime("%d"))))}{current_time.strftime(", %Y")}"
    formatted_time = current_time.strftime("%I:%M:%S %p")
    if LCPInput == "?exit":
        print("Exiting LCP...")
        time.sleep(0.5)
        print("You exitted the LCP!")
        break
    elif LCPInput == "?help":
        print(LCPHelp)
    elif LCPInput == "?info":
        print(LCPInfo)
    elif LCPInput == "?updatelog":
        print(LCPUpdateLog)
    elif LCPInput in ("?rps", "?rockpaperscissors"):
        rps()
    elif LCPInput in ("?golt", "?greaterorlowerthan"):
        golt()
    elif LCPInput == "?date":
        print(f"Your current date is {formatted_date}!")
    elif LCPInput == "?time":
        print(f"Your current time is {formatted_time}!")
    elif LCPInput == "?datetime":
        print(f"Your date and time are {formatted_time} {formatted_date}!")
    elif LCPInput == "?ping":
        latency = timeit.timeit("print('Pong!')", number=1)
        print(f"Latency of the command input was {latency}s!")
    elif LCPInput == "?randint":
        x = tryIntInput("Choose your minimum number!\n>>> ")
        y = tryIntInput("Choose your maximum number!\n>>> ")
        print(f"My random choice between {x} and {y} is {random.randint(x, y)}!")
    else:
        print(f"\"{LCPInput}\" is not a valid command, try something else!")
    # FIXME: Fix this fucking if-elif-else statement because it's hard to read
