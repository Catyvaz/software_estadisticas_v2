#Funcion para calcular el factorial de un num n
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

#funcion para calcular el num comb.
def combinatorio(n,k):
    #calculamos num comb usando formula: n! / k! * (n - k)!
    return factorial(n) // (factorial(k) * factorial(n - k))
    #usamos la funcion factorial para calcular los factoriales necesarios.

#funcion para calcular la probabilidad binomial
def probabilidad_binomial(n,p,k):
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
    #calculamos C(K,k) que es el num de formas de elegir k éxitos de k éxitos en la poblacion
     comb1 = combinatorio(K,k)
     #calculamos C(N-K, n -k) que es el num de formas de elegir los fracasos de los no-exitos en la poblacion
     comb2 = combinatorio(N - K, n - k)
     #calculamos C(N,n) que es el num de formas de elegir n elementos de una poblacion de tamaño N
     comb3 = combinatorio(N,n)
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