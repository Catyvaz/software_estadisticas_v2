from math import e

"""
def factorial(n):
    #si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    #inicia el resultado en 1
    resultado = 1
    #bucle para multiplicar todos los num desde 2 hasta n
    for i in range(2, n + 1):
        #multiplica el resultado por i en cada interacion.
        resultado *= i 
     #retorna el factorial calculado    
    return resultado
"""
def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

def Poisson(lamda, x):
    lamda = cantidad
    factorial_x = factorial(x)    
    resultado = ((e ** (-lamda)) * (lamda ** x)) / factorial_x
    
    return round(resultado, 6)

while True:
    print("")
    print("Poisson, número de ocurrencias de un evento en un intervalo")
    valor = int(input("Cuantos valores de probabilidad? \n Un solo valor = 1 \n Varios valores = 2 \n --> "))
    if valor == 1:
        cantidad = float(input("Lo que se espera: "))
        usuario_espera = float(input("¿Qué probabilidad quiere calcular?: "))

        print(f"El resultado es: ", Poisson(cantidad, usuario_espera))

    elif valor == 2:
        limite = int(input("x o más: "))
        cantidad = float(input("Lo que se espera: "))
        resultado = 0
        for i in range(limite):
            resultado += Poisson(cantidad, i)
        print(f"El resultado es: ", round(1 - resultado, 6))