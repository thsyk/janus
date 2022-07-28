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
@click.option('--cap', is_flag=True, default=False, help='Print usernames Capitalized')
@click.option('--mix', is_flag=True, default=False, help='Print usernames MiXeD')
def roll_the_dice(short, long, chars, number, low, up, cap, mix):
    """Generate random usernames with JANUS 😶‍🌫️"""
    # Fetch database
    database = open_database()
    # Assemble deck and text sources
    deck = list(database.keys())
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
        dice_join = random.choice(['', '.', '-', '_'])
        if low: 
            username = style_low(depot, dice_join)
        elif up:
            username = style_up(depot, dice_join)
        elif mix:
            username = style_mixed(depot, dice_join)
        elif cap:
            username = style_cap(depot, dice_join)
        else:
            username = random.choice([style_low(depot, dice_join), style_up(depot, dice_join), 
            style_mixed(depot, dice_join), style_cap(depot, dice_join)])
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

def style_low(depot, dice_join):
    username = dice_join.join(random.sample(depot, len(depot))).lower()
    return username

def style_up(depot, dice_join):
    username = dice_join.join(random.sample(depot, len(depot))).upper()
    return username

def style_cap(depot, dice_join):
    username = dice_join.join(random.sample(depot, len(depot)))
    return username

def style_mixed(depot, dice_join):
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
