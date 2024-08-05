import random
import time

num = ['💀', '😊', '🗣️', '🔥', '‼️']

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

def bet(amount):
    while True:
       try:
            global bet_amount
            bet_amount = int(input(f'you have {amount}. how much to bet: '))
            if 1 <= bet_amount <= amount:
                return bet_amount
            else:
                print('enter bet in range')
       except ValueError:
           print('enter a number')
def slot(amount):

    dec = input('you want to play: ').lower()

    match dec:
        case 'yes':
            bet(amount)
            slot1 = random.choice(num)
            slot2 = random.choice(num)
            slot3 = random.choice(num)
            slot4 = random.choice(num)
            slot5 = random.choice(num)
            slots = {slot1, slot2, slot3, slot4, slot5}
            print(slot1, end=" "); time.sleep(0.25)
            print(slot2, end=" "); time.sleep(0.5)
            print(slot3, end=" "); time.sleep(1)
            print(slot4, end=" "); time.sleep(2)
            print(slot5); time.sleep(1)
            logic(slot1, slot2, slot3, slot4, slot5, amount,slots)

        case 'no':
            print('thanks for playing')

        case _:
            print('put in yes or no')
            slot(amount)
def logic(slot1, slot2, slot3, slot4, slot5, amount, slots):

    if len(slots) == 1:
        print('big win')
        amount = amount + bet_amount * 5
        print(f'you won {bet_amount}, your total is {amount}')
        slot(amount)

    elif len(slots) == 2:
        print('medium win')
        amount = amount + bet_amount * 3
        print(f'you won {bet_amount}, your total is {amount}')
        slot(amount)

    elif len(slots) == 3:
        print('small win')
        amount = amount + bet_amount * 1
        print(f'you won {bet_amount}, your total is {amount}')
        slot(amount)

    else:
        print('lose')
        if bet_amount >= amount:
            print('you have no money you lose')
        else:
            amount = amount - bet_amount
            print(f'you have {amount}')
            slot(amount)




if __name__ == '__main__':
    start()



