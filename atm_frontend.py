# atm_frontend.py

from atm_backend import ATM

def display_menu():
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    atm = ATM()
    while True:
        display_menu()
        choice = input("Please choose an option (1-4): ")
        
        if choice == '1':
            balance = atm.check_balance()
            print(f"Your current balance is: ${balance:.2f}")
        
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            success, message = atm.deposit(amount)
            print(message)
        
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            success, message = atm.withdraw(amount)
            print(message)
        
        elif choice == '4':
            print(atm.exit())
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
