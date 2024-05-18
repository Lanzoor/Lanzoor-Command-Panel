import random, time, timeit, functions, base64, re
from datetime import datetime

points = 0
multiplier = 1
currentver = "1.0.7"
help = '''
Welcome to LCP command help! Here are the list of all commands that you can use.
?help: Open this help message.
?exit: Exit LCP.
?info: Open the information of LCP.
?rps or ?rockpaperscissors: Play the Rock Paper Scissors game.
?golt or ?greaterorlowerthan: Play the "Greater or Lower than" game.
?date: Get the current date based on your local timezone.
?time: Get the current time based on your local timezone.
?datetime: Get the current date and time based on your local timezone.
?ping: Check the print latency...for some reason because Lanzoor thought that this was a funny idea-
?randint: Pick a random value between the maximum and minimum value that you input.
?randkey: Generate a random key based on the length.
?flipacoin: Flip a coin.
?points: Check how many points you currently have.
?shop: Open the shop.
?import: Import a save file.
?export: Export a save file.
'''

info = f'''
Welcome to LCP information page! Here are some informations about LCP.
Author: Lanzoor
Programming language: Python (3.12~)
Version (Current version): {currentver}
First version: Alpha v1.0 in GMT+9 2024-04-06 3PM
'''

functions.printAnimation("Initializing Program...\n")
time.sleep(0.5)
functions.printAnimation("Executing LCP...")
time.sleep(0.5)
functions.printAnimation(f'''Hello User! Welcome to the Lanzoor Command Panel (Version: {currentver})! 
Type ?help to get help about the commands that you can use, or type ?exit to exit LCP.''')

while True:
    multipliercost = multiplier * (multiplier + 90) + multiplier * (multiplier + 3)
    shopopen = f'''
Hello there! Welcome to the shop. In here you can spend points to get upgrades.
Type exit to exit the shop. Here is the list of items that you can buy. 
Type the corresponding number to buy the item!
'''
    shopafter = f'''
1. Multiply all point gains by x2 (Cost: {multipliercost})
You currently have {points} points.
'''
    userinput = str(input(">>> "))
    formatteduserinput = userinput.replace(" ", "").lower()
    ctime = datetime.now()
    formatteddate = f"{ctime.strftime("%B")} {str(functions.ordinal(int(ctime.strftime("%d"))))}{ctime.strftime(", %Y")}"
    formattedtime = ctime.strftime("%I:%M:%S %p")
    match formatteduserinput:
        case "?exit":
            yesorno = functions.inputAnimation("Are you sure you want to leave LCP?\nAll of your data will be lost. However, your save data can be imported and exported using the import and the export commands. (Input Y to leave.)\n  >>> ").lower()
            if yesorno == "y":
                functions.printAnimation("Alright. See you next time!")
                time.sleep(1)
                break
        case "?help":
            functions.printAnimation(help)
        case "?info":
            functions.printAnimation(info)
        case ("?rps" | "?rockpaperscissors"):
            points = functions.rps(points, multiplier)
        case ("?golt" | "?greaterorlowerthan"):
            points = functions.golt(points, multiplier)
        case "?date":
            functions.printAnimation(f"Your current date is {formatteddate}!\nIsLeapYear: {functions.isLeapYear()}\nYour local timezone: {datetime.now().astimezone().strftime("%Z")}")
        case "?time":
            functions.printAnimation(f"Your current time is {formattedtime}!")
        case "?datetime":
            functions.printAnimation(f"Your date and time are {formattedtime} {formatteddate}!\nIsLeapYear: {functions.isLeapYear()}\nYour local timezone: {datetime.now().astimezone().strftime("%Z")}")
        case "?ping":
            latency = timeit.timeit(r"functions.printAnimation('\nPong!')", number = 1)
            functions.printAnimation(f"Latency of the command input was {latency * 1000}ms!")
        case "?randint":
            while True:
                maximum = functions.tryIntInput("Choose your minimum number!\n  >>> ")
                minimum = functions.tryIntInput("Choose your maximum number!\n  >>> ")
                if maximum < minimum: break 
                else: functions.printAnimation("The maximum number must be bigger than the minimum number, try again.")
            functions.printAnimation(f"My random choice between {maximum} and {minimum} is {random.randint(maximum, minimum)}!")
        case "?randkey":
            length = functions.tryIntInput("Enter the length of a key generation!\n  >>> ")
            result = ""
            char = list("abcdef1234567890")
            for index in range(0, length):
                if index % 4 == 0 and index != 0:
                    result += "-"
                result += random.choice(char)
            functions.printAnimation(f"Your random key that has {length} letters is {result}!")
        case "?flipacoin":
            functions.printAnimation(f"I flipped a coin... it landed on {random.choice(["Heads", "Tails"])}!")
        case "?points":
            functions.printAnimation("It seems like you don't have any points. Play a game to get points!" if points == 0 else f"You currently have {points} points!")
        case "?multiplier":
            if multiplier == 1:
                functions.printAnimation("Your multiplier count is 1 (default). Play some games to get points, and buy the multiplier upgrade at the shop!")
            else:
                functions.printAnimation(f"All point gains are currently multiplied by x{multiplier}.")
        case "?shop":
            functions.printAnimation(shopopen)
            while True:
                functions.printAnimation(shopafter)
                shopInput = functions.inputAnimation("Enter an item value or exit!\n  >>> ")
                if shopInput == "exit": 
                    break
                try:
                    shopInput = int(shopInput)
                except:
                    functions.printAnimation("That is not a valid input. Try again!\n  >>> ")
                    continue
                if shopInput == 1 and points >= multipliercost:
                    functions.printAnimation("You bought the first upgrade! Now, all of your point gains are multiplied by x2.")
                    points -= multipliercost
                    multiplier *= 2
                elif shopInput == 1 and points < multipliercost:
                    functions.printAnimation("You can't afford this item.")
        case "?export":
            beforeencoding = f"mul:{multiplier},po:{points}"
            afterencoding = base64.b64encode(beforeencoding.encode()).decode()
            functions.printAnimation(f"Your current save is {afterencoding}\nyou can import your current data by using the ?import command!\nMAKE SURE TO INPUT THE EXACT SAVE FORMAT.")
        case "?import":
            while True:
                beforedecoding = functions.inputAnimation("Enter a valid save format!\n  >>> ")
                if beforedecoding == "exit": break
                try:
                    afterdecoding = base64.b64decode(beforedecoding.encode()).decode()
                except:
                    functions.printAnimation("That is not a valid save format. Enter a valid save format using the ?export command.")
                    continue
                pattern = re.compile(r"^mul:(\d+),po:(\d+)$")
                isMatched = pattern.match(afterdecoding)
                if isMatched:
                    break
                else:
                    functions.printAnimation("Not a valid format! Try again.")
                    continue
            if beforedecoding != "exit":
                functions.printAnimation("LOADING SAVE DATA...")
                time.sleep(1) # To make it look like it is actually going through millions of iterations
                afterdecoding = afterdecoding.replace("mul:", "").replace(",po:", " ").split(" ")
                multiplier, points = int(afterdecoding[0]), int(afterdecoding[1])
                functions.printAnimation(f"Save data succesfully loaded with {points} points and {multiplier} multiplier count.")
        case (""):
            pass
        case _:
            if "?" in formatteduserinput: 
                functions.printAnimation(f"\"{userinput}\" is not a valid command, try again!")
# NOTE: The save system is still in beta. Unexpected errors might occur.
