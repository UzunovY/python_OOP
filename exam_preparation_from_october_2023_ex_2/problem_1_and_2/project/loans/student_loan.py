from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):

    def __init__(self):
        super().__init__(1.5, 2_000.0)

    def increase_interest_rate(self):
        self.interest_rate += 0.2

    @property
    def loan_type(self):
        return "StudentLoan"
