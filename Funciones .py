from math import e


#Funcion para calcular el factorial de un num n
def factorial(n):
    #validamos datos dentro del bucle
    while n < 0:
        print("Error: n debe ser un numero entero positivo")
        n = int(input("Ingrese un número para calcular el factorial"))
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

#funcion para calcular el num comb.
def combinatorio(n,k):
    #validamos que k(éxitos de muestra) no sea mayor que n(tamaño de la muestra)
    while k > n:
        print("Error. k no puede ser mayor que n")
        k = int(input(f"Ingrese un valor para k (menor o igual a {n}): "))
    #calculamos num comb usando formula: n! / k! * (n - k)!
    return factorial(n) // (factorial(k) * factorial(n - k))
    #usamos la funcion factorial para calcular los factoriales necesarios.

#funcion para calcular la probabilidad binomial
def probabilidad_binomial(n,p,k):
    #Validacion de datos
    while p < 0 or p > 1:
        print("Error. La probabilidad p debe estar entre 0 y 1")
        p = float(input("Ingrese la probabilidad de éxito p (entre 0 y 1): "))

    #Validamos que el núm de éxitos k no sea mayor al núm de ensayos n. 
    while k > n:
        print("Error: El número de éxitos k no puede ser mayor que el número de ensayos n.")
        k = int(input(f"Ingrese un valor para k (menor o igual a {n}): "))

    #calculamos la probabilidad combinatoria multiplicada por la probabilidad p elevada a la k
    #y la probabilidad de fracaso (1 - p) elevada a n - k
    comb = combinatorio(n,k)    
    prob = comb * (p ** k) * ((1 - p) ** (n - k))
    #se redondea la prob a 4 decimales
    return round(prob,4)
    #num de ensayos(n)
    #probabilidad de exitos(p)
    #num de exitos(k)


#funcion para calcular probabilidad hipergeometrica
def probabilidad_hipergeometrica(N,K,n,k):
     while K > N:
         print("Error: K no puede ser mayor que N.")
         K = int(input(f"Ingrese un valor para K (menor o igual  a {N}): "))
     while k > n:
         print("Error: k no puede ser mayor que n.")
         k = int(input(f"Ingrese un valor para k (menor o igual a {n}): "))
     while k > K:
         print("Error: k no puede ser mayor que K.")
         k = int(input(f"Ingrese un valor para k (menor o igual a {K}): "))        
    #calculamos C(K,k) que es el num de formas de elegir k éxitos de k éxitos en la poblacion     
     comb1 = combinatorio(K,k)
     #calculamos C(N-K, n -k) que es el num de formas de elegir los fracasos de los no-exitos en la poblacion
     comb2 = combinatorio(N - K, n - k)
     #calculamos C(N,n) que es el num de formas de elegir n elementos de una poblacion de tamaño N
     comb3 = combinatorio(N,n)

     while comb3 == 0:
         print("Error: Division por cero. Verifica los valores de N y n.")
         N = int(input("Ingrese el tamaño de la población N: "))
     #calculamos la probabilidad usando la formula de la probabilidad hipergeometrica
     prob = (comb1 * comb2) / comb3
     return round(prob, 4)
     #tamaño de la poblacion(N)
     #num de exitos en la poblacion(K)
     #tamaño de muestra(n)
     #num de exitos en la muestra(k)

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
        limiteI = val_numeros("Que ocurra desde \nx = ", entero = True, simple = True)
        limiteF = val_numeros("Hasta \nx = ", entero = True, simple = True)
        resultado = 0
        for i in range(limiteI, limiteF + 1):
            resultado += Poisson(cantidad, i)
        print(f"El resultado es: ", round(resultado, 5))

def calcular_curtosis(datos):
    n = len(datos)
    media = sum(datos) / n
    varianza = sum((x - media) ** 2 for x in datos) / n
    desviacion_estandar = varianza ** 0.5

    curtosis = sum((x - media) ** 4 for x in datos) / (n * desviacion_estandar ** 4)
    
    # Ajuste de Fisher para obtener la curtosis con sesgo corregido
    curtosis_fisher = ((n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))) * curtosis - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    return curtosis_fisher
    
datos = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
curtosis = calcular_curtosis(datos)
if curtosis > 0:
    tipocurtosis= "Leptocúrtica"
if curtosis == 0:
    tipocurtosis = "Mezzocúrtica"
if curtosis < 0:
    tipocurtosis= "Platicúrtica"

print(f"El coeficiente de curtosis es: {curtosis} y según su resultado es: " , tipocurtosis)