# Python3 Program for Floyd Warshall Algorithm

# Number of vertices in the graph

INF = 99999

class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = []
		for i in range(vertices):
			self.graph.append([])
			for j in range(vertices):
				if i == j:
					self.graph[i].append(0)
				else:
					self.graph[i].append(INF)
	def addEdge(self, u, v, w):
		self.graph[u-1][v-1] = w
		# self.graph[v-1][u-1] = w


# A utility function to print the solution
	def printSolution(self, dist):
		for i in range(self.V):
			for j in range(self.V):
				if(dist[i][j] == INF):
					print("%7s" % ("INF"), end=" ")
				else:
					print("%7d\t" % (dist[i][j]), end=' ')
				if j == self.V-1:
					print()

	def floydWarshall(self):
		dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph))
		self.printSolution(dist)
		for k in range(self.V):
			for i in range(self.V):
				for j in range(self.V):
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
		self.printSolution(dist)

# Driver's code
if __name__ == "__main__":
	g = Graph(7)
	g.addEdge(1, 2, 5)
	g.addEdge(1, 3, 3)
	g.addEdge(2, 3, 2)
	g.addEdge(3, 4, 7)
	g.addEdge(4, 1, 2)
	g.addEdge(2, 7, 1)
	g.addEdge(2, 5, 3)
	g.addEdge(3, 5, 7)
	g.addEdge(4, 6, 6)
	g.addEdge(7, 5, 1)
	g.addEdge(5, 6, 1)
	g.addEdge(5, 4, 2)

	
	# Function call
	
	g.floydWarshall()
# This code is contributed by Mythri J L