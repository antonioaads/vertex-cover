from typing import List, OrderedDict
class Vertex:
	def __init__(self, value):
		self.value = value
		self.adj = []

	def insert(self, neighbor):
		self.adj.append(neighbor)

	def getValue(self):
		return self.value

	def getAdj(self):
		return self.adj

class Grafo:
	def __init__(self):
		self.vertexes = OrderedDict()

	def addVertex(self, vertexValue) -> Vertex:
		newVertex = Vertex(vertexValue)
		self.vertexes[vertexValue] = newVertex
		return newVertex

	def addEdge(self, sourceVertexValue, destinationVertexValue):
		sourceVertex = self.getVertex(sourceVertexValue)
		destinationVertex = self.getVertex(destinationVertexValue)
		if not sourceVertex is None and not destinationVertex is None:
			sourceVertex.insert(destinationVertex)
			destinationVertex.insert(sourceVertex)

	def markEdgeAsUsed(self, sourceVertexValue, destinationVertexValue):
		sourceVertex = self.getVertex(sourceVertexValue)
		destinationVertex = self.getVertex(destinationVertexValue)
		if not sourceVertex is None and not destinationVertex is None:
			sourceVertex.insert(destinationVertex)
			destinationVertex.insert(sourceVertex)

	def getVertex(self, vertexValue:str) -> Vertex:
		if vertexValue in self.vertexes:
			return self.vertexes[vertexValue]
		else:
			return None

	def getMinimunVertexCover(self):

		cover = []

		for sourceVertex in self.vertexes:
			for destinationVertex in vertex.getAdj().reverse():
				if(destinationVertex not in cover and destinationVertex.getValue() > sourceVertex.getValue()):
					cover.append(sourceVertex)
					break

		return cover

if __name__ == "__main__":
	main()