# esta sección será para aprender el uso de variable 
"""nombre = 1234 # un comentario con tres comillas es un comentario de varias líneas
print (nombre)  # el codigo es secuencial, se ejecuta de arriba hacia abajo
print (type(nombre)) 
variable = 123456
print (type(variable)) #int = entero y float = decimal
variable = 123.456
print (type(variable)) #int = entero y float = decimal
a = "Diego Pinto" # string = cadena de texto
monto = 100
cobrarle = True
monto_a_cobrar = monto * cobrarle
print (monto_a_cobrar)""" # True = 1 y False = 0 # no puedo sumar un string con un int, pero si puedo multiplicar un string por un int
# un string si se puede sumar con otro string, y esto es una concatenación.
# la multiplicación si se puede hacer con un string y un int, pero no con un string y un float

"""andrea = 25.25
carlitos = andrea
andrea = 14.23
carlitos = carlitos + andrea
print (round(carlitos, 2))""" 

"""compras = 123.5
compras = compras + 100   
print (compras)"""

"""saldo = 10
saldo = saldo - 3
recargo =saldo * 0.5
print (saldo,recargo)"""

compra = 27.35
usuario = "Aracely"
texto = " le compró a Carlitos "
print (usuario,texto ,compra) # no puedo sumar string con float, pero dos string
# puedo combinar tipos de variables usando f-string
print(f"{usuario}{texto}{compra}")
print (f"Aracely le compró a Carlitos ${round(compra*1.10, 2)}") # round es para redondear el resultaod a n decimales, los parentesis se llaman argumentos


