from typing import Union


class Account:

    def __init__(self, i_d: int, name: str, balance: int = 0) -> None:
        self.id = i_d
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[int, str]:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
print()
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
