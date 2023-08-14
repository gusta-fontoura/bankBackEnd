from bank_account import *

Gustavo = BankAccount('Gustavo', 500)
Maria = BankAccount('Maria', 2000)


Gustavo.getBalance()
Maria.getBalance()

Gustavo.deposit(1000)
Maria.deposit(500)

Maria.withdraw(100000)
Maria.withdraw(2000)

Maria.transfer(40000, 'Gustavo')
Maria.transfer(200, Gustavo)
    