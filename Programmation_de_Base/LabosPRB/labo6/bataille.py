from random import shuffle

NUMBER_OF_CARDS = 52
VALET = 11
DAME = 12
ROI = 13
AS = 14

def to_text(card):
    """
    Converts a card from the form tuple(str, int) to its textual representation.
    :param card: tuple(str, int), e.g.: ('Carreau', 3)
    :return: str, representation of the card
    """
    carte = ('Carreau', 3)
    carte_texte = ''
    for element in carte:
        carte_texte += str(element)
    return carte_texte

def display_card(card):
    """
    Prints a card on screen
    :param card: tuple(str, int), e.g.: ('Carreau', 3)
    :return: None
    """
    print(to_text(card))


def display_deck(player, deck):
    """
    Prints a deck on screen
    :param player: str, deck's player name
    :param deck: list, the list of cards. Each card is a tuple(str, int), e.g.: ('Carreau', 3)
    :return: None
    """
    print(f'{player} : {deck}')


def generate_deck():
    """
    Generates a deck (list) of NUMBER_OF_CARDS cards (tuple(str, int))
    :return: list: a list representing a deck of NUMBER_OF_CARDS cards.
    """
    carreau = [2, 3, 4, 5, 6, 7, 8, 9, 10, VALET, DAME, ROI, AS]
    coeur = [2, 3, 4, 5, 6, 7, 8, 9, 10, VALET, DAME, ROI, AS]
    trefle = [2, 3, 4, 5, 6, 7, 8, 9, 10, VALET, DAME, ROI, AS]
    pique = [2, 3, 4, 5, 6, 7, 8, 9, 10, VALET, DAME, ROI, AS]

    couleur = [carreau, coeur, trefle, pique]

    deck = []

    for i in range(len(couleur)):
        if i == 0:
            typeCarte = 'Carreau'

        elif i == 1:
            typeCarte = 'Coeur'

        elif i == 2:
            typeCarte = 'Trèfle'

        else:
            typeCarte = 'Pique'



        for j in range(len(couleur[i])):
            numeroCarte = j + 2

            carte = (typeCarte, numeroCarte)
            deck.append(carte)

    return deck



def distribute_cards(deck):
    """
    From a given deck, this function shuffles and splits it in two parts, and returns it as a tuple of
    decks: (list, list)
    :param deck: list, a list representing a deck of NUMBER_OF_CARDS cards.
    :return:
    """
    deck1 = []
    deck2 = []
    shuffle(deck)
    moitie_du_deck = NUMBER_OF_CARDS // 2


    for card in deck[:moitie_du_deck]:
        deck1.append(card)

    for card in deck[moitie_du_deck:NUMBER_OF_CARDS]:
        deck2.append(card)

    return deck1, deck2





def fight_cards(a, b):
    """
    Given two cards, a and b, this function returns the one card that has the highest value. When both a and b have the
    same values, the result is None.
    :param a: tuple(str, int): a card
    :param b: tuple(str, int): a card
    :return: Returns a card (tuple, int) if one of a or b is higher than the other, else None.
    """

    valeur_a = a[1]
    valeur_b = b[1]

    if valeur_a == valeur_b:
        return None

    elif valeur_a > valeur_b:
        return a

    else:
        return b





def find_winning_deck_if_empty_deck(player_1_deck, player_2_deck):
    """
    Given two decks, this function checks if one of them has no more cards in it. If a deck with no card is found, this
    function returns the winning deck (the one which then has all the cards). Otherwise, this function returns None.
    :param player_1_deck: list, a list representing a deck of NUMBER_OF_CARDS cards.
    :param player_2_deck: list, a list representing a deck of NUMBER_OF_CARDS cards.
    :return: if one deck has no card, returns the other. Otherwise, returns None.
    """
    if len(player_1_deck) != 0 and len(player_2_deck) != 0:
        return None

    elif len(player_1_deck) == 0:
        return player_2_deck

    else:
        return player_1_deck



