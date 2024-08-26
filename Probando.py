def factorial(m):
    # Validamos datos dentro del bucle
    while m < 0:
        print("Error: m debe ser un número entero positivo")
        m = int(input("Ingrese un número para calcular el factorial: "))
    # Si m es 0 o 1, el factorial es 1
    if m == 0 or m == 1:
        return 1
    # Inicia el resultado en 1
    resultado = 1
    # Bucle para multiplicar todos los números desde 2 hasta m
    for i in range(2, m + 1):
        # Multiplica el resultado por i en cada iteración
        resultado *= i
    # Retorna el factorial calculado    
    return resultado

def combinatorio(m, n):
    while n < 0 or m < 0:
        print("Error: m y n deben ser números enteros no negativos")
        m = int(input("Ingrese un valor para m (número entero no negativo): "))
        n = int(input("Ingrese un valor para n (número entero no negativo): "))
    # Validamos que n (éxitos de muestra) no sea mayor que m (tamaño de la muestra)
    if n > m:
        print((f"Error. n ({n}) no puede ser mayor que m ({m})"))
        return None
    # Calculamos combinatorio usando la fórmula: m! / (n! * (m - n)!)
    return factorial(m) // (factorial(n) * factorial(m - n))

def probabilidad_binomial(n, p, limiteI, limiteS):
    while p < 0 or p > 1:
        print("Error. La probabilidad p debe estar entre 0 y 1.")
        p = float(input("Ingrese la probabilidad de éxito p (entre 0 y 1): "))

    while limiteI > limiteS or limiteI < 0 or limiteS > n:
        print("Error. Los límites deben estar en el rango válido y el límite inferior debe ser menor o igual al límite superior.")
        limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
        limiteS = int(input("Ingrese el valor máximo de éxitos k: "))    
    #calculamos la probabilidad combinatoria de num de ensayos(n) y num de úxitos (k) #
    # multiplicada por la probabilidad de éxitos (p) elevada al num de úxitos (k)
    #y la probabilidad de fracaso (1 - p) elevada a n - k
    resultado = 0
    for k in range(limiteI, limiteS + 1):
        comb = combinatorio(n, k)
        prob = comb * (p ** k) * ((1 - p) ** (n - k))
        print(f"La probabilidad binomial para k = {k} es: {round(prob, 4)}")
        resultado += prob
    return round(resultado, 4)
    

# Función para calcular la probabilidad hipergeométrica
def probabilidad_hipergeometrica(N, M, n, limiteI, limiteS):
    while M > N:
        print("Error: M (éxitos en la población) no puede ser mayor que N (tamaño de la población).")
        M = int(input(f"Ingrese un valor para M (menor o igual a {N}): "))
    while n > N:
        print("Error: n (tamaño de la muestra) no puede ser mayor que N.")
        n = int(input(f"Ingrese un valor para n (menor o igual a {N}): "))
    while limiteI > limiteS or limiteI < 0 or limiteS > n or limiteS > M:
        print("Error. Los límites deben estar en el rango válido y el límite inferior debe ser menor o igual al límite superior.")
        limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
        limiteS = int(input("Ingrese el valor máximo de éxitos k: "))

    
    resultado = 0
    comb3 = combinatorio(N, n)
    
    if comb3 is None:
        print("Error: División por cero. Verifica los valores de N y n. \nSUCESO IMPOSIBLE \nRegresando al menú...")
        return 0  # Retorna 0 si hubo un error en combinatorio

    for k in range(limiteI, limiteS + 1):    
        comb1 = combinatorio(M, k)
        if comb1 is None:
            print(f"Error al calcular combinatorio para M, k = {k}. \nSUCESO IMPOSIBLE \nRegresando al menú...")
            return 0  # Retorna 0 si hubo un error en combinatorio

        comb2 = combinatorio(N - M, n - k)
        if comb2 is None:
            print(f"Error al calcular combinatorio para N - M, n - k = {k}. \nSUCESO IMPOSIBLE \nRegresando al menú...")
            return 0  # Retorna 0 si hubo un error en combinatorio

        prob = (comb1 * comb2) / comb3
        print(f"La probabilidad hipergeométrica para k = {k} es: {round(prob, 4)}")
        resultado += prob

    return round(resultado, 4)

    
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular probabilidad binomial")
        print("2. Calcular probabilidad hipergeométrica")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            n = int(input("Ingrese el número de ensayos (n): "))
            p = float(input("Ingrese la probabilidad de éxito (p): "))
            limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
            limiteS = int(input("Ingrese el valor máximo de éxitos k: "))
            print(f"Probabilidad Binomial en el rango [{limiteI}, {limiteS}] es: {probabilidad_binomial(n, p, limiteI, limiteS)}")
        
        elif opcion == "2":
            N = int(input("Ingrese el tamaño de la población (N): "))
            M = int(input("Ingrese el número de éxitos en la población (M): "))
            n = int(input("Ingrese el tamaño de la muestra (n): "))
            limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
            limiteS = int(input("Ingrese el valor máximo de éxitos k: "))
            print(f"Probabilidad Hipergeométrica en el rango [{limiteI}, {limiteS}] es: {probabilidad_hipergeometrica(N, M, n, limiteI, limiteS)}")
        
        elif opcion == "3":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

