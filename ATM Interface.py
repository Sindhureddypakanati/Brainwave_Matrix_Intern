class UserAccount:
    DAILY_LIMIT = 10000
    PER_TRANSACTION_LIMIT = 5000

    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.daily_withdrawn = 0

    def validate_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def deposit_amount(self, amount):
        self.balance += amount
        return f"₹{amount} deposited successfully. New balance: ₹{self.balance}"

    def withdraw_amount(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        if amount > self.PER_TRANSACTION_LIMIT:
            return f"Cannot withdraw more than ₹{self.PER_TRANSACTION_LIMIT} in a single transaction."
        if self.daily_withdrawn + amount > self.DAILY_LIMIT:
            return f"Daily withdrawal limit of ₹{self.DAILY_LIMIT} exceeded."
        self.balance -= amount
        self.daily_withdrawn += amount
        return f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}"

    def change_pin(self, current_pin, new_pin):
        if self.pin == current_pin:
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Incorrect current PIN. PIN change failed."


def register_account(users):
    account_number = input("Enter a new account number: ")
    if account_number in users:
        print("Account number already exists. Try logging in.")
        return None
    pin = input("Set your 4-digit PIN: ")
    balance = float(input("Enter initial deposit amount: "))
    users[account_number] = UserAccount(account_number, pin, balance)
    print("Account created successfully!")
    return users[account_number]


def login(users):
    account_number = input("Enter your account number: ")
    if account_number not in users:
        print("Account not found. Please register.")
        return None
    user = users[account_number]

    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your ATM PIN: ")
        if user.validate_pin(entered_pin):
            print("Login successful!\n")
            return user
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
    print("Too many incorrect attempts. Exiting login.")
    return None


def atm_menu(user):
    while True:
        print("\nChoose an action:")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Change PIN")
        print("5. Logout")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            print("Your Current balance is: ₹", user.check_balance())
        elif choice == "2":
            amount = float(input("Enter Deposit amount: "))
            print(user.deposit_amount(amount))
        elif choice == "3":
            amount = float(input("Enter Withdraw amount (max ₹5000 per transaction): "))
            entered_pin = input("Re-enter your PIN to confirm withdrawal: ")
            if user.validate_pin(entered_pin):
                print(user.withdraw_amount(amount))
            else:
                print("Incorrect PIN. Withdrawal canceled.")
        elif choice == "4":
            current_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")
            print(user.change_pin(current_pin, new_pin))
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def main():
    users = {}
    print("===== Welcome to the ATM Interface =====")

    while True:
        print("\nMain Menu:")
        print("1. Register New Account")
        print("2. Login to Existing Account")
        print("3. Exit")

        main_choice = input("Enter your choice (1/2/3): ")

        if main_choice == "1":
            register_account(users)
        elif main_choice == "2":
            user = login(users)
            if user:
                atm_menu(user)
        elif main_choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()