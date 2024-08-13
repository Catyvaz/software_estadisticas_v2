#Funcion para calcular el factorial de un num n
def factorial(n):
    #si n es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    #inicia el resultado en 1
    resultado = 1
    #bucle para multiplicar todos los num desde 2 hasta n
    for i in range(2, n + 1):
        #multiplica el resultado por i en cada interacion.
        resultado *= i 
     #retorna el factorial calculado    
    return resultado

#funcion para calcular el num comb.
def combinatorio(n,k):
    #calculamos num comb usando formula: n! / k! * (n - k)!
    return factorial(n) // (factorial(k) * factorial(n - k))
    #usamos la funcion factorial para calcular los factoriales necesarios.
    