from typing import Union


class Integer:

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> Union["Integer", str]:
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str) -> "Integer":
        value = value.upper()
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        for i in range(len(value) - 1):
            if roman[value[i]] < roman[value[i + 1]]:
                num += roman[value[i]] * -1
                continue
            num += roman[value[i]]

        num += roman[value[-1]]

        return cls(num)

    @classmethod
    def from_string(cls, value: str) -> Union["Integer", str]:
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
third_num = Integer.from_roman("MCMLXXXIX")
print(third_num.value)
