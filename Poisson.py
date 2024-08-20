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

#Esta función evalua que los valores que se ingresen sean correctos.
#Se evalua que los que se ingrese sea del tipo numerico, y en caso de no serlo se avisa y se pide que ingrese nuevamente un valor.
#Se ingresa el mensaje que verá el usuario, se condiciona si tiene que ser entero el valor y con simple si se elige entre dos opciones o no.
def val_numeros(mensaje, entero = True, simple = True):
    while True:
        ingreso = input(mensaje)
        if entero:
            try:
                valor = int(ingreso)
                if valor < 0:
                    print("Debe ingresar valores mayores o iguales a 0")
                else:
                    if simple:
                        return valor
                    else:
                        if 0 < valor & valor < 3:
                            return valor
                        else:
                            print("Seleccione una opción válida")
            except:
                print("Ingrese valores numéricos enteros")
        else:
            try:
                valor = float(ingreso)
                if valor < 0:
                    print("Debe ingresar valores mayores o iguales a 0")
                else:
                    return valor
            except:
                print("Ingrese valores numéricos")


while True:
    print("")
    print("Poisson, número de ocurrencias de un evento en un intervalo")
    print("Recuerde que la probabilidad de ocurrencia debe ser un numero entero mayor que 0")
    #Se ingresa el valor de lamda, o lo que se espera
    cantidad = val_numeros("Promedio de ocurrencias en x intervalo: ", entero = False, simple = True)
    #Se pregunta si es la ocurrencia de un solo caso o de varios.
    valor = val_numeros("Cuantas veces debe ocurrir el evento? \n Un caso = 1 \n Varios casos = 2 \n --> ", entero = True, simple = False)
    
    if valor == 1:
        #Se evalua una sola posibilidad. ejemplo, que llegue 1 sola persona.
        usuario_espera = val_numeros("¿Qué probabilidad quiere calcular?\n x = ", entero = True, simple = True)
        print(f"El resultado es: ", Poisson(cantidad, usuario_espera))
    elif valor == 2:
        #Se evaluan varias probabilidades. ejemplo, que lleguen 2 o 3 personas
        print("Ingrese la probabilidad de ocurrencia de cuales casos quiere calcular. ejemplo; que ingresen desde 2 hasta 4 personas.")
        while True:
            limiteI = val_numeros("Que ocurra desde \nx = ", entero = True, simple = True)
            limiteF = val_numeros("Hasta \nx = ", entero = True, simple = True)
            if limiteI > limiteF:
                print("El valor de inicio debe ser menor que el de final")
            else:
                break
        resultado = 0

        for i in range(limiteI, limiteF + 1):
            resultado += Poisson(cantidad, i)
        print(f"El resultado es: ", round(resultado, 5))