from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    valid_loans = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    valid_clients = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loans:
            raise Exception("Invalid loan type!")
        self.loans.append(self.valid_loans[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.valid_clients:
            raise Exception("Invalid client type!")
        if self.capacity <= 0:
            return "Not enough bank capacity."
        self.clients.append(self.valid_clients[client_type](client_name, client_id, income))
        self.capacity -= 1
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client.possible_loan_type != loan_type:
            raise Exception("Inappropriate loan type!")

        for loan in self.loans:
            if loan.loan_type == loan_type:
                client.loans.append(loan)
                self.loans.remove(loan)
                break

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        matched_loans = 0
        for loan in self.loans:
            if loan.loan_type == loan_type:
                loan.increase_interest_rate()
                matched_loans += 1
        return f"Successfully changed {matched_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                affected_clients += 1
        return f"Number of clients affected: {affected_clients}."

    def get_statistics(self):
        granted_loans = []
        total_client_interest_rate = 0
        for c in self.clients:
            granted_loans.extend(c.loans)
            total_client_interest_rate += c.interest

        avg_client_interest_rate = total_client_interest_rate / len(self.clients) if self.clients else 0

        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum(c.income for c in self.clients):.2f}",
                  f"Granted Loans: {len(granted_loans)}, Total Sum: {sum(l.amount for l in granted_loans):.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
                  ]

        return "\n".join(result).strip()

