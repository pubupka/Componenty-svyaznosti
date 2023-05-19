matrix = [[0, 1, 0, 1, 0, 0, 0],  # граф как на паре, но ещё вершину 7 сделал изолированной
          [1, 0, 1, 0, 0, 0, 0],
          [0, 1, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

nodes = list(range(7))
queue = []  # надо добавить вершину для входа в цикл
components = ""
count = 0

while nodes or queue:
    if not queue:
        queue.append(nodes[0])  # когда компонента связности закончилась, можно начать с любой вершины
    node = queue[0]
    if node in nodes:
        nodes.remove(node)
    for j in range(7):
        if matrix[node][j] == 1 and j in nodes:
            queue.append(j)
            nodes.remove(j)
    components += str(node + 1) + " "
    queue.remove(node)
    if not queue:
        components += "   "
        count += 1
print(f"Компонент связности: {count}, компоненты: {components}")
