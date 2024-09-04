from math import e
from estadisticas_descriptivas import *

def factorial(m):
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
    # Calculamos combinatorio usando la fórmula: m! / (n! * (m - n)!)
    return factorial(m) // (factorial(n) * factorial(m - n))

def probabilidad_binomial(n, p, limiteI, limiteS):    
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
    resultado = 0
    comb3 = combinatorio(N, n)
    
    if comb3 is None:
        print("Error: División por cero. Verifica los valores de N y n. \nSUCESO IMPOSIBLE \nRegresando al menú...")
        return 0  # Retorna 0 si hubo un error en combinatorio

    for k in range(limiteI, limiteS + 1):    
        comb1 = combinatorio(M, k)
        if comb1 is None:
            print(f"Error al calcular combinatorio, con k = {k}. \nSUCESO IMPOSIBLE \nRegresando al menú...")
            return 0  # Retorna 0 si hubo un error en combinatorio

        comb2 = combinatorio(N - M, n - k)
        if comb2 is None:
            print(f"Error al calcular combinatorio, con k = {k}. \nSUCESO IMPOSIBLE \nRegresando al menú...")
            return 0  # Retorna 0 si hubo un error en combinatorio

        prob = (comb1 * comb2) / comb3
        print(f"La probabilidad hipergeométrica para k = {k} es: {round(prob, 4)}")
        resultado += prob

    return round(resultado, 4)

def Poisson(lamda, x):
    factorial_x = factorial(x)    
    resultado = ((e ** (-lamda)) * (lamda ** x)) / factorial_x
    
    return round(resultado, 6)

#Esta función evalua que los valores que se ingresen sean correctos.
#Se evalua que los que se ingrese sea del tipo numerico, y en caso de no serlo se avisa y se pide que ingrese nuevamente un valor.
#Se ingresa el mensaje que verá el usuario, se condiciona si tiene que ser entero el valor y con simple si se elige entre dos opciones o no.
def val_numeros(mensaje, entero = True, lol = True):
    while True:
        ingreso = input(mensaje)
        if entero:
            try:
                valor = int(ingreso)
                if valor < 0:
                    print("Debe ingresar valores mayores o iguales a 0")
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


def calcular_curtosis(datos):
    n = len(datos)
    media = sum(datos) / n
    varianza = sum((x - media) ** 2 for x in datos) / (n - 1)
    desviacion_estandar = varianza ** 0.5

    curtosis = sum((x - media) ** 4 for x in datos) / ((n - 1)* desviacion_estandar ** 4)
    
    #Restamos 3 para que la distribución normal tenga una curtosis de 0, ya que la curtosis de una distribución normal es exactamente 3
    curtosis_final =  curtosis - 3 

    #Determinación del tipo de curtosis
    if curtosis_final > 0:
        tipo_curtosis= "Leptocúrtica"
    if curtosis_final == 0:
        tipo_curtosis = "Mesocúrtica"
    if curtosis_final < 0:
        tipo_curtosis= "Platicúrtica"
    
    curtosis_redondeada= round(curtosis_final,4)
    return curtosis_redondeada, tipo_curtosis

import math
from scipy.integrate import quad

# Función de la distribución gaussiana donde se realiza la formula para obtener f(x)
def distribucion_gaussiana(x, mu, sigma):
    coeficiente = 1 / (sigma * math.sqrt(2 * math.pi))
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coeficiente * math.exp(exponente)

# Función principal
def calcular_integral_gaussiana(mu_original, sigma_original, a, b):
    # Convertir los límites de integración a la distribución normal estandarizada
    # Se estandariza siguiendo la formula: z = x - mu / sigma
    z_a = (a - mu_original) / sigma_original
    z_b = (b - mu_original) / sigma_original

    # Calcular la integral en la distribución normal estandarizada args(mu=0, sigma=1)
    resultado_estandarizado, _ = quad(distribucion_gaussiana, z_a, z_b, args=(0, 1))

    # Imprimir el resultado redondeando a 4 decimales
    print("Resultado de la integral estandarizada:",round(resultado_estandarizado,4))

# Llamar a la función principal para ejecutar el programa
# DESMARCAR PARA PROBAR 

#prueba funcion requisitos 

from typing import List, Tuple
