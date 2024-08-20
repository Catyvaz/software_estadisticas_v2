




while True:
    print("**********************************************")
    print("****      ESTADÍSTICA DESCRIPTIVA Y       ****")
    print("****      PROBABILIDAD Y ESTADÍSTICA      ****")
    print("**********************************************")

    print("Seleccione el módulo que desea utilizar:")
    print("1 = Estadística Descriptiva")
    print("2 = Probabilidad y Estadística")
    print("3 = Salir")
    seleccion = input("Ingrese el número de su opción: ")




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