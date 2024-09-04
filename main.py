class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def calcular_saldo_final(self):
        if self.saldo < 10000.00:
            self.saldo = self.saldo * (1 + 0.03)
        else:
            self.saldo = self.saldo * (1 + 0.04)
        return self.saldo

    def mostrar_saldo_final(self):
        saldo_final = self.calcular_saldo_final()
        print(f"Saldo final es: ${saldo_final:.2f}")


# Ejemplo de uso
print('Dame saldo actual:')
saldo_inicial = float(input())

# Crear una instancia de CuentaBancaria con el saldo inicial
mi_cuenta = CuentaBancaria(saldo_inicial)

# Mostrar el saldo final
mi_cuenta.mostrar_saldo_final()
