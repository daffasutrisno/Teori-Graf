import heapq

# Representasi graf menggunakan adjacency list
graph = {
    'V1': [('V2', 2), ('V3', 8), ('V4', 1)],
    'V2': [('V1', 2), ('V5', 1)],
    'V3': [('V1', 8), ('V4', 7), ('V6', 1)],
    'V4': [('V1', 1), ('V3', 7), ('V7', 9)],
    'V5': [('V2', 1), ('V6', 3), ('V8', 2)],
    'V6': [('V3', 1), ('V5', 3), ('V7', 4), ('V9', 6)],
    'V7': [('V4', 9), ('V6', 4), ('V9', 3), ('V10', 1)],
    'V8': [('V5', 2), ('V9', 7), ('V11', 9)],
    'V9': [('V6', 6), ('V7', 3), ('V8', 7), ('V10', 1), ('V11', 2)],
    'V10': [('V7', 1), ('V9', 1)],
    'V11': [('V8', 9), ('V9', 2)]
}

def dijkstra(graph, start, goal):
    # Inisialisasi jarak awal untuk setiap simpul
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    # Menyimpan jalur untuk setiap simpul
    path = {start: None}

    step = 1
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        print(f"Step {step}: Visiting Node: {current_node}, Distance from Start: {current_distance}")
        step += 1

        # Jika mencapai tujuan, keluar dari loop
        if current_node == goal:
            break

        # Proses tetangga-tetangga dari simpul saat ini
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Jika ditemukan jalur yang lebih pendek, update jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                path[neighbor] = current_node
                print(f"   -> Updating path to {neighbor}: New Distance = {distance}")

    # Melacak kembali jalur dari tujuan ke awal
    full_path = []
    current = goal
    while current is not None:
        full_path.insert(0, current)
        current = path[current]

    return distances[goal], full_path

# Menjalankan algoritma Dijkstra dari V1 ke V11
start_node = 'V1'
goal_node = 'V11'
shortest_distance, shortest_path = dijkstra(graph, start_node, goal_node)

print(f"\nShortest path from {start_node} to {goal_node}: {' -> '.join(shortest_path)}")
print(f"Shortest distance from {start_node} to {goal_node}: {shortest_distance}")