import random, time, timeit, functions, base64, re
from datetime import datetime

points = 0
multiplier = 1
count = 0
multipliermultiplier = 1
currentver = "1.1.2"
help = f'''
Welcome to LCP help!
Here is the information of LCP.
Author: Lanzoor
Programming language: Python (3.12~)
Version (Current version): {currentver}
First version: Alpha v1.0 in GMT+9 2024-04-06 3PM 
Here are the list of all commands that you can use.

Here is the list of all commands that you can use.
?help: Open this help message.
?exit: Exit LCP.
?rps or ?rockpaperscissors: Play the Rock Paper Scissors game.
?golt or ?greaterorlowerthan: Play the "Greater or Lower than" game.
?datetime: Get the current date and time based on your local timezone.
?ping: Check the print latency...for some reason because Lanzoor thought that this was a funny idea-
?randint: Pick a random value between the maximum and minimum value that you input.
?randkey: Generate a random key based on the length.
?stats: Show the user stats.
?flipacoin: Flip a coin.
?shop: Open the shop.
?import: Import a save file.
?export: Export a save file.
'''
functions.printAnimation("Initializing Program...\n")
time.sleep(0.5)
functions.printAnimation("Executing LCP...")
time.sleep(0.5)
functions.printAnimation(f'''Hello User! Welcome to the Lanzoor Command Panel (Version: {currentver})! 
Type ?help to get help about the commands that you can use, or type ?exit to exit LCP.''')
while True:
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
        case ("?rps" | "?rockpaperscissors"):
            points = functions.rps(points, multiplier, multipliermultiplier)
        case ("?golt" | "?greaterorlowerthan"):
            points = functions.golt(points, multiplier, multipliermultiplier)
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
        case "?shop":
            functions.printAnimation('''
Hello there! Welcome to the shop. In here you can spend points to get upgrades.
Type exit to exit the shop. Here is the list of items that you can buy. 
Type the corresponding number to buy the item!
''')
            while True:
                multipliercost = (multiplier * (multiplier + 55) + multiplier * (multiplier + 2)) if multipliermultiplier < 1 else (multiplier * (multiplier + 70) + multiplier * (multiplier + 4))
                multipliermultipliercost = (multipliermultiplier * (multipliermultiplier + 200) * (multipliermultiplier + 4)) if multipliermultiplier < 1 else (multipliermultiplier * (multipliermultiplier + 425) * (multipliermultiplier + 5))
                shopafter = f'''
1. Add 1 to the point multiplier (Cost: {multipliercost})
2. Add 5 to the multiplier multiplier (Cost: {multipliermultipliercost})
You currently have {points} points.
'''
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
                    functions.printAnimation("You bought the first upgrade! Now, all of your point gains are multiplied by x2 (additive).")
                    points -= multipliercost
                    multiplier += 1
                elif shopInput == 1 and points < multipliercost:
                    functions.printAnimation("You can't afford this item.")
                
                if shopInput == 2 and points >= multipliermultipliercost:
                    functions.printAnimation("You bought the second upgrade! Now, all of your multiplier effects are multiplied by x5 (additive).")
                    points -= multipliermultipliercost
                    multipliermultiplier += 5
                elif shopInput == 2 and points < multipliermultipliercost:
                    functions.printAnimation("You can't afford this item.")
        case "?export":
            beforeencoding = f"po:{points},mul:{multiplier},super:{multipliermultiplier},cou:{count}"
            afterencoding = base64.b64encode(beforeencoding.encode()).decode()
            functions.printAnimation(f"Your current save is {afterencoding}\nyou can import your current data by using the ?import command!\nMAKE SURE TO INPUT THE EXACT SAVE FORMAT.")
        case "?import":
            while True:
                beforedecoding = functions.inputAnimation("Enter a valid save format!\n  >>> ").replace(" ", "")
                if beforedecoding == "exit": break
                try:
                    afterdecoding = base64.b64decode(beforedecoding.encode()).decode()
                except:
                    functions.printAnimation("That is not a valid save format. Enter a valid save format using the ?export command.")
                    continue
                pattern = re.compile(r"^po:(\d+),mul:(\d+),super:(\d+),cou:(\d+)$")
                isMatched = pattern.match(afterdecoding)
                if isMatched:
                    break
                else:
                    functions.printAnimation("Not a valid format! Try again.")
                    continue
            if beforedecoding != "exit":
                functions.printAnimation("LOADING SAVE DATA...")
                time.sleep(1) # To make it look like it is actually going through millions of iterations
                afterdecoding = afterdecoding.replace("po:", "").replace(",mul:", " ").replace(",super:", " ").replace(",cou:", " ").split(" ")
                points, multiplier, multipliermultiplier, count = int(afterdecoding[0]), int(afterdecoding[1]), int(afterdecoding[2]), int(afterdecoding[3])
                functions.printAnimation(f"Save data succesfully loaded with {points} points, {multiplier} multiplier count, {multipliermultiplier} multiplier multiplier count, and {count} command input count.")
        case "?stats":
            print(f"You currently have {points} points, {multiplier} multiplier count, and {multipliermultiplier} multiplier multiplier count. You used {count} commands total excluding non-command inputs.")
        case (""):
            continue
        case _:
            if "?" in formatteduserinput: 
                functions.printAnimation(f"\"{userinput}\" is not a valid command, try again!")
            continue
    count += 1
# NOTE: The save system is still in beta. Unexpected errors might occur.
