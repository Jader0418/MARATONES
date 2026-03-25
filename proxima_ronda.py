
# PROBLEMA: Next Round (Clasificación)

# n = cantidad de participantes
# k = posición de referencia (puesto k)
n, k = map(int, input().split())

a = list(map(int, input().split()))

# PASO 1: Obtener el puntaje de referencia

# En Python los índices empiezan desde 0
# Entonces el participante en posición k está en índice k-1
pivote = a[k - 1]

# PASO 2: Contar cuántos clasifican

# Inicializamos contador en 0
clasificados = 0


for puntaje in a:
    
    if puntaje >= pivote and puntaje > 0:
        
    
        clasificados += 1


print(clasificados)