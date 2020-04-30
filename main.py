from Map import Node,Map as Map
from aStar import Astar

# Boundaries count start at 1
# Create Map 
map = Map()
map.setStartPoint(1,1)
map.setEndPoint(20,20)
map.setWall((10,1),(10,10))
map.setWall((5,10),(10,10))
map.setWall((17,10),(17,20))

#test

astar = Astar(map)
astar.findPath(map.startPoint,map.endPoint)
map.print()