def fight(player_1_deck, player_2_deck, rewards):
    """
    This function simulates one fight sequence of the game and returns the winning deck:
    - Each player draws one card
    - Those cards are added to the rewards list
    - Both cards fight each other
    - When a player wins, the cards in rewards are shuffled and put at the bottom of his deck.
    - When the cards values are equal, a battle is triggered:
        - Each player draws two cards and add them to the rewards
        - The last cards drawn fight each other.
        - When a player wins, the cards in rewards are shuffled and put at the bottom of his deck.
        - When the cards values are equal, a new battle is triggered.
    - Whenever one deck becomes empty, we have a winner.
    :param player_1_deck: list, a list representing a deck of NUMBER_OF_CARDS cards.
    :param player_2_deck: list, a list representing a deck of NUMBER_OF_CARDS cards.
    :param rewards: list, cards that should be put back to the winner's deck.
    :return: list, the winning deck.
    """
    rewards.append(player_1_deck.pop(0))
    rewards.append(player_2_deck.pop(0))

    carte_gagnante = fight_cards(rewards[0], rewards[1])

    if carte_gagnante != rewards[1]:
        shuffle(rewards)
        for card in rewards:
            player_1_deck.append(rewards.pop(rewards.index(card)))

        return player_1_deck

    elif carte_gagnante != rewards[0]:
        shuffle(rewards)
        for card in rewards:
            player_2_deck.append(rewards.pop(rewards.index(card)))

        return player_2_deck

                                    ######## 1ere Bataille ###########
    else:

        for i in range(2):
            rewards.append(player_1_deck.pop(i+1))
            rewards.append(player_2_deck.pop(i+1))

        gagnant_bataille = fight_cards(rewards[4], rewards[5])


        if gagnant_bataille != rewards[5]:
            shuffle(rewards)
            for card in rewards:
                player_1_deck.append(rewards.pop(rewards.index(card)))

            return player_1_deck

        elif gagnant_bataille != rewards[4]:
            shuffle(rewards)
            for card in rewards:
                player_2_deck.append(rewards.pop(rewards.index(card)))

            return player_2_deck
                                    ######## 2e Bataille ###########
        else:
            for i in range(2):
                rewards.append(player_1_deck.pop(i + 3))
                rewards.append(player_2_deck.pop(i + 3))

            gagnant_bataille2 = fight_cards(rewards[6], rewards[7])

            if gagnant_bataille2 != rewards[7]:
                shuffle(rewards)
                for card in rewards:
                    player_1_deck.append(rewards.pop(rewards.index(card)))

                return player_1_deck

            elif gagnant_bataille2 != rewards[6]:
                shuffle(rewards)
                for card in rewards:
                    player_2_deck.append(rewards.pop(rewards.index(card)))

                return player_2_deck


    if find_winning_deck_if_empty_deck(player_1_deck, player_2_deck):
        return find_winning_deck_if_empty_deck(player_1_deck, player_2_deck)







def play(player_1, player_1_deck, player_2, player_2_deck):
    """
    This function handles the game loop until a winner is found.
    :param player_1: str, the first player's name
    :param player_1_deck: list, the list representing the first player's deck of NUMBER_OF_CARDS cards.
    :param player_2: str, the second player's name
    :param player_2_deck: list, the list representing the second player's deck of NUMBER_OF_CARDS cards.
    :return:
    """

    while not find_winning_deck_if_empty_deck(player_1_deck, player_2_deck):
        rewards = []
        deck_gagnant = fight(player_1_deck, player_2_deck, rewards)

    if deck_gagnant == player_1_deck:
        return player_1
    else:
        return player_2


def _main():
    deck = generate_deck()

    player_1 = input('Enter player #1 name: ')
    player_2 = input('Enter player #2 name: ')

    player_1_deck, player_2_deck = distribute_cards(deck)

    display_deck(player_1, player_1_deck)
    display_deck(player_2, player_2_deck)

    winner = play(player_1, player_1_deck, player_2, player_2_deck)

    print('\n\n--- WE HAVE A WINNER --- ')
    print(f'The winner is {winner} !')





if __name__ == '__main__':
    _main()
