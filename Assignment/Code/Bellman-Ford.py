# Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# Class to represent a graph

class Graph:
	
	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.vertex = vertices
		self.graph = []

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def BellmanFord(self, src):

		dist = [float("Inf")] * self.V
		dist[src] = 0
		print(dist)
		
		for _ in range(self.V - 1):
			change = False
			for x in range(11):

				for u, v, w in self.graph:
					if x == u-1 and dist[x] > dist[v-1] + w:
						dist[x] = dist[v-1] + w
						change = True
					if x == v-1 and dist[x] > dist[u-1] + w:
						dist[x] = dist[u-1] + w
						change = True
			print(dist)
			if change == False:
				break


# Driver's code
if __name__ == '__main__':
	g = Graph(11)
	g.addEdge(1, 2, 2)
	g.addEdge(1, 3, 8)
	g.addEdge(1, 4, 1)
	g.addEdge(2, 3, 6)
	g.addEdge(3, 4, 7)
	g.addEdge(2, 5, 1)
	g.addEdge(3, 5, 5)
	g.addEdge(3, 6, 1)
	g.addEdge(3, 7, 2)
	g.addEdge(4, 7, 9)
	g.addEdge(5, 6, 3)
	g.addEdge(6, 7, 4)
	g.addEdge(5, 8, 2)
	g.addEdge(5, 9, 9)
	g.addEdge(6, 9, 6)
	g.addEdge(7, 9, 3)
	g.addEdge(7, 10, 1)
	g.addEdge(8, 9, 7)
	g.addEdge(9, 10, 1)
	g.addEdge(8, 11, 9)
	g.addEdge(9, 11, 2)
	g.addEdge(10, 11, 4)
	
	

	# function call
	g.BellmanFord(0)

# Initially, Contributed by Neelam Yadav
# Later On, Edited by Himanshu Garg