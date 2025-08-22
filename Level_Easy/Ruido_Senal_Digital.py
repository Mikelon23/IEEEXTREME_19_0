#Ana está analizando señales digitales en su laboratorio de telecomunicaciones. 
# Ha notado que algunas muestras de su señal contienen "ruido" representado por 
# valores negativos que necesita filtrar.
#Dada una secuencia de números enteros que representan muestras de una señal digital, tu tarea es:

#Eliminar todos los valores negativos (ruido)
#Calcular el promedio de los valores restantes
#Contar cuántos valores están por encima del promedio

n = int(input())
values = list(map(int, input().split()))

# Filtrar valores positivos
positive_values = [x for x in values if x > 0]

if not positive_values:
    print("0 0")
else:
    # Calcular promedio y redondear hacia abajo
    average = sum(positive_values) // len(positive_values)
    
    # Contar valores por encima del promedio
    above_average = sum(1 for x in positive_values if x > average)
    
    print(f"{average} {above_average}")

#Entrada:
#8 -5 10 3 -2 8 15 -1 6
#Salida:
# 8 2

#Explicación
#Valores positivos: [10, 3, 8, 15, 6]
#Promedio: (10+3+8+15+6)/5 = 42/5 = 8.4 → 8 (redondeado hacia abajo)
#Valores por encima de 8: 10 y 15 → 2 valores