
class ATM:
    def __init__(self):
        self.balance = 1000.0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"${amount} deposited successfully."
        else:
            return False, "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return True, f"${amount} withdrawn successfully."
            else:
                return False, "Insufficient balance."
        else:
            return False, "Withdrawal amount must be positive."

    def exit(self):
        return "Thank you for using the ATM. Goodbye!"
