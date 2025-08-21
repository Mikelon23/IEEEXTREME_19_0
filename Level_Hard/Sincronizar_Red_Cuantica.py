#Una red cuántica tiene n nodos con estados binarios (0/1). Cada segundo, los nodos 
# actualizan su estado:
#Si un nodo tiene ≥2 vecinos con estado 1, cambia su estado (0→1 o 1→0).
#Excepción: Nodos con imán cuántico (lista M) nunca cambian.
#Determina en cuántos segundos la red alcanza un estado estable (que no cambia). Si es cíclica, retorna -1.
#Entrada:
#n m: nodos y aristas (1 ≤ n ≤ 20)
#m líneas: aristas u v (no dirigidas)
#estado_inicial: cadena binaria de longitud n
#k magnetizados: número de nodos magnetizados y sus índices
#Salida:
#Número de segundos hasta estabilidad (o -1 si es cíclica).

#Solución (Simulación + Detección de Ciclos):
from collections import deque

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n)]
    for i in range(1, 1+m):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    estado = list(map(int, list(data[1+m])))
    magnetizados = set(map(int, data[2+m].split()[1:]))
    
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
            vecinos = graph[nodo]
            count_1 = sum(current[v] for v in vecinos)
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

#Entrada:
#3 3
#0 1
#1 2
#2 0
#010
#1 1

#Salida: 2
