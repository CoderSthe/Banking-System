# Parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print()
        print(f"Name:       {self.name}")
        print(f"Age:        {self.age}")
        print(f"Gender:     {self.gender}")

# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Account balance has been updated:    R{self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient funds | Balance available: R{self.balance}")
        else:
            self.balance -= self.amount
            print(f"Account balance has been updated:   R{self.balance}")

    def view_balance(self):
        self.show_details()
        print(f"Account balance:    R{self.balance}")