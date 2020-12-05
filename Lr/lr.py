from typing import List
from collections import OrderedDict
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

class Graph:
	def __init__(self):
		self.vertexes = OrderedDict()
		
	def readInputFile(self, file):
		with open(file, 'r') as inputFile:
			lines = inputFile.readlines()
			for line in lines:
				vertices = line.split('\n')[0].split(',')

				if len(vertices) != 2:
					raise Exception('Invalid file format')
             
				self.addVertex(int(vertices[0]))
				self.addVertex(int(vertices[1]))
				
				self.addEdge(int(vertices[0]), int(vertices[1]))

	def addVertex(self, vertexValue):
		if(vertexValue not in self.vertexes):
			newVertex = Vertex(vertexValue)
			self.vertexes[vertexValue] = newVertex
			return newVertex
		else:
			return self.vertexes[vertexValue]

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

	def getVertex(self, vertexValue):
		if vertexValue in self.vertexes:
			return self.vertexes[vertexValue]
		else:
			return None

	def getMinimunVertexCover(self):

		cover = []
		for vertex in reversed(self.vertexes.keys()):
			sourceVertex = self.vertexes[vertex]
			for destinationVertex in sourceVertex.getAdj():
				if(destinationVertex.getValue() not in cover and destinationVertex.getValue() > sourceVertex.getValue()):
					cover.append(sourceVertex.getValue())
					break

		return cover
