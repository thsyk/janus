import random
import json
import click
from pathlib import Path


@click.command()
@click.option('-s', '--short', is_flag=True, default=False, help='Generate shorter usernames')
@click.option('-l', '--long', is_flag=True, default=False, help='Generate longer usernames')
@click.option('-c', '--chars', default=25, type=int, help='Define max. character length of username (Default: 25)')
@click.option('-n', '--number', default=10, type=int, help='Define the number of generated usernames (Default: 10)')
@click.option('--low', is_flag=True, default=False, help='Print usernames in lowercase')
@click.option('--up', is_flag=True, default=False, help='Print usernames in UPPERCASE')
@click.option('--mix', is_flag=True, default=False, help='Print usernames MiXeD')
def roll_the_dice(short, long, chars, number, low, up, mix):
    """Generate random usernames with JANUS 😶‍🌫️"""
    # Fetch database
    database = open_database()
    # Assemble deck and text sources
    deck = list(database.keys())
    length = random.choice([2, 3, 4])
    # Define number of usernames to create
    usernames = []
    usernames_count=number
    for _x in range(0, usernames_count):
        length = random.choice([2, 3]) if short else random.choice([2, 3, 4])
        length = random.choice([4, 5]) if long else random.choice([2, 3, 4])
        depot = []
        while length > 0:
            dice = random.choice(deck)
            result = random.choice(database[dice]).capitalize()
            depot.append(result)
            length -= 1
        # Start mixing the generated parts of the username
        username = shake_mixer(depot, low, up, mix)
        # Cut the mixed username in an appetizing length
        cut = 15 if short else chars
        dice_cut = random.randint(6, cut)
        if len(username) > dice_cut and username[:dice_cut].endswith(('_', '-', '.')):
            dice_cut -= 1
            username = username[0:dice_cut]  
        else:
            username = username[0:dice_cut]
        usernames.append(username)
    # Send generated usernames to print
    print_output(usernames)

def shake_mixer(depot, low, up, mix):
    # Defines the character with which the parts of the username are joined
    dice_join = random.choice(['', '.', '-', '_'])
    # Defines the style of the username (lowercase, uppercase etc.)
    if low:
        dice_style = 'lower'
    elif up:
        dice_style = 'upper'
    elif mix:
        dice_style = 'mix'
    else:
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
