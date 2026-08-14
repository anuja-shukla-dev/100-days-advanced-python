class BankAccount:
    bank_name = "ABC Bank"
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if self.validate_amount(amount)==True:
            self.balance += amount
            print("Amount deposited",amount)
        else:
            print("Amount cannot be negative")

    def withdraw(self, amount):
        if self.validate_amount(amount)==True and amount <=self.balance:
            self.balance -=amount
            print("Amount withdraw",amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print(f"Bank name: {self.bank_name}")

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False

acc = BankAccount("Rahul", 2000)
acc.display_balance()

amount_deposit = int(input("Enter amount to deposit: "))
acc.deposit(amount_deposit)

amount_withdraw = int(input("Enter amount to withdraw: "))
acc.withdraw(amount_withdraw)
acc.display_balance()