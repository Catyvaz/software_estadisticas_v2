from math import e

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

def validar_noneg(valor):
    if valor < 0:
        print("El valor debe ser mayor a 0.")
        break

def Poisson(lamda, x):
    lamda = cantidad
    factorial_x = factorial(x)    
    resultado = ((e ** (-lamda)) * (lamda ** x)) / factorial_x
    
    return round(resultado, 6)

while True:
    print("")
    print("Poisson, número de ocurrencias de un evento en un intervalo")
    print("Recuerde que la probabilidad de ocurrencia debe ser un numero entero mayor que 0")
    valor = int(input("Cuantas veces debe ocurrir el evento? \n Un caso = 1 \n Varios casos = 2 \n --> "))
    if valor == 1:
        cantidad = float(input("Promedio de ocurrencias en x intervalo: "))
        usuario_espera = int(input("¿Qué probabilidad quiere calcular?\n x = "))
        validar_noneg(cantidad)
        validar_noneg(usuario_espera)
        print(f"El resultado es: ", Poisson(cantidad, usuario_espera))

    elif valor == 2:
        print("Ingrese la probabilidad de ocurrencia de cuales casos quiere calcular, separandolos con un espacio y luego precionando enter. \nejemplo: 1 2 3 4 (enter)")
        limite = list(input("Ocurrencias \nx = "))
        cantidad = float(input("Promedio de ocurrencias en x intervalo: "))
        resultado = 0
        for i in range(limite):
            resultado += Poisson(cantidad, i)
        print(f"El resultado es: ", round(resultado, 6))