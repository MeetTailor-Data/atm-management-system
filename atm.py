balance = float(input("Enter Your Balance: "))

def deposit():
    global balance
    amount = float(input("Enter Amount: "))
    if amount > 0:
        balance += amount
        print("Amount Deposited Successfully")
    else:
        print("Invalid Amount")

def withdraw():
    global balance
    amount = float(input("Enter Amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Amount Withdrawn Successfully")
    else:
        print("Invalid Amount or Insufficient Balance")

def check_balance():
    print("Your Balance is:", balance)

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Exiting ATM...")
        break
    else:
        print("Invalid Choice! Try again.")
