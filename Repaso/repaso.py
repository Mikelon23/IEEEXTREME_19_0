"""
EJEMPLOS EJECUTABLES - Guía de Algoritmos IEEE

Este archivo contiene todos los algoritmos con casos de prueba
que puedes ejecutar directamente para ver cómo funcionan.

Uso: python3 ejemplos_ejecutables.py
"""

from collections import deque, defaultdict
import heapq
import bisect
import math

print("=" * 70)
print(" GUÍA DE ALGORITMOS - EJEMPLOS EJECUTABLES ".center(70))
print("=" * 70)
print()

# =============================================================================
# 1. BFS - BÚSQUEDA EN ANCHURA
# =============================================================================

print("\n" + "=" * 70)
print("1. BFS - BÚSQUEDA EN ANCHURA")
print("=" * 70)

def bfs(graph, start):
    """Realiza BFS y retorna distancias"""
    n = len(graph)
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)
    
    return dist

# Ejemplo: Red social
print("\nEjemplo: Red Social de Amigos")
print("Grafo:")
print("  0 (Ana) <-> 1 (Bob) <-> 2 (Carlos)")
print("  0 (Ana) <-> 3 (Diana)")
print("  3 (Diana) <-> 4 (Elena)")

nombres = ["Ana", "Bob", "Carlos", "Diana", "Elena"]
grafo_amigos = [
    [1, 3],     # Ana es amiga de Bob y Diana
    [0, 2],     # Bob es amigo de Ana y Carlos
    [1],        # Carlos es amigo de Bob
    [0, 4],     # Diana es amiga de Ana y Elena
    [3]         # Elena es amiga de Diana
]

distancias = bfs(grafo_amigos, 0)  # Desde Ana
print("\nDistancias desde Ana:")
for i, d in enumerate(distancias):
    print(f"  {nombres[i]}: {d} saltos")

print("\n✓ BFS encuentra el camino más corto en grafos no ponderados")

# =============================================================================
# 2. DFS - BÚSQUEDA EN PROFUNDIDAD
# =============================================================================

print("\n" + "=" * 70)
print("2. DFS - BÚSQUEDA EN PROFUNDIDAD")
print("=" * 70)

def dfs_iterative(graph, start):
    """DFS iterativo que retorna orden de visita"""
    visited = set()
    stack = [start]
    orden = []
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            orden.append(current)
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return orden

print("\nEjemplo: Exploración de Laberinto")
print("Grafo de habitaciones:")
print("  0 -> [1, 2]")
print("  1 -> [3]")
print("  2 -> [3]")
print("  3 -> []")

grafo_laberinto = [
    [1, 2],
    [3],
    [3],
    []
]

orden_dfs = dfs_iterative(grafo_laberinto, 0)
print(f"\nOrden de exploración DFS: {orden_dfs}")
print("✓ DFS explora en profundidad antes de retroceder")

# =============================================================================
# 3. DIJKSTRA - CAMINO MÍNIMO
# =============================================================================

print("\n" + "=" * 70)
print("3. DIJKSTRA - CAMINO MÁS CORTO")
print("=" * 70)

