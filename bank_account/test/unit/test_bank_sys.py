import unittest

from src.account import BankAccount

class TestAccount(unittest.TestCase):
    def setUp(self):
        print("Setting up!")
        self.account = BankAccount("A123456Z", 0)

    def tearDown(self):
        print("Tearing Down!")

    def test_deposit(self):
        print(f"Balance starting: {self.account.balance}")
        initial_amt = self.account.balance
        deposit_amt = 100
        self.account.deposit(deposit_amt)
        self.assertEqual(self.account.balance, deposit_amt + initial_amt)
        print(f"Balance ending is: [(deposit amt){deposit_amt}+(initial amt){initial_amt}={deposit_amt+initial_amt}] {self.account.balance}")

    def test_get_balance(self):
        print("\tTest 1 (initial):")
        self.assertEqual(self.account.get_balance(),self.account.balance)
        print(f"\t\t{self.account.get_balance()} is equal to balance ({self.account.balance})")
        deposit_amt = 150
        self.account.deposit(deposit_amt)
        print(f"\tTest 2 (deposit of {deposit_amt}):")
        self.assertEqual(self.account.get_balance(),self.account.balance)
        print(f"\t\t{self.account.get_balance()} is equal to balance ({self.account.balance})")

    def test_get_account_number(self):
        self.assertEqual