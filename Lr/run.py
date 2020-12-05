import sys
import time
from lr import Graph

if len(sys.argv) < 2:
    raise Exception('Please, send at least one parameter')

for file in sys.argv[1:]:
    print ('Analyzing the graph defined in', file)
    
    graph = Graph()
    graph.readInputFile(file)
    initialTime = time.time()
    chosenVertices = graph.getMinimunVertexCover()
    finalTime = time.time()
    chosenVertices.sort()

    print ('Number of chosen vertices:' , len(chosenVertices))
    print ('Chosen Vertices:', chosenVertices)
    print ('Runtime:', finalTime - initialTime, '\n')
