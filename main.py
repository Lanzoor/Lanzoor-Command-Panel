import random, time, timeit, sources, base64, re
from datetime import datetime
from colorama import Fore, Style

points = 0
multiplier = 1
count = 0
mulmul = 1
sources.print_with_animation("Initializing Program...\n")
time.sleep(0.5)
sources.print_with_animation("Executing LCP...")
time.sleep(0.5)
sources.print_with_animation(sources.welcome)
while True:
    user_input = str(input(">>> "))
    formatted_user_input = user_input.replace(" ", "").lower()
    current_time = datetime.now()
    formatted_date = f"{current_time.strftime("%B")} {str(sources.ordinal(int(current_time.strftime("%d"))))}{current_time.strftime(", %Y")}"
    formatted_time = current_time.strftime("%I:%M:%S %p")
    
    match formatted_user_input:
        case "?exit":
            yes_or_no = sources.input_with_animation(sources.exit_confirmation).lower()
            if yes_or_no == "y":
                sources.print_with_animation("Alright, See you next time.")
                time.sleep(0.5)
                break
        case "?help":
            sources.print_with_animation(sources.help)
        case ("?rps" | "?rockpaperscissors"):
            points = sources.rps(points, multiplier, mulmul)
        case ("?golt" | "?greaterorlowerthan"):
            points = sources.golt(points, multiplier, mulmul)
        case "?datetime":
            sources.print_with_animation(f"Your date and time are {formatted_time} {formatted_date}!\nIsLeapYear: {sources.is_leap_year()}\nYour local timezone: {datetime.now().astimezone().strftime("%Z")}")
        case "?ping":
            latency = timeit.timeit(r"import sources;sources.printAnimation('Pong!')", number = 1)
            sources.print_with_animation(f"Latency of the command input was {latency * 1000}ms!")
        case "?randint":
            while True:
                maximum = sources.try_integer_input("Choose your minimum number!\n  >>> ")
                minimum = sources.try_integer_input("Choose your maximum number!\n  >>> ")
                if maximum < minimum: break 
                else: sources.print_with_animation("The maximum number must be bigger than the minimum number, try again.")
            sources.print_with_animation(f"My random choice between {maximum} and {minimum} is {random.randint(maximum, minimum)}!")
        case "?randkey":
            length = sources.try_integer_input("Enter the length of a key generation!\n  >>> ")
            result = ""
            char = list("abcdef1234567890")
            for index in range(0, length):
                if index % 4 == 0 and index != 0:
                    result += "-"
                result += random.choice(char)
            sources.print_with_animation(f"Your random key that has {length} letters is {result}!")
        case "?flipacoin":
            sources.print_with_animation(f"I flipped a coin... it landed on {random.choice(["Heads", "Tails"])}!")
        case "?shop":
            sources.print_with_animation(sources.welcome_to_the_shop)
            while True:
                multiplier_cost = (multiplier * (multiplier + 55) + multiplier * (multiplier + 2)) if mulmul < 1 else (multiplier * (multiplier + 70) + multiplier * (multiplier + 4))
                mulmul_cost = (mulmul * (mulmul + 200) * (mulmul + 4)) if mulmul < 1 else (mulmul * (mulmul + 425) * (mulmul + 5))
                prices = f'''
1. Add 1 to the point multiplier (Cost: {multiplier_cost})
2. Add 5 to the multiplier multiplier (Cost: {mulmul_cost})
You currently have {points} points.
'''
                sources.print_with_animation(prices)
                shop_item_input = sources.input_with_animation("Enter an item value or exit!\n  >>> ")
                if shop_item_input == "exit": 
                    break
                try:
                    shop_item_input = int(shop_item_input)
                except:
                    sources.print_with_animation("That is not a valid input. Try again!\n  >>> ")
                    continue
                if shop_item_input == 1 and points >= multiplier_cost:
                    sources.print_with_animation("You bought the first upgrade! Now, all of your point gains are multiplied by x2 (additive).")
                    points -= multiplier_cost
                    multiplier += 1
                elif shop_item_input == 1 and points < multiplier_cost:
                    sources.print_with_animation("You can't afford this item.")
                
                if shop_item_input == 2 and points >= mulmul_cost:
                    sources.print_with_animation("You bought the second upgrade! Now, all of your multiplier effects are multiplied by x5 (additive).")
                    points -= mulmul_cost
                    mulmul += 5
                elif shop_item_input == 2 and points < mulmul_cost:
                    sources.print_with_animation("You can't afford this item.")
        case "?export":
            before_encoding = f"po:{points},mul:{multiplier},super:{mulmul},cou:{count}"
            after_encoding = base64.b64encode(before_encoding.encode()).decode()
            sources.print_with_animation("Your current save is", 0.001, False)
            sources.print_with_animation(Fore.CYAN + f" {after_encoding}")
            print(Style.RESET_ALL + '', end="")
            sources.print_with_animation("You can import your current data by using the ?import command.\nMake sure to input this exact save data!")
        case "?import":
            while True:
                before_decoding = sources.input_with_animation("Enter a valid save format!\n  >>> ").replace(" ", "")
                if before_decoding == "exit": break
                try:
                    after_decoding = base64.b64decode(before_decoding.encode()).decode()
                except:
                    sources.print_with_animation("That is not a valid save format. Enter a valid save format using the ?export command.")
                    continue
                valid_save_data = re.compile(r"^po:(\d+),mul:(\d+),super:(\d+),cou:(\d+)$")
                is_matched = valid_save_data.match(after_decoding)
                if is_matched:
                    break
                else:
                    sources.print_with_animation("That is not a valid save format. Enter a valid save format using the ?export command.")
                    continue
            if before_decoding != "exit":
                sources.print_with_animation(Fore.RED + "LOADING SAVE DATA...")
                time.sleep(1)
                after_decoding = after_decoding.replace("po:", "").replace(",mul:", " ").replace(",super:", " ").replace(",cou:", " ").split(" ")
                before_points, before_multiplier, before_mulmul, before_count = int(after_decoding[0]), int(after_decoding[1]), int(after_decoding[2]), int(after_decoding[3])
                if any([before_points < 0, before_multiplier < 0, before_mulmul < 0, before_count < 0]):
                    sources.print_with_animation("Seems like your save data is corrupted, \nincluding negative sources. Please try again with a valid save.")
                    print(Style.RESET_ALL + '', end="")
                else:
                    print(Style.RESET_ALL + '', end="")
                    points, multiplier, mulmul, count = before_points, before_multiplier, before_mulmul, before_count
                    sources.print_with_animation(Fore.CYAN + f"Save data succesfully loaded with {points} points, {multiplier} multiplier count, \n{mulmul} multiplier multiplier count, and {count} command input count!")
                    print(Style.RESET_ALL + '', end="")
        case ("?stats" | "?stat"):
            print(f"You currently have {points} points, {multiplier} multiplier count, and {mulmul} multiplier multiplier count. You used {count} commands total excluding non-command inputs.")
        case (""):
            continue
        case _:
            if "?" in formatted_user_input: 
                sources.print_with_animation(f"\"{user_input}\" is not a valid command, try again!")
            elif "?" not in formatted_user_input and formatted_user_input in sources.valid_commands:
                sources.print_with_animation("That is still a valid command, but you inputted them not as a command.\nPerhaps you forgot the question mark?")
            continue
    count += 1
