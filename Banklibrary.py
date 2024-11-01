class Cuenta: 
    def __init__(self, bank_account, balance=0):
        self.bank_account = bank_account  
        self.balance = balance  

    def deposito(self, cantidad=int(input("Introduzca la cantidad a depositar"))):
        # Verifica que la cantidad sea positiva
        if cantidad >= 0:
            self.balance += cantidad
            print(f"Se han depositado {cantidad}.Su balance actual es de: {self.balance}")
        else:
            print("Por favor introduzca una cantidad positiva")

    def retirar(self, cantidad=int(input("Introduzca la cantidad a retirar"))):
        # Verifica que la cantidad sea positiva
        if cantidad > 0:
            if self.balance >= cantidad:
                self.balance -= cantidad  
                print(f"Se han retirado {cantidad}. Su balance actual es de: {self.balance}")
            else:
                print(f"Fondos insuficientes. Su balance actual es de: {self.balance}")
        else:
            print("Por favor introduzca una cantidad positiva")

    def get_balance(self): 
        return self.balance
    