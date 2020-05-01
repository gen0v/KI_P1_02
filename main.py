from Map import Node,Map as Map
from aStar import Astar
import copy

# Boundaries count start at 1
# Create Map 
map, map2 = Map(), Map()
map.setStartPoint(1,1)
map.setEndPoint(20,20)
#normal walls
map.setWall((10,1),(10,10))
map.setWall((5,10),(10,10))
map.setWall((17,10),(17,20))

map2 = copy.deepcopy(map)

print("-- Manh. (1)")
astar = Astar(map,1)
astar.findPath(map.startPoint,map.endPoint)
map.print()
###
print()
###
print("-- Eukli. (2)")
astar = Astar(map2,2)
astar.findPath(map2.startPoint,map2.endPoint)
map2.print()