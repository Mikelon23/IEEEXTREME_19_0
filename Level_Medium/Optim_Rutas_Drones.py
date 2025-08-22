# Un enjambre de drones debe entregar suministros en n ubicaciones. Cada dron parte desde (0,0), 
# visita exactamente k ubicaciones (en cualquier orden), y regresa al origen.
#  Calcula la distancia mínima total para un dron.
#Entrada:
#Primera línea: n k (2 ≤ k ≤ n ≤ 15)
#Siguientes n líneas: coordenadas x y de cada ubicación (enteros, -100 ≤ x,y ≤ 100).
#Salida:
#Distancia euclidiana mínima redondeada a 2 decimales.

#Solución (Programación Dinámica + Permutaciones):
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n)]
    for i in range(1, 1 + m):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    estado_str = data[1 + m].strip()
    estado = [int(c) for c in estado_str]
    
    k_line = data[2 + m].split()
    k = int(k_line[0])
    magnetizados = set()
    if k > 0:
        magnetizados = set(map(int, k_line[1:1 + k]))
    
    visited = {}
    steps = 0
    current = tuple(estado)
    
    while current not in visited:
        visited[current] = steps
        next_estado = list(current)
        changed = False
        
        for nodo in range(n):
            if nodo in magnetizados:
                continue
                
            count_1 = 0
            for vecino in graph[nodo]:
                if current[vecino] == 1:
                    count_1 += 1
            
            if count_1 >= 2:
                next_estado[nodo] = 1 - current[nodo]
                changed = True
        
        if not changed:
            print(steps)
            return
            
        current = tuple(next_estado)
        steps += 1
    
    print(-1)

if __name__ == "__main__":
    main()