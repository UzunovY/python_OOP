class EmailValidator:

    def __init__(self, min_length: int, _mails: list, _domains: list) -> None:
        self.min_length = min_length
        self.mails = _mails
        self.domains = _domains

    def __is_name_valid(self, name) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain) -> bool:
        return domain in self.domains

    def validate(self, email) -> bool:
        name, body = email.split("@")
        mail, domain = body.split(".")

        return (self.__is_name_valid(name)
                and self.__is_mail_valid(mail)
                and self.__is_domain_valid(domain))


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
