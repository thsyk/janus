import random
import json
import click
from pathlib import Path


@click.command()
@click.option('-l', '--long', is_flag=True, default=False, help='Generate longer usernames')
@click.option('-n', '--number', default=10, type=int, help='Define the number of generated usernames (Default: 10)')
@click.option('--style', default='', help="Choose style of username: 'low' = lowercase, 'up' = UPPERCASE, 'mix' = MiXeD, 'cap' = In Capitals")
def roll_the_dice(long, number, style):
    """Generate random usernames with JANUS 😶‍🌫️"""
    # Fetch database
    database = open_database()
    # Assemble deck and text sources
    deck = list(database.keys())
    # Define number of usernames to create
    usernames = []
    usernames_count=number
    for _x in range(0, usernames_count):
        length = 3 if long else 2
        depot = []
        while length > 0:
            dice = random.choice(deck)
            result = random.choice(database[dice]).capitalize()
            depot.append(result)
            length -= 1
        if random.choice([1, 2, 3, 4]) == 3:  
            depot[-1] = f"{depot[-1] + str(random.randint(1, 99))}"
        # Start mixing the generated parts of the username
        dice_join = '-' if style else random.choice(['-', ''])
        username = start_mixing(depot, dice_join, style)
        usernames.append(username)
    # Send generated usernames to print
    print_output(usernames)

def start_mixing(depot, dice_join, style):
    if dice_join == '':
        username = dice_join.join(random.sample(depot, len(depot)))
    else:
        if style == 'low':
            username = dice_join.join(random.sample(depot, len(depot))).lower()
        elif style == 'up':
            username = dice_join.join(random.sample(depot, len(depot))).upper()
        elif style == 'cap':
            username = dice_join.join(random.sample(depot, len(depot)))
        elif style == 'mix':
            username = dice_join.join(random.sample(depot, len(depot)))
            username_upper = [username[i] for i in range(0, len(username), 2)]
            username_lower = [username[i] for i in range(1, len(username), 2)]
            username_updated = []
            for x, y in zip(username_upper, username_lower):
                username_updated.append(x.upper())
                username_updated.append(y)
            username = ''.join(username_updated)
        else:
            username = start_mixing(depot, dice_join, style='low')
    return username

def open_database():
    db = Path('database.json')
    with open(db, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def print_output(usernames):
    for name in usernames:
        print(name)

if __name__ == '__main__':
    roll_the_dice()
