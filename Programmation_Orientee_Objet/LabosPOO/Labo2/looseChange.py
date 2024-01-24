from math import floor

PENNIES = 1
NICKELS = 5
DIMES = 10
QUARTERS = 25

def loose_change(money):
    change = {"pennies": 0, "nickels": 0, "dimes": 0, "quarters": 0}

    if money <= 0:
        return change

    elif type(money) == float:
        money = floor(money)


    change["quarters"] = money // QUARTERS
    reste = money - (change['quarters'] * QUARTERS)

    change["dimes"] = reste // DIMES
    reste = reste - (change['dimes'] * DIMES)

    change["nickels"] = reste // NICKELS
    reste = reste - (change['nickels'] * NICKELS)

    change["pennies"] = reste // PENNIES

    return change


def _main():

    print(loose_change(56))
    print(loose_change(-435))
    print(loose_change(4.935))


if __name__ == '__main__':
    _main()