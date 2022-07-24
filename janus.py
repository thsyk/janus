import random
import json
from pathlib import Path


def open_database():
    db = Path('database.json')
    with open(db, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data

def roll_the_dice(database):
    deck = list(database.keys())
    length = random.choice([2, 3, 4])
    # Define number of usernames to create
    usernames = []
    usernames_count = 10
    for _x in range(1, usernames_count):
        length = random.choice([2, 3, 4])
        depot = []
        while length > 0:
            dice = random.choice(deck)
            result = random.choice(database[dice]).capitalize()
            depot.append(result)
            length -= 1
        # Start mixing the generated parts of the username
        username = shake_mixer(depot)
        # Cut the mixed username in an appetizing length // Default: 25 chars
        dice_cut = random.randint(6, 25)
        if len(username) > dice_cut and username[:dice_cut].endswith(('_', '-', '.')):
            dice_cut -= 1
            username = username[0:dice_cut]  
        else:
            username = username[0:dice_cut]
        usernames.append(username)
    # Send generated usernames to print
    print_output(usernames)

def shake_mixer(depot):
    # Defines the char with which the parts of the username are joined
    dice_join = random.choice(['', '.', '-', '_'])
    # Defines the style of the username (lowercase, uppercase etc.)
    dice_style = random.choice(['lower', 'cap', 'upper', 'mix'])
    if dice_style == 'lower':
        username = dice_join.join(random.sample(depot, len(depot))).lower()
    elif dice_style == 'cap':
        username = dice_join.join(random.sample(depot, len(depot)))
    elif dice_style == 'upper':
        username = dice_join.join(random.sample(depot, len(depot))).upper()
    elif dice_style == 'mix':
        username = dice_join.join(random.sample(depot, len(depot)))
        username_upper = [username[i] for i in range(0, len(username), 2)]
        username_lower = [username[i] for i in range(1, len(username), 2)]
        username_updated = []
        for x, y in zip(username_upper, username_lower):
            username_updated.append(x.upper())
            username_updated.append(y)
        username = ''.join(username_updated)
    return username

def print_output(usernames):
    for name in usernames:
        print(name)


database = open_database()
usernames = roll_the_dice(database)
