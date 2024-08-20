# Definición de funciones

from typing import List, Tuple, Dict #001: se importa la librería typing para documentar mejor las funciones

def media(lista: List[float]) -> float: # La función recibe una lista de números flotantes y devuelve un número flotante
    suma = sum(lista) # Suma los elementos de la lista
    res_media = suma / len(lista)
    res_media_redondeado = round(res_media, 4) # Redondea a 4 decimales

    return res_media_redondeado # Retorna la media redondeada

def mediana(lista: List[float]) -> float:
    lista_ordenada = sorted(lista) #002: se crea una lista nueva con los elementos ordenados 
    mitad = len(lista_ordenada) // 2 #003: se toma la división entera de la longitud de la lista por 2

    if len(lista_ordenada) % 2 == 0: # Si la cantidad de elementos de la lista es par
        res_mediana = (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2 #004: La mediana es la suma de los elementos centrales dividido 2
    else: # Si la cantidad de elementos es impar
        res_mediana = lista_ordenada[mitad] #005: La mediana es el valor central

    return res_mediana # Retorna la mediana
    
def moda(lista: Dict[float, int], lista_ordenada: Dict[float, int]) -> Tuple[List[float], float]: # La función recibe dos diccionarios con claves flotantes y valores enteros, y devuelve una tupla que contiene una lista de flotantes y un flotante
    max_frecuencia = max(lista.values()) # Se calcula la frecuencia absoluta máxima de los números de la lista
    
    if list(lista.values()).count(max_frecuencia) == len(lista): #006: si todos los valores tienen la misma frecuencia
        res_moda = None # No existe la moda, es decir, es igual a vacío
    else: # Si existe moda (ya sea simple o múltiple)
        res_moda = [numero for numero, frecuencia in lista_ordenada.items() if frecuencia == max_frecuencia] #007: Se calcula una lista con la moda o modas
    
    return res_moda, max_frecuencia # Retorna el valor o los valores de la moda con su respectiva frecuencia absoluta
    
def cuartiles(lista: List[float]) -> Tuple[float, float, float]: # La función recibe una lista de flotantes y devuelve una tupla de tres flotantes
    lista_ordenada = sorted(lista)
    mitad = len(lista_ordenada) // 2 # Bajo la misma lógica que en la mediana, se calcula el medio

    if len(lista_ordenada) % 2 == 0:
        nros_izq = lista_ordenada[:mitad] #008: se toma la mitad izquierda del conjunto
    else:
        nros_izq = lista_ordenada[:mitad+1] #009: se toma la mitad izquierda más la mediana
    res_Q1 = mediana(nros_izq) # Para Q1, se calcula la mediana de este subconjunto

    res_Q2 = mediana(lista_ordenada) # Q2 es el mismo valor que la mediana

    nros_der = lista_ordenada[mitad:] #010: se toma la mitad derecha del conjunto (se incluye la mediana si la longitud es impar)
    res_Q3 = mediana(nros_der) # Para Q3, se calcula la mediana de este subconjunto

    return res_Q1, res_Q2, res_Q3 # Retorna los valores de los cuartiles

def rango(lista: List[float]) -> float:
    lista_ordenada = sorted(lista)
    minimo = lista_ordenada[0] # El valor mínimo es el primero de la lista
    maximo = lista_ordenada[len(lista_ordenada) - 1] # El valor máximo es el último de la lista
    res_rango = maximo - minimo

    return res_rango # Retorna el valor del rango

def varianza(lista: List[float]) -> float:
    sumatoria = 0
    for numero in lista:
        termino = (numero - media(lista)) ** 2 # Calcula el cuadrado de Xi menos la media
        sumatoria += termino

    if len(lista) != 1:
        res_varianza = sumatoria / (len(lista) - 1) # n-1
        res_varianza_redondeado = round(res_varianza, 4)
    else: # Si hay solo un elemento, no hay varianza
        res_varianza_redondeado = None

    return res_varianza_redondeado # Retorna la varianza redondeada

def desviacion_estandar(lista: List[float]) -> float:
    if len(lista) != 1:
        res_desviacion_estandar = varianza(lista) ** 0.5 # Calcula la raíz cuadrada de la varianza
        res_desviacion_estandar_redondeado = round(res_desviacion_estandar, 4)
    else: # Si hay un solo elemento, no hay desviación
        res_desviacion_estandar_redondeado = None

    return res_desviacion_estandar_redondeado # Retorna la desviación estándar redondeada

def frecuencias(lista_ordenada: dict) -> list:
    can = sum(lista_ordenada.values()) # Calcula la cantidad de elementos
    frecuencia_abs_acumulada = 0
    frecuencia_rel_acumulada = 0
    frecuencia_por_acumulada = 0
    filas = [] #011: creo una lista para almacenar cada fila de la tabla

    for numero, frecuencia in lista_ordenada.items(): # Se calculan los distintos tipos de frecuencias
        frecuencia_relativa = (frecuencia / can)
        frecuencia_porcentual = (frecuencia / can) * 100
        frecuencia_abs_acumulada += frecuencia
        frecuencia_rel_acumulada += frecuencia_relativa
        frecuencia_por_acumulada += frecuencia_porcentual
        #012: se crea el formato para cada línea usando f-strings
        fila = f"{numero:10} | {frecuencia:2}  | {frecuencia_relativa:7.4f} | {frecuencia_porcentual:7.4f}% | {frecuencia_abs_acumulada:3}  | {frecuencia_rel_acumulada:7.4f}  | {frecuencia_por_acumulada:7.4f}%"
        filas.append(fila) # Se agrega cada línea a la lista

    return filas # Retorna la lista con las líneas de la tabla

# Funciones de validación de entrada

def input_int(prompt: str) -> int: #013: Función que verifica que se ingrese un entero en la sección del menú
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def input_float_list(prompt: str) -> List[float]: #014: Función que verifica que se ingrese una lista de flotantes al inicio
    while True:
        try:
            input_data = input(prompt)
            return [float(x) for x in input_data.split()]
        except ValueError:
            print("Entrada inválida. Por favor, ingrese una lista de números separados por espacios.")

