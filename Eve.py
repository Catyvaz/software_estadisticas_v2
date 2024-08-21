'''
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


def menu():
    while True:
        print("\nSeleccion de funcion a probar:")
        print("1. Calcular Factorial")
        print("2. Calcular Combinatorio")
        print("3. Calcular Probabilidad Binomial")
        print("4. Calcular Probabilidad Hipergeométrica")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            n = int(input("Ingrese el valor de n: "))
            print(f"Factorial de {n} es: {factorial(n)}")

        elif opcion == "2":
            n = int(input("Ingrese el valor de n: "))
            k = int(input("Ingrese el valor de k: "))
            print(f"Combinatorio C({n},{k} es: {combinatorio(n,k)})")

        elif opcion == "3":
            n = int(input("Ingrese el número de ensayos (n): "))
            p = float(input("Ingrese la probabilidad de éxito (p): "))
            k = int(input("Ingrese el número de éxitos deseados (k): "))
            print(f"Probabilidad Binomial P(X = {k}) es: {probabilidad_binomial(n,p,k)}")

        elif opcion == "4":
            N = int(input("Ingrese el tamaño de la población (N): "))
            K = int(input("Ingrese el número de éxitos en la población (K): "))
            n = int(input("Ingrese el tamaño de la muestra (n): "))
            k = int(input("Ingrese el número de éxitos en la muestra (k): "))
            print(f"Probabilidad Hipergeométrica es: {probabilidad_hipergeometrica(N,K,n,k)}")

        elif opcion == "5":
            print("Creo que anda todo")
            break

        else:
            print("Opcion no valida. Intente de nuevo.")

menu()   

                         '''

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
         print("Error: K(éxitos en la poblacion) no puede ser mayor que N(tamaño de la población).")
         K = int(input(f"Ingrese un valor para K (menor o igual  a {N}): "))
     while k > n:
         print("Error: k(éxitos en la muestra) no puede ser mayor que n(tamaño de muestra).")
         k = int(input(f"Ingrese un valor para k (menor o igual a {n}): "))
     while k > K:
         print("Error: k(éxitos en la muestra) no puede ser mayor que K(éxitos en la poblacion).")
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
def val_numeros(mensaje, entero=True,):
    while True:
        ingreso = input(mensaje)
        try:
            if entero:
                valor = int(ingreso)
                if valor < 0:
                    print("Debe ingresar valores mayores o iguales a 0")
                else:
                    return valor
            else:
                valor = float(ingreso)
                if valor < 0:
                    print("Debe ingresar valores mayores o iguales a 0")
                else:
                    return valor
        except ValueError:
            print("Ingrese valores numéricos enteros")
            

n = val_numeros("Ingrese el número de ensayos (n): ")
p = val_numeros("Ingrese la probabilidad de éxito (p): ", entero=False)
k = val_numeros("Ingrese el número de éxitos deseados (k): ")
print(f"Probabilidad Binomial P(X = {k}) es: {probabilidad_binomial(n, p, k)}")

N = val_numeros("Ingrese el tamaño de la población (N): ")
K = val_numeros("Ingrese el número de éxitos en la población (K): ")
n = val_numeros("Ingrese el tamaño de la muestra (n): ")
k = val_numeros("Ingrese el número de éxitos en la muestra (k): ")
print(f"Probabilidad Hipergeométrica es: {probabilidad_hipergeometrica(N, K, n, k)}")