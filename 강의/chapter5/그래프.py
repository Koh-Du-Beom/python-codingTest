adj_list = [[] for _ in range(4)]

adj_list[0].append(1); adj_list[0].append(2)
adj_list[1].append(3)
adj_list[2].append(3)
adj_list[3].append(0)

print(adj_list)

adj_matrix = [[0 for _ in range(4)] for _ in range(4)]

adj_matrix[0][1] = 1; adj_matrix[0][2] = 1
adj_matrix[1][3] = 1
adj_matrix[2][3] = 1
adj_matrix[3][0] = 1

print(adj_matrix)


edge_list = []

edge_list.append([0, 1])
edge_list.append([0, 2])
edge_list.append([1, 3])
edge_list.append([2, 3])
edge_list.append([3, 0])

print(edge_list)