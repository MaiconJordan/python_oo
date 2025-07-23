from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        pass

class WithdrawalFee(FeeStrategy):
    def calculate_fee(self, amount: float) -> float:
        return amount * 0.0003  # 0.03%

class BankAccount(Account):
    def __init__(self, balance: float = 0.0, fee_strategy: FeeStrategy = None):
        self._balance = balance
        self._fee_strategy = fee_strategy or WithdrawalFee()

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        fee = self._fee_strategy.calculate_fee(amount)
        total = amount + fee
        if total > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= total

    def charge_withdrawal_fee(self, amount: float) -> float:
        return self._fee_strategy.calculate_fee(amount)

# Exemplo de uso:
if __name__ == "__main__":
    account = BankAccount(balance=1000.0)
    account.deposit(500.0)
    print(f"Saldo após depósito: {account.balance}")
    account.withdraw(200.0)
    print(f"Saldo após saque: {account.balance}")