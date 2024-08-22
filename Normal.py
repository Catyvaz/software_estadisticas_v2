import math
from scipy.integrate import quad
# Función para calcular la distribución gaussiana
def distribucion_gaussiana(x, mu, sigma):
    # Calcular la parte del exponente
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    
    # Calcular la densidad de probabilidad
    coeficiente = 1 / (sigma * math.sqrt(2 * math.pi))
    densidad_probabilidad = coeficiente * math.exp(exponente) #INTEGRAR
    #ESTANDARIZAR 
    
    return densidad_probabilidad

"""ejemplo para realizar el print correctamente
print(f"La densidad de probabilidad para x = {x} es: {resultado:.6f}") """

#prueba de funcionamiento ejemplo alturas
mu = 0
sigma = 1
rango_min = -1
rango_max= 1

resultado, error = quad(distribucion_gaussiana,rango_min,rango_max, args(mu,sigma))

print(f"Resultado de la integral{resultado}:")
"""# Rango de valores x
valores_x = range(150, 200)  # Desde 150 cm hasta 200 cm"""

"""#Calcular y almacenar las densidades de probabilidad
valores_y = [distribucion_gaussiana(x, mu, sigma) for x in valores_x]
#Imprimir los resultados
for x, y in zip(valores_x, valores_y):
    print(f"x = {x}, f(x) = {y:.6f}")"""
