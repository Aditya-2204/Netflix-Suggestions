'''
Aditya Chakraborty
9/8/23
Netflix Suggestions
'''
import random
sci_fi = ["Cloudy With a Chance of Meatballs", "Zathura", "Megamind"]

mystery = ["Scooby-Doo", "Monster House", "Nancy Drew"]
sci_fi_and_mystery = ["Tomorrow Land", "House with a Clock in its walls", "Race to witch mountain"]
adventure = ["Swiss Family Robinson", "The Goonies", "Princess Bride"]

random_choicescifi = random.choice(sci_fi)
random_choicemystery = random.choice(mystery)
inp = input(f"Welcome to the Netflix Suggestions.\nDo you like {random_choicescifi} (y/n): ")
if inp == "y":
    inp2 = input(f"\nDo you like {random.choice(mystery)} (y/n): ")
    if inp2 == "y":
        print(f"You should watch {random.choice(sci_fi_and_mystery)}")
    elif inp2 == "n":
        sci_fi.remove(random_choicescifi)
        print(f"You should watch {random.choice(sci_fi)}")
elif inp == "n":
    inp2 = input(f"\nDo you like {random.choice(mystery)} (y/n): ")
    if inp2 == "y":
        mystery.remove(random_choicemystery)
        print(f"You should watch {random.choice(mystery)}")
    elif inp2 == "n":
        print(f"You should watch {random.choice(adventure)}")