class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __str__(self):
        return f"Owner: {self.owner} | Balance: {self.balance}"

acc1 = BankAccount("Rahul", 900000)
acc2 = BankAccount("Raman", 950000)

print(acc1)
print(acc2)
print(acc1 + acc2)
print(acc1 > acc2)
print(acc1 == acc2)