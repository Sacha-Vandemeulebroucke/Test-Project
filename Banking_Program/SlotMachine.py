import random

def spin_row():
    symbols = ["🍉","🍒","🍋","🍺","🍀"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("|".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        print("You win !!!")
        match row[0]:
            case "🍉":
                return bet*3
            case "🍒":
                return bet*5
            case "🍋":
                return bet*8
            case "🍺":
                return bet*15
            case "🍀":
                return bet*20
            case _:
                print("Error")
    else:
        print("Not this time")
        return 0


def main():
    balance = 100

    print('***********************')
    print('Welcome to Python Slots')
    print("Symbols: 🍉 🍒 🍋 🍺 🍀")
    print('***********************')

    while balance > 0:

        print(f'Current balance: ${balance}')
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print('Please enter a valid number')
            continue

        bet = int(bet)

        if bet > balance:
            print(f"Not enough money. You actually have : {balance}")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")


        balance -= bet
        row = spin_row()
        print_row(row)
        balance += get_payout(row,bet)

        play_again = input(f"Play again ? (type q to quit)")

        if play_again.casefold() == "q":
            break

if __name__ == '__main__':
    main()


