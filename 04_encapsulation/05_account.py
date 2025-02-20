from typing import Union


class Account:

    def __init__(self, id_: int, balance: int, pin: int) -> None:
        self.__id = id_
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin) -> Union[int, str]:
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
