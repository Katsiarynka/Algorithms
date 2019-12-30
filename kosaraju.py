from collections import defaultdict

class Graph(object):
	def __init__(self, v):
		self.v = v
		self.graph = defaultdict(list)

	def getAnOrder(self, v, visited, stack):
		visited[v] = 1
		for vertical in self.graph[v]:
			if not visited[vertical]:
				self.getAnOrder(vertical, visited, stack)
		stack.append(v)

	def addEdge(self, v, destination):
		self.graph[v].append(destination)

	def getTranspose(self):
		g = Graph(self.v)
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j, i)
		return g

	def DFSUtil(self, v, visited):
		visited[v] = True
		print(v,)
		for i in self.graph[v]:
			if not visited[i]:
				self.DFSUtil(i, visited)



	def printSCCs(self):
		stack = []
		visited = [False] * self.v
		for i in range(self.v):
			if not visited[i]:
				self.getAnOrder(i, visited, stack)

		gt = self.getTranspose()
		visited = [False] * self.v	

		while stack:
			v = stack.pop()
			if not visited[v]:
				gt.DFSUtil(v, visited)
				print('')

g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
   
print ("Following are strongly connected components " +
                           "in given graph") 
g.printSCCs() 
# Prints:
# Following are strongly connected components in given graph
# 0
# 1
# 2

# 3

# 4


