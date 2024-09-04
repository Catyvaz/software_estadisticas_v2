from Funciones import *
from estadisticas_descriptivas import *

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
    
    if seleccion == "1":
        # Estas tres variables serán las utilizadas a lo largo de todo el programa y las que recibirán las funciones
        conteo = {} # Diccionario con los números y sus respectivas frecuencias
        conteo_ordenado = {} # Ordenado de forma ascendente
        nros = [] # Lista con los números ingresados por el usuario
        nros = input_float_list("Ingrese los datos separados por espacios: ")

        for i in nros: # Cuenta la frecuencia absoluta de cada número
                    if i in conteo:
                        conteo[i] += 1
                    else:
                        conteo[i] = 1

        claves_ordenadas = list(conteo.keys()) # Crea una lista con las claves del diccionario 'conteo'
        claves_ordenadas.sort()
        for clave in claves_ordenadas:
            conteo_ordenado[clave] = conteo[clave] # A cada número le asigna su frecuencia

        while True: # Mientras no se rompa el ciclo
            opcion_a = input_int("""\nSeleccione qué tipo de medida quiere calcular:
                            
            0 = Salir
            1 = Medidas de posición         
            2 = Medidas de dispersión
            3 = Tabla de frecuencias  
                                                
        Opción elegida: """)

            if opcion_a == 0:
                print("Cerrando aplicación")
                break # Se rompe el ciclo while

            elif opcion_a == 1:

                opcion_b = input_int("""\nSeleccione qué medida de posición quiere calcular:
                            
            0 = Volver
            1 = Media         
            2 = Mediana
            3 = Moda
            4 = Cuartiles                          
                                                
        Opción elegida: """)
                
                if opcion_b == 1:

                    res_media = media(nros) 
                    print("\nMedia:", res_media)
                    input("Presione enter para continuar ")

                elif opcion_b == 2:

                    res_mediana = mediana(nros)
                    print("\nMediana:", res_mediana)
                    input("Presione enter para continuar ")

                elif opcion_b == 3:

                    res_moda, max_frecuencia = moda(conteo, conteo_ordenado)
                    print("")

                    if res_moda == None: # Si no hay moda
                        print(f"El conjunto no tiene moda, todos los valores tienen frecuencia {max_frecuencia}")
                        input("Presione enter para continuar ")
                    else:
                        for valor in res_moda:
                            print("Moda:", valor)

                        print("\nFrecuencia:", max_frecuencia)
                        input("Presione enter para continuar ")
                
                elif opcion_b == 4:

                    res_Q1, res_Q2, res_Q3 = cuartiles(nros)
                    print("\nQ1 (25%):", res_Q1)
                    print("Q2 (50%, mediana):", res_Q2)
                    print("Q3 (75%):", res_Q3)
                    input("Presione enter para continuar ")

                else:
                    print("Opción no válida, por favor seleccione una opción válida.")

            elif opcion_a == 2:

                opcion_b = input_int("""\nSeleccione qué medida de dispersión quiere calcular:
                            
            0 = Volver
            1 = Rango         
            2 = Varianza
            3 = Desviación estándar                       
                                                
        Opción elegida: """)
                
                if opcion_b == 1:
                    
                    res_rango = rango(nros)
                    print("\nRango:", res_rango)
                    input("Presione enter para continuar ")

                elif opcion_b == 2:
                    
                    res_varianza = varianza(nros)

                    if res_varianza:
                        print("\nVarianza:", res_varianza)
                    else:
                        print("\nEl conjunto no tiene varianza")
                    input("Presione enter para continuar ")

                elif opcion_b == 3:
                    
                    res_desviacion_estandar = desviacion_estandar(nros)

                    if res_desviacion_estandar:
                        print("\nDesviación estándar:", res_desviacion_estandar)
                    else:
                        print("\nEl conjunto no tiene desviación estándar")
                    input("Presione enter para continuar ")
                
                else:
                    print("Opción no válida, por favor seleccione una opción válida.")
            
            elif opcion_a == 3:

                # Se crean las columnas de la tabla
                tabla = "\nFrecuencias:" +\
                    "\n   Número  | fi  |   fri   |  fri%    |  Fi  |   Fri    |   Fri%" +\
                    "\n-------------------------------------------------------------------"
                print(tabla)

                filas = frecuencias(conteo_ordenado)
                for fila in filas:
                    print(fila) # Se imprime cada valor de la lista, o sea cada línea de la tabla

                input("\nPresione enter para continuar ")

            else:
                print("Opción no válida, por favor seleccione una opción válida.")
    elif seleccion == "2":
        print("Se eligió Probabilidad y Estadísticas")
        print("Seleccione qué distribución quiere calcular.")
        while True:
            print("\nSeleccion de funcion a probar:")
            print("1. Calcular Probabilidad Binomial")
            print("2. Calcular Probabilidad Hipergeométrica")
            print("3. Poisson.")
            print("4. Coeficiente de Curtosis")
            print("5. Normal o Gaussiana")
            print("6. Salir.")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("Probabilidad Binomial")
                n = val_numeros("Ingrese el número de ensayos (n): ", True, True)
                p = val_numeros("Ingrese la probabilidad de éxito (entre 0 y 1) (p): ", False, True)
                while p < 0 or p > 1:
                    print("Error. La probabilidad p debe estar entre 0 y 1.")
                    p = val_numeros("Ingrese la probabilidad de éxito (entre 0 y 1) (p): ", False, True)
                
                print("En caso de ser un solo caso, poner el mismo número en ambos limites")
                limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True, True)
                limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True, True)
                while limiteI > limiteS or limiteS > n:
                    print("Error. El límite inferior debe ser menor o igual al límite superior.")
                    limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True, True)
                    limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True, True)
                print(f"Probabilidad Binomial en el rango [{limiteI}, {limiteS}] es: {probabilidad_binomial(n, p, limiteI, limiteS)}")
            
            elif opcion == "2":
                print("Probabilidad Hipergeométrica")
                N = val_numeros("Ingrese el tamaño de la población (N): ", True, True)
                M = val_numeros("Ingrese el número de éxitos en la población (M): ", True, True)
                while M > N:
                    print("Error: M (éxitos en la población) no puede ser mayor que N (tamaño de la población).")
                    M = val_numeros(f"Ingrese un valor para M (menor o igual a {N}): ", True, True)
                n = val_numeros("Ingrese el tamaño de la muestra (n): ", True, True)
                while n > N:
                    print("Error: n (tamaño de la muestra) no puede ser mayor que N.")
                    n = val_numeros(f"Ingrese un valor para n (menor o igual a {N}): ", True, True)
                limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True, True)
                limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True, True)
                while limiteI > limiteS or limiteI < 0 or limiteS > n or limiteS > M:
                    print("Error. El límite inferior debe ser menor o igual al límite superior.")
                    limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True, True)
                    limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True, True)
                print(f"Probabilidad Hipergeométrica en el rango [{limiteI}, {limiteS}] es: {probabilidad_hipergeometrica(N, M, n, limiteI, limiteS)}")    

            elif opcion == "3":
                print("Poisson")
                print("Recuerde que la probabilidad de ocurrencia debe ser un numero entero mayor que 0")
                #Se ingresa el valor de lamda, o lo que se espera
                cantidad = val_numeros("Promedio de ocurrencias en x intervalo (lamda): ", entero = False, lol = True)
                print("Ingrese la probabilidad de ocurrencia de cuales casos quiere calcular. ejemplo; que ingresen desde 2 hasta 4 personas.")
                print("En caso de ser un solo caso, poner el mismo número en ambos límites.")
                limiteI = val_numeros("Valor mínimo \nx = ", entero = True, lol =True)
                limiteF = val_numeros("Valor máximo \nx = ", entero = True, lol = True)
                while limiteI > limiteF:
                    print("Error. El límite inferior debe ser menor o igual al límite superior.")
                    limiteI = val_numeros("Valor mínimo \nx = ", entero = True, lol = True)
                    limiteF = val_numeros("Valor máximo \nx = ", entero = True, lol = True) 
                resultado = 0
                for i in range(limiteI, limiteF + 1):
                    resultado += Poisson(cantidad, i)
                    print(f"La probabilidad de Poisson para x = {i} es: {round(Poisson(cantidad, i), 4)}")
                print(f"El resultado es: ", round(resultado, 4)) 
        
            elif opcion == "4":
                datos = input_float_list("Ingrese los datos separados por espacios: ")
                if len(datos) < 4:
                    print("No se puede calcular la curtosis con menos de 4 datos.")
                curtosis_redondeada, tipo_curtosis = calcular_curtosis(datos)
                print("\nEl coeficiente de curtosis es: ",curtosis_redondeada," y según su resultado es: ", tipo_curtosis)

            elif opcion == "5":
                # Solicitar los parámetros al usuario
                mu_original = float(input("Ingrese la media/mu (μ) de la distribución: "))
                sigma_original = float(input("Ingrese la desviación estándar/sigma (σ) de la distribución: "))
                #Se solicitan los limites para luego estandarizar y calcular la integral
                a = float(input("Ingrese el límite inferior (a) de integración: "))
                b = float(input("Ingrese el límite superior (b) de integración: "))

                resultado_normal=calcular_integral_gaussiana(mu_original, sigma_original, a, b)
                print(f"La Normal o Gaussiana es: {resultado_normal}")

            else:          
                print("Salir")
                break
else:
    print("Opcion no valida. Intente de nuevo.")
