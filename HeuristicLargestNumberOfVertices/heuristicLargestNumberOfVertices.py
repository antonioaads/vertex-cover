class HeuristicLargestNumberOfVertices():
    def __init__(self, inputFileName):
        self.vertices = {}
        self.edges = {}
        self.edgesNumber = 0
        self.chosenVertices = []
        self.edgesRead = []
        self.inputFileName = inputFileName
        self.readInputFile(inputFileName)

    def readInputFile(self, file):
        with open(file, 'r') as inputFile:
            lines = inputFile.readlines()
            edgeIndex = 1
            for line in lines:
                vertices = line.split('\n')[0].split(',')

                if len(vertices) != 2:
                    raise Exception('Invalid file format')
                
                vertices[0] = int(vertices[0])
                vertices[1] = int(vertices[1])
     
                self.edges[edgeIndex] = (vertices[0], vertices[1])

                for vertex in vertices:
                    if vertex in self.vertices:
                        self.vertices[vertex].append(edgeIndex)
                    else:
                        self.vertices[vertex] = [edgeIndex]
                
                edgeIndex+= 1
            self.edgesNumber = len(self.edges)

    def getVertexIndexWithHigherEdgesNumber(self):
        higherNumber = 0
        higherIndex = None

        for vertex in self.vertices:
            edgesNumber = len(self.vertices[vertex])
            if (edgesNumber > higherNumber):
                higherNumber = edgesNumber
                higherIndex = vertex
        
        return higherIndex

    def removeReadEdges(self, edges):
        for vertex in self.vertices:
            for edge in edges:
                while self.vertices[vertex].count(edge) > 0:
                    self.vertices[vertex].remove(edge)

           

    def run(self):
        while len(self.edgesRead) < self.edgesNumber:
            chosenVertexIndex = self.getVertexIndexWithHigherEdgesNumber()

            verticeEdges = self.vertices[chosenVertexIndex]

            self.chosenVertices.append(chosenVertexIndex)
            self.edgesRead+=verticeEdges
    
            self.removeReadEdges(verticeEdges[:])


        return self.chosenVertices, self.edgesRead