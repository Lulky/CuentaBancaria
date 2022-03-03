# from User import User
from CuentaBancaria import CuentaBancaria

# john = User("jhon")
# mary = User("Mary")



# john.hacer_deposito(1500)
# john.hacer_retiro(100)

# mary.hacer_deposito(100)

# john.transfer_dinero(mary, 100)

# john.mostrar_balance_usuario()

# print(john.pesos)
# print(mary.pesos)

cuenta = CuentaBancaria(8, 100)
cuenta_2 = CuentaBancaria(10, 1000)

cuenta.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).hacer_retiro(100).generar_interes().imprimir_cuentas()

cuenta_2.hacer_deposito(100).hacer_deposito(100).hacer_retiro(100).hacer_retiro(50).hacer_retiro(20).hacer_retiro(500).generar_interes().imprimir_cuentas()






# cuenta.hacer_deposito(100)

# CuentaBancaria.imprimir_cuentas()


