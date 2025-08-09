# Un enjambre de drones debe entregar suministros en n ubicaciones. Cada dron parte desde (0,0), 
# visita exactamente k ubicaciones (en cualquier orden), y regresa al origen.
#  Calcula la distancia mínima total para un dron.
#Entrada:
#Primera línea: n k (2 ≤ k ≤ n ≤ 15)
#Siguientes n líneas: coordenadas x y de cada ubicación (enteros, -100 ≤ x,y ≤ 100).
#Salida:
#Distancia euclidiana mínima redondeada a 2 decimales.

#Solución (Programación Dinámica + Permutaciones):
import math
from itertools import combinations

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def main():
    n, k = map(int, input().split())
    puntos = [tuple(map(int, input().split())) for _ in range(n)]
    origen = (0, 0)
    
    # Precalcular distancias desde/hacia origen
    dist_origen = [distancia(origen, p) for p in puntos]
    
    # Matriz de distancias entre puntos
    dist_entre = [[distancia(puntos[i], puntos[j]) for j in range(n)] for i in range(n)]
    
    # DP: dp[mask][i] = mínima distancia al visitar conjunto 'mask' terminando en 'i'
    dp = [[float('inf')] * n for _ in range(1<<n)]
    for i in range(n):
        dp[1<<i][i] = dist_origen[i] * 2  # Ida y vuelta si solo un punto
    
    # Iterar sobre máscaras y puntos
    for mask in range(1<<n):
        for i in range(n):
            if not (mask & (1<<i)): continue
            for j in range(n):
                if mask & (1<<j): continue
                new_mask = mask | (1<<j)
                nuevo_valor = dp[mask][i] - dist_origen[i] + dist_entre[i][j] + dist_origen[j]
                if nuevo_valor < dp[new_mask][j]:
                    dp[new_mask][j] = nuevo_valor
    
    # Encontrar mínimo para todas las máscaras con exactamente k bits activos
    min_dist = float('inf')
    for mask in range(1<<n):
        if bin(mask).count('1') == k:
            min_dist = min(min_dist, min(dp[mask]))
    
    print(f"{min_dist:.2f}")

if __name__ == "__main__":
    main()

#Entrada:
#3 2
#1 1
#2 2
#3 3
#Salida: 5.66