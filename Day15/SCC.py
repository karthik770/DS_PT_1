from collections import defaultdict
class Graph:

	def __init__(self,vertices): #8
		self.V= vertices 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v): # (0,1)
		self.graph[u].append(v) 

	def DFSUtil(self,v,visited):
		visited[v]= True
		print (v),
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited)


	def fillOrder(self,v,visited, stack):
		visited[v]= True
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack = stack.append(v)
	
	def getTranspose(self):
		g = Graph(self.V)

		for i in self.graph: #(i,j)
			for j in self.graph[i]:
				g.addEdge(j,i) #(j,i)
		return g

	def printSCCs(self):
		
		stack = []
		visited =[False]*(self.V)
        # Step 1 - DFS
		for i in range(self.V):# 0 - 7
			if visited[i]==False: #0
				self.fillOrder(i, visited, stack) #0,0,[]
        #Step 2- Reverse
		gr = self.getTranspose()
		
		#Step 3- DFS
		visited =[False]*(self.V)

		while stack:
			i = stack.pop()
			if visited[i]==False:
				gr.DFSUtil(i, visited)
				print("")

g = Graph(8)
g.addEdge(0,1) 
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,0)
g.addEdge(2, 4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,4)
g.addEdge(6,7)



print ("Following are strongly connected components " +
						"in given graph")
g.printSCCs()