def dijkstra(graph, start):
    """Algoritmo de Dijkstra"""
    n = len(graph)
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    parent = [-1] * n
    heap = [(0, start)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(heap, (new_dist, v))
    
    return dist, parent

def reconstruct_path(parent, start, end):
    """Reconstruye el camino"""
    if parent[end] == -1 and end != start:
        return None
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    return path[::-1]

print("\nEjemplo: Red de Carreteras (en km)")
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla"]
print("\nConexiones:")
print("  Madrid <-> Barcelona (620 km)")
print("  Madrid <-> Valencia (350 km)")
print("  Madrid <-> Sevilla (530 km)")
print("  Barcelona <-> Valencia (350 km)")
print("  Valencia <-> Sevilla (650 km)")

grafo_carreteras = [
    [(1, 620), (2, 350), (3, 530)],  # Madrid
    [(0, 620), (2, 350)],             # Barcelona
    [(0, 350), (1, 350), (3, 650)],   # Valencia
    [(0, 530), (2, 650)]              # Sevilla
]

dist, parent = dijkstra(grafo_carreteras, 0)  # Desde Madrid

print("\nDistancias desde Madrid:")
for i, d in enumerate(dist):
    camino = reconstruct_path(parent, 0, i)
    nombres_camino = [ciudades[c] for c in camino]
    print(f"  {ciudades[i]}: {d} km - Ruta: {' -> '.join(nombres_camino)}")

print("\n✓ Dijkstra garantiza el camino más corto con pesos no negativos")

# =============================================================================
# 4. DSU - UNION-FIND
# =============================================================================

print("\n" + "=" * 70)
print("4. DSU - DISJOINT SET UNION")
print("=" * 70)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True
    
    def same_set(self, x, y):
        return self.find(x) == self.find(y)

print("\nEjemplo: Círculos de Amigos")
print("Personas: 0, 1, 2, 3, 4, 5")
print("\nAmistades:")
print("  0 <-> 1")
print("  2 <-> 3")
print("  4 <-> 5")

dsu = DSU(6)
dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(4, 5)

print("\nConsultas:")
print(f"  ¿0 y 1 son amigos? {dsu.same_set(0, 1)} ✓")
print(f"  ¿0 y 2 son amigos? {dsu.same_set(0, 2)} ✗")
print(f"  ¿2 y 3 son amigos? {dsu.same_set(2, 3)} ✓")

# Ahora 0 y 2 se hacen amigos
print("\nNueva amistad: 0 <-> 2")
dsu.union(0, 2)

print("\nConsultas después:")
print(f"  ¿0 y 3 son amigos? {dsu.same_set(0, 3)} ✓ (indirectamente)")
print(f"  ¿1 y 3 son amigos? {dsu.same_set(1, 3)} ✓ (indirectamente)")

print("\n✓ DSU mantiene componentes conexas eficientemente")

# =============================================================================
# 5. KRUSKAL MST
# =============================================================================

print("\n" + "=" * 70)
print("5. KRUSKAL - ÁRBOL DE EXPANSIÓN MÍNIMA")
print("=" * 70)

def kruskal_mst(n, edges):
    """Algoritmo de Kruskal"""
    edges.sort()
    dsu = DSU(n)
    total_cost = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if dsu.union(u, v):
            total_cost += weight
            mst_edges.append((u, v, weight))
    
    return total_cost, mst_edges

print("\nEjemplo: Red Eléctrica (costos en miles de €)")
print("Ciudades: A(0), B(1), C(2), D(3)")
print("\nCables posibles:")
aristas_cable = [
    (10, 0, 1),  # A-B: 10k€
    (15, 0, 2),  # A-C: 15k€
    (20, 0, 3),  # A-D: 20k€
    (25, 1, 2),  # B-C: 25k€
    (30, 1, 3),  # B-D: 30k€
    (35, 2, 3),  # C-D: 35k€
]

for w, u, v in sorted(aristas_cable):
    print(f"  Ciudad {u} <-> Ciudad {v}: {w}k€")

costo_mst, cables_mst = kruskal_mst(4, aristas_cable.copy())

print(f"\n✓ MST encontrado con costo total: {costo_mst}k€")
print("Cables a instalar:")
for u, v, w in cables_mst:
    print(f"  Ciudad {u} <-> Ciudad {v}: {w}k€")

print("\n✓ Kruskal garantiza costo mínimo para conectar todos los nodos")

# =============================================================================
# 6. PROGRAMACIÓN DINÁMICA - KNAPSACK
# =============================================================================

print("\n" + "=" * 70)
print("6. PROGRAMACIÓN DINÁMICA - KNAPSACK 0/1")
print("=" * 70)

def knapsack(weights, values, capacity):
    """Problema de la mochila 0/1"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    
    # Reconstruir items
    w = capacity
    items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], items[::-1]

print("\nEjemplo: Mochila de Viaje")
objetos = ["Laptop", "Cámara", "Libro", "Ropa"]
pesos = [3, 2, 1, 2]  # kg
valores = [50, 30, 15, 20]  # utilidad
capacidad = 5  # kg

print(f"Capacidad de mochila: {capacidad} kg\n")
print("Objetos disponibles:")
for i, obj in enumerate(objetos):
    print(f"  {obj}: {pesos[i]} kg, valor {valores[i]}")

valor_max, items_tomados = knapsack(pesos, valores, capacidad)

print(f"\n✓ Valor máximo: {valor_max}")
print("Items a llevar:")
for idx in items_tomados:
    print(f"  - {objetos[idx]} ({pesos[idx]} kg, valor {valores[idx]})")

peso_total = sum(pesos[i] for i in items_tomados)
print(f"Peso total: {peso_total} kg")

print("\n✓ DP encuentra la combinación óptima explorando todos los subproblemas")

# =============================================================================
# 7. LIS - LONGEST INCREASING SUBSEQUENCE
# =============================================================================

print("\n" + "=" * 70)
print("7. LIS - SUBSECUENCIA CRECIENTE MÁS LARGA")
print("=" * 70)

def lis_nlogn(arr):
    """LIS con binary search O(N log N)"""
    tails = []
    
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

print("\nEjemplo: Secuencia de Números")
secuencia = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Secuencia: {secuencia}")

longitud_lis = lis_nlogn(secuencia)
print(f"\n✓ Longitud de LIS: {longitud_lis}")
print("Ejemplos de LIS posibles: [2, 3, 7, 18] o [2, 3, 7, 101]")

print("\n✓ LIS se resuelve eficientemente con binary search")

# =============================================================================
# 8. BINARY SEARCH
# =============================================================================

print("\n" + "=" * 70)
print("8. BINARY SEARCH - BÚSQUEDA BINARIA")
print("=" * 70)

def binary_search(arr, target):
    """Búsqueda binaria clásica"""
    left, right = 0, len(arr) - 1
    pasos = 0
    
    while left <= right:
        pasos += 1
        mid = (left + right) // 2
        print(f"  Paso {pasos}: Buscando en índice {mid} (valor {arr[mid]})")
        
        if arr[mid] == target:
            return mid, pasos
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, pasos

print("\nEjemplo: Buscar en Array Ordenado")
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
objetivo = 17

print(f"Array: {numeros}")
print(f"Buscar: {objetivo}\n")

indice, pasos = binary_search(numeros, objetivo)

if indice != -1:
    print(f"\n✓ Encontrado en índice {indice} en {pasos} pasos")
    print(f"  (vs {len(numeros)} pasos con búsqueda lineal)")
else:
    print(f"\n✗ No encontrado ({pasos} pasos)")

print("\n✓ Binary Search reduce búsquedas de O(N) a O(log N)")

# =============================================================================
# 9. BINARY SEARCH EN RESPUESTA
# =============================================================================

print("\n" + "=" * 70)
print("9. BINARY SEARCH EN LA RESPUESTA")
print("=" * 70)

def can_distribute(arr, k, max_sum):
    """¿Podemos dividir arr en k subarrays con suma máx max_sum?"""
    subarrays = 1
    current_sum = 0
    
    for num in arr:
        if num > max_sum:
            return False
        if current_sum + num > max_sum:
            subarrays += 1
            current_sum = num
        else:
            current_sum += num
    
    return subarrays <= k

def split_array_min_max(arr, k):
    """Divide array en k subarrays minimizando la suma máxima"""
    left = max(arr)  # Mínimo posible
    right = sum(arr)  # Máximo posible
    result = right
    
    print(f"Rango de búsqueda: [{left}, {right}]")
    iteracion = 0
    
    while left <= right:
        iteracion += 1
        mid = (left + right) // 2
        print(f"  Iteración {iteracion}: Probando suma máxima = {mid}")
        
        if can_distribute(arr, k, mid):
            result = mid
            right = mid - 1
            print(f"    ✓ Posible con {mid}, buscar menor")
        else:
            left = mid + 1
            print(f"    ✗ No posible con {mid}, buscar mayor")
    
    return result

print("\nEjemplo: Dividir Tareas entre Trabajadores")
tareas = [7, 2, 5, 10, 8]  # Horas por tarea
num_trabajadores = 2

print(f"Tareas (horas): {tareas}")
print(f"Trabajadores: {num_trabajadores}")
print(f"Objetivo: Minimizar máximo de horas que trabaja un trabajador\n")

min_max = split_array_min_max(tareas, num_trabajadores)

print(f"\n✓ Mínimo máximo: {min_max} horas")
print("Distribución posible: [7, 2, 5] (14h) y [10, 8] (18h)")

print("\n✓ Binary search en respuesta encuentra el óptimo sin probar todo")

# =============================================================================
# RESUMEN FINAL
# =============================================================================

print("\n" + "=" * 70)
print(" RESUMEN ".center(70))
print("=" * 70)

algoritmos_cubiertos = [
    ("BFS", "O(V+E)", "Camino más corto sin pesos"),
    ("DFS", "O(V+E)", "Exploración profunda, ciclos"),
    ("Dijkstra", "O((V+E) log V)", "Camino más corto con pesos ≥ 0"),
    ("DSU", "O(α(n)) ≈ O(1)", "Union-find, componentes"),
    ("Kruskal", "O(E log E)", "MST - árbol expansión mínima"),
    ("Knapsack DP", "O(N·W)", "Optimización con restricciones"),
    ("LIS", "O(N log N)", "Subsecuencia creciente máxima"),
    ("Binary Search", "O(log N)", "Búsqueda en ordenados"),
]

print("\nAlgoritmos implementados:\n")
for nombre, complejidad, descripcion in algoritmos_cubiertos:
    print(f"  ✓ {nombre:<20} {complejidad:<18} {descripcion}")

print("\n" + "=" * 70)
print(" Todos los algoritmos ejecutados correctamente! ".center(70))
print("=" * 70)
print()