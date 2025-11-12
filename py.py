# Automated Teller Machine Operation

#----------------account balance function--------------
def acc_balance(balance):
    print("Checking Balance.....")
    print(f"Your current balance is: ${balance:.2f}")
    # print("Checking ")

# def payment():
#     pass
#----------------withdraw function--------------
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount cannot be negative or has to be greater than 0")
        return 0
    else:
        return amount

#---------------------deposit---------------------
def deposit(balance):
    amount = float(input("Enter the amount you want to deposit: "))

    if amount < 0:
        print("You cannot deposit a negative amount or invalid amount")
        return 0
    else:
        print(f"The deposit of ${amount:.2f} was successful")
        return amount

#-------------------transfer function------------------
def transfer(balance):

    print("1. First Bank",)
    print("2. United Bank Africa")
    print("3. Sterling Bank ")
    print("4. Wema Bank ")
    print("5. Polaris Bank")
    print("6. Guaranty Trust Bank")
    choice =input("Select the bank to transfer(1-6): ")
    banks = {
        "1": "First Bank",
        "2": "United Bank Africa",
        "3": "Sterling Bank",
        "4": "Wema Bank",
        "5": "Polaris Bank",
        "6": "Guaranty Trust Bank",
    }

    if choice not in banks:
        print("Invalid choice")
        return 0
    print(f"You selected {banks[choice]}")

    try:
        amount = float(input("Enter amount do you want to transfer: "))
        user = input("Enter the account number: ")
        user = user.replace(" ", "")
    except ValueError:
        print("Invalid input")
        return 0

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < balance:
        print(f"You have succesfully transferred the sum of ${amount:.2f} to {user} {banks[choice]}")
    elif amount < 0:
        print("Amount cannot be negative or has to be greater than 0")
        return 0
    else:
        return amount,user

def setup_pin(correct_pin):
    correct_pin = input("Enter your new 4-digit pin: ")
    print("You have successfully reset your pin ")
    return correct_pin
#----------------------the main function-----------------
def main():
    balance = 0
    is_running = True
    attempts = 3
    correct_pin = "1234"

    while attempts > 0:
        entered_pin = input("Enter your 4-digits PIN: ")
        entered_pin = entered_pin.replace(" ", "")
        # entered_pin = entered_pin.isdigit()
        if entered_pin == correct_pin:
            print("\n PIN correct! Access granted.\n")
            break
        else:
            attempts -= 1
            print(f"\n PIN NOT correct! Access denied. You have {attempts} attempts left  \n")
        if attempts == 0:
            is_running = False
            print(f"\n Your account has been blocked temporary. Too many attempts.")

    while is_running:
        print("Running Program")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Transfer")
        print("5. Reset pin")
        print("6. Exit")

        choice = input("Enter your choice(1-6): ")
        if choice == "1":
            balance += deposit(balance)
        elif choice == "2":
            balance -= withdraw(balance)
        elif choice == "3":
            acc_balance(balance)
        elif choice == "4":
            transfer(balance)
        elif choice == "5":
            setup_pin(correct_pin)
        elif choice == "6":
            is_running = False
            print("Thank you for using our services")
            print("We will be expecting ")
        else:
            print("Invalid Choice or not part of the options")

if __name__ == '__main__':
    main()