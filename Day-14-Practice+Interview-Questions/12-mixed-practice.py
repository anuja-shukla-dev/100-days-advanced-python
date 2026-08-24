class BankAccount:
    def __init__(self, account_holder, account_no, balance):
        self.account_holder = account_holder
        self.account_no = account_no
        self._balance = balance

    def transaction_logger(func):
        def wrapper(*args, **kwargs):
            print(f"Transaction: {func.__name__}")
            func(*args, **kwargs)

        return wrapper

    @transaction_logger
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Amount deposited",amount)
            print("Total amount",self._balance)
        else:
            print("Amount should be positive")

    @transaction_logger
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print("Amount withdraw",amount)
            print("Total amount",self._balance)
        else:
            print("Invalid amount")

    @property
    def balance(self):
        return self._balance

    def __gt__(self, other):
        return self.balance > other.balance

    @classmethod
    def create_account(cls, data):
        account_holder, account_no, balance = data.split("-")

        return cls(account_holder, int(account_no), float(balance))

    @staticmethod
    def validate_account_no(number):
        if len(number) == 5 and number.isdigit():
            return True

        return False


    def display(self):
        print("======ACCOUNT DETAILS=====")
        print("Account holder",self.account_holder)
        print("Account no",self.account_no)
        print("Balance",self.balance)

name = input("Enter name: ")
acc_no = int(input("Enter account no: "))
balance = float(input("Enter initial balance: "))

acc1 = BankAccount(name, acc_no, balance)
acc1.display()

print(BankAccount.validate_account_no("12345"))

acc2 = BankAccount.create_account("Rahul-12345-200000")
acc2.display()

print(acc1 > acc2)

