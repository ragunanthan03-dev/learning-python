#This program logic is made by match-case statement(switch) instead of if-else ladder.

balance=0 #Global variable

def check_balance():
        print(f"Your balance is: ₹{balance}")

def deposit():
    global balance #Using Global keyword because we are modifying a global variable
    amount=int(input("Enter amount:"))
    match amount<=0:
        case True:
            print("Invalid amount")
            print("Please Try Again")
        case _:
            balance+=amount
            print(f'₹{amount} deposited successfully')
            print(f"Your balance is: ₹{balance}")

def withdraw():
    global balance
    amount=int(input("Enter amount:"))
    match amount > balance :
        case True:
            print("Invalid amount")
            print("Please Try Again")
        case _:
            balance-=amount
            print(f"₹{amount} withdrawn successfully")
            print(f"Your balance is: ₹{balance}")

while True:
    print("\n---------------MENU-----------------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("------------------------------------")
    print()
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            check_balance()
        case 2:
            deposit()
        case 3:
            withdraw()
        case 4:
            print("Thank you for using our ATM")
            break
        case _:
            print("Invalid choice")
            print("Please Try Again")


