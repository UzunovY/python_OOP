from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):

    def __init__(self):
        super().__init__(3.5, 50_000.0)

    def increase_interest_rate(self):
        self.interest_rate += 0.5

    @property
    def loan_type(self):
        return "MortgageLoan"
