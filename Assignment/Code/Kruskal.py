# Python program for Kruskal's algorithm to findB
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph


# Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
	def addEdge(self, u, v, w):
		self.graph.append([u-1, v-1, w])
	def find(self, parent, i):
		if parent[i] != i:
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	def union(self, parent, rank, x, y):
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x
		else:
			parent[y] = x
			rank[x] += 1

	def KruskalMST(self):
		result = []
		i = 0
		e = 0
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is less than to V-1
		while e < self.V - 1:
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
				
		minimumCost = 0
		print("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u+1, v+1, weight))
		print("Minimum Spanning Tree", minimumCost)


# Driver code
if __name__ == '__main__':
	g = Graph(7)
	g.addEdge(1, 2, 6)
	g.addEdge(1, 4, 7)
	g.addEdge(1, 3, 8)
	g.addEdge(2, 4, 6)
	g.addEdge(3, 4, 3)
	g.addEdge(2, 5, 6)
	g.addEdge(3, 6, 1)
	g.addEdge(4, 5, 3)
	g.addEdge(4, 6, 4)
	g.addEdge(5, 7, 2)
	g.addEdge(4, 7, 2)
	g.addEdge(6, 7, 3)

	# Function call
	g.KruskalMST()

# This code is contributed by Neelam Yadav
# Improved by James Graça-Jones