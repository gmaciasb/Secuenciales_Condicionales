# Punto 1: Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

num_camisas = int(input('Digite la cantidad de camisas a comprar: '))
valor_camisas = int(input('Digite el valor de las camisas: '))
valor_sindesc = valor_camisas * num_camisas
if num_camisas >= 3:
    descuento = valor_sindesc * 0.3
    valor_pagar = valor_sindesc - descuento
    print(f'El valor a pagar es: $ {valor_pagar}')
else:
    descuento = valor_sindesc * 0.1
    valor_pagar = valor_sindesc - descuento
    print(f'El valor a pagar es: $ {valor_pagar}')

# Punto 2: En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta. 

valor_compra = float(input('Digite el valor de la compra: '))
num_azar = float(input('Digite el numero escogido: '))
if num_azar < 74:
    descuento = valor_compra * 0.15
    vpagar =  valor_compra - descuento
    print(f'El valor a pagar es de: $ {vpagar}') 
else: 
    descuento = valor_compra * 0.2
    vpagar =  valor_compra - descuento
    print(f'El valor a pagar es de: $ {vpagar}')

# Punto 3: Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que consiste
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al 
# cliente.       
monto_f = float(input('Digite el monto por el que se efectuo la finanza: '))
if monto_f < 50000:
    v_pagar = monto_f * 0.03
    print(f'El valor a pagar es de: $ {v_pagar}')
else:
    v_pagar = monto_f * 0.02
    print(f'El valor a pagar es de: $ {v_pagar}')
    
