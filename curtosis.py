def calcular_curtosis(lista: List[float]) -> Tuple[float, str]:
    n = len(lista)
    if n < 4:
        return None, "No se puede calcular la curtosis con menos de 4 datos"

    res_media = media(lista)
    res_desviacion_estandar = desviacion_estandar(lista)

    suma_curtosis = sum((numero - res_media) ** 4 for numero in lista)
    curtosis = suma_curtosis / (n * res_desviacion_estandar ** 4)
    
    # Ajuste de Fisher para obtener la curtosis con sesgo corregido
    curtosis_fisher = ((n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))) * curtosis - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))

    if curtosis_fisher > 0:
        tipo_curtosis = "Leptocúrtica"
    elif curtosis_fisher == 0:
        tipo_curtosis = "Mesocúrtica"
    else:
        tipo_curtosis = "Platicúrtica"
    
    return curtosis_fisher, tipo_curtosis  # Retorna el coeficiente de Curtosis y su tipo

"""0 = Salir
    1 = Medidas de posición         
    2 = Medidas de dispersión
    3 = Tabla de frecuencias  
    4 = Curtosis"""

if opcion_a == 4:
        res_curtosis, tipo_curtosis = calcular_curtosis(nros)
        if res_curtosis is not None:
            print(f"El coeficiente de curtosis es: {res_curtosis:.4f} y según su resultadoto es: {tipo_curtosis}")
        else:
            print("No se puede calcular la curtosis con menos de 4 datos.")
    else:
        print("Opción no válida, por favor seleccione una opción válida.")
