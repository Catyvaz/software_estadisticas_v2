def calcular_curtosis(datos):
    n = len(datos)
    media = sum(datos) / n
    varianza = sum((x - media) ** 2 for x in datos) / n
    desviacion_estandar = varianza ** 0.5

    curtosis = sum((x - media) ** 4 for x in datos) / (n * desviacion_estandar ** 4)
    
    # Ajuste de Fisher para obtener la curtosis con sesgo corregido
    curtosis_fisher = ((n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))) * curtosis - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    return curtosis_fisher

# Ejemplo de uso
datos = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
curtosis = calcular_curtosis(datos)
if curtosis > 0:
    tipocurtosis= "Leptocúrtica"
if curtosis == 0:
    tipocurtosis = "Mezzocúrtica"
if curtosis < 0:
    tipocurtosis= "Platicúrtica"

print(f"El coeficiente de curtosis es: {curtosis} y según su resultado es: " , tipocurtosis)
