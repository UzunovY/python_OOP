class Profile:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self, value) -> None:
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value) -> None:
        valid_length = len(value) >= 8
        has_upper = any([ch for ch in value if ch.isupper()])
        has_digit = any([ch for ch in value if ch.isdigit()])

        if not (valid_length and has_upper and has_digit):
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" ' \
               f'and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
