# Punto 1: Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

persona_uno = float(input('Digite el valor de inversión de la persona uno: '))
persona_dos = float(input('Digite el valor de inversión de la persona dos: '))
persona_tres = float(input('Digite el valor de inversión de la persona tres: '))
inversion_total = persona_uno + persona_dos + persona_tres
porcentaje_puno = (persona_uno / inversion_total)*100
porcentaje_pdos = (persona_dos / inversion_total)*100
porcentaje_ptres = (persona_tres / inversion_total)*100
print(f'El porcentaje de inversión para la persona uno fue de: {porcentaje_puno} %')
print(f'El porcentaje de inversión para la persona dos fue de: {porcentaje_pdos} %')
print(f'El porcentaje de inversión para la persona tres fue de: {porcentaje_ptres} %')
print(f'la inversión total es: {inversion_total}')

# Punto 2: Una empresa paga a sus empleados además del sueldo base una
# bonificación especial de $80.000 por cada hijo. Realice un programa
# en Java que determine el monto de la bonificación y el monto total a
# pagar al trabajador.

sueldo_base = float(input('Digite el sueldo base del empleado: '))
num_hijos = int(input('Digite el numero de hijos del empleado: '))
boniesp = 80000
valor_boni = num_hijos * boniesp
m_total = sueldo_base + valor_boni
print(f'El monto de la bonificación es: $ {valor_boni}')
print(f'El monto total a pagar es: $ {m_total}')

# Punto 3: Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.


saldo_ini = float(input('Digite el saldo inicial del ahorrador: $ '))
v_interes = 0.015
interes = saldo_ini * v_interes
saldo_final = saldo_ini + interes
print(f'El saldo final del ahorrador es: $ {saldo_final}')

# Punto 4: Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
# cliente debe dar una cuota inicial del 35%y el resto lo paga en 12
# cuotas. Determine el valor a pagar por cuota inicial y el monto de
# cada cuota.

cant_metro = float(input('Digite la cantidad de metros a comprar: $ '))
valor_tmetros = cant_metro * 80000
vcuota_ini = valor_tmetros * 0.35
valor_rest = (valor_tmetros - vcuota_ini)/12
print(f'El valor a pagar de la cuota iniciales: $ {vcuota_ini}')
print(f'El monto de las cuotas es: $ {valor_rest}')

# Punto 5: Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# programa en Java que determine el monto de cada descuento y el
# monto total a pagar al trabajador.

sueldo_base = float(input('Digite el sueldo base del trabajador: '))
desc_ppublic = sueldo_base * 0.01
desc_ssocial = sueldo_base * 0.04
desc_sforzoso = sueldo_base * 0.5
desc_cajahorro = sueldo_base * 0.05
total_desc = desc_ppublic + desc_ssocial + desc_sforzoso + desc_cajahorro
total_pagar = sueldo_base - total_desc
print(f'El descuento por ley de politica pública es: $ {desc_ppublic}')
print(f'El descuento por seguro social es: $ {desc_ssocial}')
print(f'El descuento por  seguro forzoso es: $ {desc_sforzoso}')
print(f'El descuento por caja de ahorro: $ {desc_cajahorro}')
print(f'El monto total a pagar al trabajador es de: $ {total_pagar}')

# Punto 6: El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.

num_palabras = float(input('Digite la cantidad de palabras: '))
num_centimetros = float(input('Digite la cantidad de centimetros: '))
num_colores = float(input('Digite la cantidad de colores: '))
v_palabra = num_palabras * 20000
v_centimetros = num_centimetros * 15000
v_colores = num_colores * 25000
vtotal = v_palabra + v_centimetros + v_colores
print(f'El valor del clasificado es: $ {vtotal}')

# Punto 7: Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un programa en Java que determine el monto
# del bono a pagar a un trabajador que tiene varios años en la empresa.

sueldo_base = float(input('Digite el sueldo base del trabajador: '))
cant_años = float(input('Digite la cantidad de años en la empresa: '))
if cant_años == 1:
    bono_uno = sueldo_base + 100000
    print(f'El sueldo del trabajador es: {bono_uno}')
else:
    bono = 120000 * cant_años
    sueldot = sueldo_base + bono
    print(f'El sueldo del trabajador es: {sueldot}')
    
# Punto 8: Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.

horas_trabajadas = float(input('Digite la cantidad de horas trabajadas: '))
valorh = horas_trabajadas * 20000
descuento = valorh * 0.05
vtotal = valorh - descuento
print(f'El monto de descuento es: $ {descuento}')
print(f'El monto total a pagar al trabajador es de: $ {vtotal}')
    
