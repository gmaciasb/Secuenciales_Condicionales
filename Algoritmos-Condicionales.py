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
    
# Punto 4: Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.

l_puntos = int(input('Digite los puntos que emitio la fabrica el lunes: '))
m_puntos = int(input('Digite los puntos que emitio la fabrica el martes: '))
mi_puntos = int(input('Digite los puntos que emitio la fabrica el miercoles: '))
j_puntos = int(input('Digite los puntos que emitio la fabrica el jueves: '))
v_puntos = int(input('Digite los puntos que emitio la fabrica el viernes: '))

tpuntos = (l_puntos + m_puntos + mi_puntos + j_puntos + j_puntos + v_puntos) / 5
if tpuntos > 170:
        gl_puntos = float(input('Digite las ganancias del lunes: '))
        gm_puntos = float(input('Digite las ganancias del martes: '))
        gmi_puntos = float(input('Digite las ganancias del miercoles: '))
        gj_puntos = float(input('Digite las ganancias del jueves: '))
        gv_puntos = float(input('Digite los puntos que emite el viernes: '))
        totalg = (gl_puntos + gm_puntos + gmi_puntos + gj_puntos + gv_puntos)
        multa = totalg * 0.5
        print(f'El dinero perdido es de : $ {multa}')
else:
    print('No debe pagar multa')
    
# Punto 5: Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.    
        
vcars = float(input('Digite el costo del carro: $ '))
incremento = float(input('Digite el incremento del terreno: $ '))
devalu = float(input('Digite la devaluación del carro: $ '))
m_incremento = incremento / 2
if  devalu > m_incremento:
    print('Debe comprar el terreno')
else:
    print('Debe comprar el carro')    
    
# Punto 6:

n_compu = int(input('Digite la cantidad de computadoras que desea comprar: '))
valor_compu = 11000
costo = valor_compu * n_compu
if n_compu < 5:
    descuento = costo * 0.1
    totalp = costo - descuento
    print(f'El valor a pagar es: $ {totalp}')
elif n_compu >= 5 and n_compu < 10:
    descuento = costo * 0.2
    totalp = costo - descuento
    print(f'El valor a pagar es: $ {totalp}')  
else:
    descuento = costo * 0.4
    totalp = costo - descuento
    print(f'El valor a pagar es: $ {totalp}')    
    
# Punto 7:
precio = float(input('Digite el precio del producto a comprar: $ '))
marca = str(input('Digite la marca del producto: '))
if precio >= 2000:
    descuento = precio * 0.1
    total = precio - descuento 
    if marca == "NOSY":
        desc_dos = precio * 0.05
        tot_dos = total - desc_dos
        iva = precio * 0.16
        totalp = tot_dos + iva
        print(f'El precio con descuento de marca e iva es: {totalp}')
    else:
        iva = precio * 0.16
        totalp = tot_dos + iva
        print(f'El precio con descuento de marca e iva es: {totalp}')
else:
    if marca == "NOSY":
        desc_dos = precio * 0.05
        tot_dos = precio - desc_dos
        iva = precio * 0.16
        totalp = tot_dos + iva
        print(f'El precio con descuento de marca e iva es: {totalp}')
    else:
        iva = precio * 0.16
        totalp = tot_dos + iva
        print(f'El precio con descuento de marca e iva es: {totalp}') 
        
# Punto 9:

pri_numero = float(input('Digite el primer numero: '))
seg_numero = float(input('Digite el segundo numero: '))
if pri_numero == seg_numero:
    multi = pri_numero * seg_numero
    print(f'El resultado es: {multi}')
elif pri_numero > seg_numero:
     rest = pri_numero - seg_numero
     print(f'El resultado es: {rest}')
else:
     sum = pri_numero + seg_numero
     print(f'El mayor es el numero: {sum}')
     
    
# Punto 10: Leer tres números diferentes e imprimir el número mayor de los
# tres.

pri_numero = float(input('Digite el primer numero: '))
seg_numero = float(input('Digite el segundo numero: '))
ter_numero = float(input('Digite el tercer numero: '))
if pri_numero > seg_numero:
    if pri_numero > ter_numero:
        print(f'El mayor es el numero: {pri_numero}')
    else:
        print(f'El mayor es el numero: {ter_numero}')
else:
    if seg_numero > ter_numero:
        print(f'El mayor es el numero: {seg_numero}')
    else:
        print(f'El mayor es el numero: {ter_numero}')  