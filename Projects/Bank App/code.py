from datetime import datetime
import pandas as pd

class Bank_App:
    def __init__(self):
        self.balance = 0
        self.transaction_history = {
            "Type": [],
            "Amount": [],
            "Balance": [],
            "Timestamp": []
        }

    class InvalidAmountError(Exception):
        def __init__(self, amount):
            self.amount = amount
        def __str__(self):
            return f"The shared amount = {self.amount} is not a valid amount, value should not be negative or zero"

    class InsufficientFundsError(Exception):
        def __init__(self, amount, balance):
            self.amount = amount
            self.balance = balance
        def __str__(self):
            return f"The amount {self.amount} cannot be withdrawn, the available balance is {self.balance}"

    def transactionHistory(self, method, amount):
        current_time = datetime.now().strftime("%Y-%m-%d")
        self.transaction_history["Type"].append(method)
        self.transaction_history["Amount"].append(amount)
        self.transaction_history["Balance"].append(self.balance)
        self.transaction_history["Timestamp"].append(current_time)

    def deposit(self, amount):
        if amount <= 0:
            raise Bank_App.InvalidAmountError(amount)
        self.balance += amount
        self.transactionHistory("Deposit", amount)
        print(f"Deposited Successfully, Updated Balance : {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise Bank_App.InvalidAmountError(amount)
        if amount > self.balance:
            raise Bank_App.InsufficientFundsError(amount, self.balance)

        total_withdrawal = 0
        for i in range(len(self.transaction_history["Type"])):
            if (self.transaction_history["Type"][i] == "Withdraw" and
                self.transaction_history["Timestamp"][i][:10] == datetime.now().strftime("%Y-%m-%d")):
                total_withdrawal += self.transaction_history["Amount"][i]

        if total_withdrawal + amount <= 50000:
            self.balance -= amount
            self.transactionHistory("Withdraw", amount)
            print(f"Withdrawal Successful, Updated Balance : {self.balance}")
        else:
            print("You have reached your daily limit of 50000 as withdrawal")

    def _rollback_last_log(self):
        for column in self.transaction_history.values():
            if column:
                column.pop()

    def transfer(self, other_account, amount):
        if amount > self.balance:
            raise Bank_App.InsufficientFundsError(amount, self.balance)
        try:
            self.withdraw(amount)
            other_account.deposit(amount)
            print("---------------\nTransfer Completed Successfully")
            return True
        except Exception as e:
            print("\nError During Transfer, Rolling Back")
            self.balance += amount
            self._rollback_last_log()
            return False

    def get_history_df(self):
        """Return transaction history as a Pandas DataFrame"""
        return pd.DataFrame(self.transaction_history)


def main():
    acc1 = Bank_App()
    acc2 = Bank_App()

    while True:
        print("\n===== Bank Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer to another account")
        print("4. Show Transaction History (DataFrame)")
        print("5. Show Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amt = float(input("Enter amount to deposit: "))
                acc1.deposit(amt)

            elif choice == "2":
                amt = float(input("Enter amount to withdraw: "))
                acc1.withdraw(amt)

            elif choice == "3":
                amt = float(input("Enter amount to transfer: "))
                acc1.transfer(acc2, amt)

            elif choice == "4":
                print(acc1.get_history_df())

            elif choice == "5":
                print(f"Current Balance: {acc1.balance}")

            elif choice == "6":
                print("Exiting... Thank you!")
                break

            else:
                print("Invalid choice, please try again.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