menu()


'''


def probabilidad_binomial():
    """
    Solicita al usuario los parámetros necesarios y calcula la probabilidad binomial
    para un rango de valores k según lo indicado por el usuario.
    """
    n = int(input("Ingrese el número de ensayos n: "))
    p = float(input("Ingrese la probabilidad de éxito p (entre 0 y 1): "))

    # Validación de la probabilidad
    while p < 0 or p > 1:
        print("Error. La probabilidad p debe estar entre 0 y 1")
        p = float(input("Ingrese la probabilidad de éxito p (entre 0 y 1): "))

    # Ingresar el rango de valores para k
    limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
    limiteF = int(input("Ingrese el valor máximo de éxitos k: "))

    while limiteI > limiteF or limiteI < 0 or limiteF > n:
        print("Error. El límite inferior debe ser menor o igual al límite superior.")
        limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
        limiteF = int(input("Ingrese el valor máximo de éxitos k: "))

    def calcular_probabilidad(k):
        comb = combinatorio(n, k)
        return comb * (p ** k) * ((1 - p) ** (n - k))

    resultado = 0
    for k in range(limiteI, limiteF + 1):
        prob = calcular_probabilidad(k)
        print(f"La probabilidad binomial para k = {k} es: {round(prob, 4)}")
        resultado += prob
    
    print(f"La probabilidad binomial total en el rango [{limiteI}, {limiteF}] es: {round(resultado, 4)}")

def probabilidad_hipergeometrica():
    N = int(input("Ingrese el tamaño de la población (N): "))
    M = int(input("Ingrese el número de éxitos en la población (K): "))
    n = int(input("Ingrese el tamaño de la muestra (n): "))

    while M > N:
        print("Error: M (éxitos en la población) no puede ser mayor que N (tamaño de la población).")
        M = int(input(f"Ingrese un valor para K (menor o igual a {N}): "))
    while n > N:
        print("Error: n (tamaño de la muestra) no puede ser mayor que N.")
        n = int(input(f"Ingrese un valor para n (menor o igual a {N}): "))

    limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
    limiteF = int(input("Ingrese el valor máximo de éxitos k: "))

    while limiteI > limiteF or limiteI < 0 or limiteF > n or limiteF > M:
        print("Error. El límite inferior debe ser menor o igual al límite superior y ambos deben estar en el rango válido.")
        limiteI = int(input("Ingrese el valor mínimo de éxitos k: "))
        limiteF = int(input("Ingrese el valor máximo de éxitos k: "))

    resultado = 0
    for k in range(limiteI, limiteF + 1):
        comb1 = combinatorio(M, k)
        comb2 = combinatorio(N - M, n - k)
        comb3 = combinatorio(N,n)
        while comb3 == 0:
         print("Error: Division por cero. Verifica los valores de N y n.")
         N = int(input("Ingrese el tamaño de la población N: "))
        prob = (comb1 * comb2) / comb3
        print(f"La probabilidad hipergeométrica para k = {k} es: {round(prob, 4)}")
        resultado += prob

    print(f"La probabilidad hipergeométrica total en el rango [{limiteI}, {limiteF}] es: {round(resultado, 4)}")


def menu():
    while True:
        print("\nSelección de función a probar:")
        print("1. Calcular Factorial")
        print("2. Calcular Combinatorio")
        print("3. Calcular Probabilidad Binomial")
        print("4. Calcular Probabilidad Hipergeométrica")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            m = int(input("Ingrese el valor de m: "))
            print(f"Factorial de {m} es: {factorial(m)}")

        elif opcion == "2":
            m = int(input("Ingrese el valor de m: "))
            n = int(input("Ingrese el valor de n: "))
            print(f"Combinatorio C({m},{n}) es: {combinatorio(m, n)}")

        elif opcion == "3":
            probabilidad_binomial()

        elif opcion == "4":
            probabilidad_hipergeometrica()    

menu()
'''

