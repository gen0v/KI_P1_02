from Map import Node,Map as Map

map = Map()
# Boundaries count start at 0 
map.setStartPoint(0,0)
map.setEndPoint(19,19)

#map.setWall((0,2))
#map.setWall((1,5))

map.setWall((9,0),(9,9))

map.print()
