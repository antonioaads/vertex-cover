import sys
import time
from heuristicLargestNumberOfVertices import HeuristicLargestNumberOfVertices


if len(sys.argv) < 2:
    raise Exception('Please, send at least one parameter')

for file in sys.argv[1:]:
    print 'Analyzing the graph defined in', file
    
    heuristic = HeuristicLargestNumberOfVertices(file)
    initialTime = time.time()
    chosenVertices, edgesRead = heuristic.run()
    finalTime = time.time()
    chosenVertices.sort()

    print 'Chosen Vertices:', chosenVertices
    print 'Runtime:', finalTime - initialTime, '\n'
