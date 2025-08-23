import math
from itertools import combinations

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    puntos = []
    for i in range(1, 1 + n):
        x, y = map(int, data[i].split())
        puntos.append((x, y))
    
    origen = (0, 0)
    dist_origen = [distancia(origen, p) for p in puntos]
    
    dist_entre = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_entre[i][j] = distancia(puntos[i], puntos[j])
    
    # DP: dp[mask][i] = mínima distancia al visitar conjunto 'mask' terminando en 'i'
    dp = [[float('inf')] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 2 * dist_origen[i]
    
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                nuevo_valor = dp[mask][i] - dist_origen[i] + dist_entre[i][j] + dist_origen[j]
                if nuevo_valor < dp[new_mask][j]:
                    dp[new_mask][j] = nuevo_valor
    
    min_dist = float('inf')
    for mask in range(1 << n):
        if bin(mask).count('1') == k:
            for i in range(n):
                if dp[mask][i] < min_dist:
                    min_dist = dp[mask][i]
    
    print("{:.2f}".format(min_dist))

if __name__ == "__main__":
    main()