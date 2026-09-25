from abc import ABC, abstractmethod
from datetime import datetime


class Account(ABC):
    """Abstract base class for bank accounts."""

    def __init__(self, account_number, holder_name, opening_balance=0.0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = float(opening_balance)
        self._transactions = []

        if opening_balance > 0:
            self._record_transaction("Deposit", opening_balance, self._balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def holder_name(self):
        return self._holder_name

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance += amount
        self._record_transaction("Deposit", amount, self._balance)
        return self._balance

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money according to the account rules."""
        pass

    def _complete_withdrawal(self, amount):
        self._balance -= amount
        self._record_transaction("Withdrawal", amount, self._balance)
        return self._balance

    def _record_transaction(self, transaction_type, amount, balance_after):
        self._transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": round(float(amount), 2),
            "balance": round(float(balance_after), 2)
        })

    def transaction_history(self):
        return list(self._transactions)

    def display_details(self):
        return (
            f"Account: {self.account_number} | "
            f"Holder: {self.holder_name} | "
            f"Balance: ₹{self.balance:.2f}"
        )


class SavingsAccount(Account):
    """Savings account with a minimum balance requirement."""

    MIN_BALANCE = 500.0

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(
                f"Withdrawal denied. Minimum balance of ₹{self.MIN_BALANCE:.2f} is required."
            )

        return self._complete_withdrawal(amount)


class CurrentAccount(Account):
    """Current account that allows withdrawals up to a defined overdraft limit."""

    OVERDRAFT_LIMIT = 5000.0

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise ValueError(
                f"Withdrawal denied. Overdraft limit is ₹{self.OVERDRAFT_LIMIT:.2f}."
            )

        return self._complete_withdrawal(amount)


class Bank:
    """Manages bank accounts and delegates operations to account objects."""

    def __init__(self):
        self._accounts = {}

    def create_account(self, account_type, account_number, holder_name, opening_balance=0):
        if account_number in self._accounts:
            raise ValueError("Account number already exists.")

        account_type = account_type.lower()

        if account_type == "savings":
            account = SavingsAccount(
                account_number, holder_name, opening_balance
            )
        elif account_type == "current":
            account = CurrentAccount(
                account_number, holder_name, opening_balance
            )
        else:
            raise ValueError("Account type must be 'savings' or 'current'.")

        self._accounts[account_number] = account
        return account

    def get_account(self, account_number):
        account = self._accounts.get(account_number)
        if account is None:
            raise ValueError("Account not found.")
        return account

    def list_accounts(self):
        return list(self._accounts.values())


def show_transaction_history(account):
    print(f"\n--- Transaction History: {account.account_number} ---")

    history = account.transaction_history()

    if not history:
        print("No transactions found.")
        return

    for transaction in history:
        print(
            f"{transaction['date']} | "
            f"{transaction['type']} | "
            f"₹{transaction['amount']:.2f} | "
            f"Balance: ₹{transaction['balance']:.2f}"
        )


def main():
    bank = Bank()

    # Sample accounts for demonstration.
    bank.create_account("savings", "S1001", "Ravi", 5000)
    bank.create_account("current", "C1001", "Anita", 3000)

    while True:
        print("\n========== PYTHON BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                account_type = input("Account type (savings/current): ").strip()
                account_number = input("Account number: ").strip()
                holder_name = input("Account holder name: ").strip()
                opening_balance = float(input("Opening balance: "))

                account = bank.create_account(
                    account_type,
                    account_number,
                    holder_name,
                    opening_balance
                )
                print("Account created successfully.")
                print(account.display_details())

            elif choice == "2":
                print("\n--- Accounts ---")
                accounts = bank.list_accounts()

                for account in accounts:
                    print(account.display_details())

            elif choice == "3":
                account_number = input("Account number: ").strip()
                amount = float(input("Deposit amount: "))

                account = bank.get_account(account_number)
                new_balance = account.deposit(amount)

                print(f"Deposit successful. New balance: ₹{new_balance:.2f}")

            elif choice == "4":
                account_number = input("Account number: ").strip()
                amount = float(input("Withdrawal amount: "))

                account = bank.get_account(account_number)
                new_balance = account.withdraw(amount)

                print(f"Withdrawal successful. New balance: ₹{new_balance:.2f}")

            elif choice == "5":
                account_number = input("Account number: ").strip()
                account = bank.get_account(account_number)
                show_transaction_history(account)

            elif choice == "6":
                print("Thank you for using the Python Banking System.")
                break

            else:
                print("Please choose a number from 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
