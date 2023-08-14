class BalanceExpection(Exception):
    pass

class BankAccount():
    def __init__(self, name, accBalance):
        self.name = name
        self.balance = accBalance
        print(f"\nConta de '{self.name}' criada com sucesso!\n\n")

    def getBalance(self):
        print(f"\nO saldo de '{self.name}': ${self.balance:.2f}\n\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposito de ${amount:.2f} realizado com sucesso!")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceExpection(
                f"\nSaldo de {self.name} é ${self.balance:.2f}")


    def withdraw(self, amount):
       try:
           self.viableTransaction(amount)
           self.balance -= amount
           print("\nSaque realizado com sucesso!")
           self.getBalance()
       except BalanceExpection as error:
           print(f'\nSaque bloqueado: {error}')

    def transfer(self, amount, account):
        try:
            print("\n__________\nIniciando operação de transação entre contas..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transação completa com sucesso!\n__________\n\n")
        except BalanceExpection as error:
            print(f'\nSaque bloqueado: {error}')

           
    

