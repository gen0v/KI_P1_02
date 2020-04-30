from queue import Queue
from Map import Node
import heapq

class Astar:
    def __init__(self, map):
        self.open = []
        self.closed = []
        self.map = map
    
    def findPath(self, start: Node, end: Node):
        self.initialize(start)
        # --------------------------
        while len(self.open) > 0:
            # input("GO")
            self.map.print()
            
            # Repair heap (idk if needed atm)
            heapq.heapify(self.open)
            # lowest cost
            s = self.open.pop()
            print("Current position is : " + str(s.x)
                + " " + str(s.y))
            if s == end:
                print("END")
                return s.setPath()
                return
            self.closed.append(s)
            
            # going through nghbrs
            for s2 in self.map.nghbrs(s):
                
                if s2 in self.closed or s2.isWall():
                    #ignore it
                    continue
                else:
                    if s2 not in self.open:
                        # make parent
                        s2.parent = s
                        # record f g h costs
                        s2.g = s.g + 1
                        s2.h = abs(s2.x - end.x) + abs(s2.y - end.y)
                        s2.f = s2.g + s2.h
                        # s2.setValue("G")
                        self.open.append(s2)
                    else:
                        # see if this path is better
                        if s.g + 1 < s2.g:
                            s2.parent = s
                            s2.h = abs(s2.x - end.x) + abs(s2.y - end.y)
                            s2.f = s2.g + s2.h
                            s2.setValue("'")


                    
                #self.updateVertex(s,s2)
        return "no path found"
                        


    def initialize(self, start: Node):
        #start.parent = start
        #self.open.insert(0,start)
        heapq.heappush(self.open,start)
        
    
    def updateVertex(self, s,s2):
        if s.g + 1 < s2.g:
            s2.g = s.g + 1
            s2.parent = s
            if s2 in self.open:
                self.open.remove(0,s2)
            self.open.insert(0,s2)