import unittest
from banking_system import Bank


class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.savings = self.bank.create_account(
            "savings", "S1001", "Test User", 5000
        )
        self.current = self.bank.create_account(
            "current", "C1001", "Current User", 1000
        )

    def test_deposit(self):
        self.savings.deposit(1000)
        self.assertEqual(self.savings.balance, 6000)

    def test_savings_withdrawal(self):
        self.savings.withdraw(1000)
        self.assertEqual(self.savings.balance, 4000)

    def test_savings_minimum_balance(self):
        with self.assertRaises(ValueError):
            self.savings.withdraw(4600)

    def test_current_account_overdraft(self):
        self.current.withdraw(4000)
        self.assertEqual(self.current.balance, -3000)

    def test_transaction_history(self):
        self.savings.deposit(500)
        history = self.savings.transaction_history()
        self.assertGreaterEqual(len(history), 2)
        self.assertEqual(history[-1]["type"], "Deposit")

    def test_duplicate_account(self):
        with self.assertRaises(ValueError):
            self.bank.create_account("savings", "S1001", "Another User", 1000)


if __name__ == "__main__":
    unittest.main()
