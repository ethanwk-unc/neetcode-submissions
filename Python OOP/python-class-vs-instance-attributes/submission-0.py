class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts  = 0 
    total_balance = 0
    
    def __init__(self, name:str, balance:float):
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    def get_balance(self) -> float:
        return self.balance

    def get_name(self) -> str:
        return self.name


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
Alice_acc = BankAccount("Alice", 1000)
Bob_acc = BankAccount("Bob", 2000)

print(f"{Alice_acc.get_name()}'s balance: ${Alice_acc.get_balance()}")
print(f"{Bob_acc.get_name()}'s balance: ${Bob_acc.get_balance()}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")