import random
import time

num = ['💀', '😊', '🗣️', '🔥', '‼️']


# start the program with balance, calls slot
def start():
    try:
        amount = int(input('how much to put in balance: '))
        if amount <= 0:
            print('Enter positive amount')
            start()
        else:
            slot(amount)
    except ValueError:
        print('put in a number')
        start()


# asks for the amount to bet
def bet(amount):
    while True:
        try:
            global bet_amount
            bet_amount = int(input(f'You have {amount}. How much do you want to bet: '))
            if 1 <= bet_amount <= amount:
                return bet_amount
            else:
                print('enter bet in range')
        except ValueError:
            print('Enter a number')


# ask if player wants to play, calls roll
def slot(amount):
    dec = input('Do you want to play: ').lower()
    roll(dec, amount)


# generates random slots, calls print_slot or slot
def roll(dec, amount):
    match dec:
        case 'yes':
            bet(amount)
            slot1 = random.choice(num)
            slot2 = random.choice(num)
            slot3 = random.choice(num)
            slot4 = random.choice(num)
            slot5 = random.choice(num)
            rand_num = [slot1, slot2, slot3, slot4, slot5]
            print_slot(rand_num, amount)

        case 'no':
            print('Thanks for playing!')

        case _:
            print('Put in yes or no')
            slot(amount)


# prints the slots, calls logic
def print_slot(rand_num, amount):
    sleep_time = 0.5
    for i in rand_num:
        time.sleep(sleep_time)
        print(i, end=' ')
        sleep_time += 0.5
    print()
    logic(rand_num, amount)


# logic for  slots and prints how much won, calls slot
def logic(rand_num, amount):
    slots = set(rand_num)
    winner = len(slots)
    match winner:

        case 1:
            print('big win')
            amount = amount + bet_amount * 5
            print(f'you won {bet_amount}, your total is {amount}')
            slot(amount)

        case 2:
            print('medium win')
            amount = amount + bet_amount * 3
            print(f'you won {bet_amount * 3}, your total is {amount}')
            slot(amount)

        case 3:
            print('small win')
            amount = amount + bet_amount * 1
            print(f'you won {bet_amount}, your total is {amount}')
            slot(amount)

        case _:
            print('lose')
            if bet_amount >= amount:
                print('you have no money you lose')
            else:
                amount = amount - bet_amount
                print(f'you have {amount}')
                slot(amount)


if __name__ == '__main__':
    start()
