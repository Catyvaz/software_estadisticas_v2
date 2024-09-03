import math
from scipy.integrate import quad

# Función de la distribución gaussiana donde se realiza la formula para obtener f(x)
def distribucion_gaussiana(x, mu, sigma):
    coeficiente = 1 / (sigma * math.sqrt(2 * math.pi))
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coeficiente * math.exp(exponente)

# Función principal
def calcular_integral_gaussiana():
    # Solicitar los parámetros al usuario
    mu_original = float(input("Ingrese la media/mu (μ) de la distribución: "))
    sigma_original = float(input("Ingrese la desviación estándar/sigma (σ) de la distribución: "))
    #Se solicitan los limites para luego estandarizar y calcular la integral
    a = float(input("Ingrese el límite inferior (a) de integración: "))
    b = float(input("Ingrese el límite superior (b) de integración: "))

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
calcular_integral_gaussiana()

