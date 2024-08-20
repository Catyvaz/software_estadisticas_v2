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

def Poisson(lamda, x):
    factorial_x = factorial(x)    
    resultado = ((e ** (-lamda)) * (lamda ** x)) / factorial_x
    
    return round(resultado, 6)

def numero(valor):
    if valor.isdigit():
        float(valor)
    else:
        print("Debe ingresar valores numéricos")
        return 0


while True:
    print("")
    print("Poisson, número de ocurrencias de un evento en un intervalo")
    print("Recuerde que la probabilidad de ocurrencia debe ser un numero entero mayor que 0")
    cantidad = input("Promedio de ocurrencias en x intervalo: ")
    cantidad = float(cantidad) if cantidad.isdigit() else print("Debe ingresar valores numéricos")
    valor = int(input("Cuantas veces debe ocurrir el evento? \n Un caso = 1 \n Varios casos = 2 \n --> "))
    if valor == 1:
        usuario_espera = int(input("¿Qué probabilidad quiere calcular?\n x = "))
        print(f"El resultado es: ", Poisson(cantidad, usuario_espera))
    elif valor == 2:
        print("Ingrese la probabilidad de ocurrencia de cuales casos quiere calcular, separandolos con un espacio y luego precionando enter. \nejemplo: 1 2 3 4 (enter)")
        limiteI = int(input("Que ocurra desde \nx = "))
        limiteF = int(input("Hasta \nx = "))
        resultado = 0
        for i in range(limiteI, limiteF + 1):
            resultado += Poisson(cantidad, i)
        print(f"El resultado es: ", round(resultado, 5))