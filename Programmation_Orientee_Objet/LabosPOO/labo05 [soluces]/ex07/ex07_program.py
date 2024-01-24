import os
import re
from ex06_compressions import LZW
from ex04_program import change_directory


def compress(source, destination):
    lzw = LZW()
    with open(source) as src:
        with open(destination, 'wb') as dest:
            lzw.compress(source=src, destination=dest)


def decompress(source, destination):
    lzw = LZW()
    with open(source, 'rb') as src:
        with open(destination, 'w') as dest:
            lzw.decompress(source=src, destination=dest)


ACTIONS = {
    'c': {
        'Type':'compression',
        'Src':'txt',
        'Ext':'.*\.txt',
        'Dest':'bin',
        'Regex':'.*\.bin',
        'Fct':compress
    },
    'd': {
        'Type':'decompression',
        'Src':'bin',
        'Ext':'.*\.bin',
        'Dest':'txt',
        'Regex':'.*\.txt',
        'Fct':decompress
    }
}


def ask_source(choice):
    valid = False
    while not valid:
        source = input(f'Veuillez entrer un fichier source au format {ACTIONS[choice]["Src"]}: ')
        valid = re.match(ACTIONS[choice]["Ext"], source)
    return source


def ask_destination(choice):
    valid = False
    while not valid:
        destination = input(f'Veuillez entrer un fichier destination au format {ACTIONS[choice]["Dest"]}: ')
        valid = re.match(ACTIONS[choice]["Regex"], destination)
    return destination


def choose_action():
    valid = False
    while not valid:
        choice = input('Voulez vous utiliser la [c]ompression ou la [d]écompression ? ')
        if choice.lower() == 'c' or choice.lower() == 'd':
            valid = True
    return choice


def execute(choice, source, destination):
    try:
        ACTIONS[choice]["Fct"](source=source, destination=destination)
    except:
        return f'Une erreur est apparue lors de ' + (
            f'la compression ' if ACTIONS[choice]["Type"] == 'compression' else 'la decompression ') + f'du fichier {source}'
    return (f'La compression ' if ACTIONS[choice]["Type"] == 'compression' else 'La decompression ') + f'du fichier {destination} a bien été effectuée'


def main():
    # From ex04_program.change_directory
    change_directory()

    # Select action to do
    choice = choose_action()
    source = ask_source(choice)
    destination = ask_destination(choice)

    # Execute the selected action
    result = execute(choice, source, destination)
    print(result)


if __name__ == '__main__':
    main()
