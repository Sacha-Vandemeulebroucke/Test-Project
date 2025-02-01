
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    while (amount := int(input("Select how much you want to deposit in $: "))) <= 0:
        print("The amount must be greater than 0.")
    balance += amount
    return balance

def withdraw(balance):
    while (amount := int(input("Select how much you want to withdraw in $: "))) <= 0:
        print("The amount must be greater than 0.")
    if amount > balance:
        print('Operation not allowed')
    else:
        balance -= amount
        return balance

def print_options():
    print('*****************')
    print('Banking Program')
    print('*****************')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    print('*****************')


def main():
    balance = 0
    is_running = True

    while is_running:

        print_options()

        choice = int(input('Enter your choice (1-4): '))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance = deposit(balance)
            case 3:
                if balance <= 0:
                    print('Operation not allowed')
                else:
                    balance = withdraw(balance)
            case 4:
                is_running = False
            case _:
                print('Please enter a number between 1 and 4')



main()