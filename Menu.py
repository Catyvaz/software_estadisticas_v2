from Funciones import *
from software_estadistica_v1 import *

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

    if seleccion == 1:
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
    elif seleccion == 2:
        print("Se eligió Probabilidad y Estadísticas")
        print("Seleccione qué distribución quiere calcular.")
        print("1 = Binomial. \n2 = Hipergeométrica. \n3 = Poisson. \n4 =  Coeficiente de Curtosis. \n5 = Normal o Gaussiana.")
        while True:
            print("\nSeleccion de funcion a probar:")
            print("1. Calcular Probabilidad Binomial")
            print("2. Calcular Probabilidad Hipergeométrica")
            print("3. Poisson.")
            print("4. Coeficiente de Curtosis.")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                n = int(input("Ingrese el número de ensayos (n): "))
                p = float(input("Ingrese la probabilidad de éxito (p): "))
                k = int(input("Ingrese el número de éxitos deseados (k): "))
                print(f"Probabilidad Binomial P(X = {k}) es: {probabilidad_binomial(n,p,k)}")

            elif opcion == "2":
                N = int(input("Ingrese el tamaño de la población (N): "))
                K = int(input("Ingrese el número de éxitos en la población (K): "))
                n = int(input("Ingrese el tamaño de la muestra (n): "))
                k = int(input("Ingrese el número de éxitos en la muestra (k): "))
                print(f"Probabilidad Hipergeométrica es: {probabilidad_hipergeometrica(N,K,n,k)}")

            elif opcion == "3":
                while True:
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

            
            
            
            elif opcion == "5":
                print("Creo que anda todo")
                break

            else:
                print("Opcion no valida. Intente de nuevo.")

