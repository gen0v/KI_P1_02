from queue import Queue
from Map import Node
import heapq
import math

class Astar:
    def __init__(self, map):
        self.open = []
        self.closed = []
        self.map = map
    
    def findPath(self, start: Node, end: Node):
        self.initialize(start)
        # --------------------------
        while len(self.open) > 0:
            # Repair heap (idk if needed atm)
            # heapq.heapify(self.open)
            # self.open.sort(reverse=True)
            
            # this works
            self.open.sort()
            
            # self.map.print()

            # for x in self.open:
            #     print(round(x.f,2))
            # lowest cost
            s = self.open.pop()
            # print("VALUE : " + str(s.f))
            # print("Current position is : " + str(s.x)
            #     + " " + str(s.y))
            # input("GO")
            s.setValue(".")
            if s == end:
                # print("END")
                return s.setPath()
                return
            self.closed.append(s)
            
            # going through nghbrs
            for child in self.map.nghbrs(s):
                
                if child in self.closed or child.isWall():
                    # print(str(child.x) + " " + str(child.y) + " IGNORED")
                    # child.setValue("I")
                    #ignore it
                    continue
                # else:
                #     child.g = s.g + 1
                #     child.h = ((child.x - end.x) ** 2)+((child.y - end.y) ** 2)
                #     child.f = child.g + child.h
                #     if child in self.open:
                #         # TEST
                #         for n in self.open:
                #             if n == child:
                #                 if child.g > n.g:
                #                     continue
                #                 else:
                #                     break
                #     child.setValue("G")
                #     self.open.append(child)
                else:
                    if child not in self.open:
                        # make parent
                        child.parent = s
                        # record f g h costs
                        child.g = s.g + 1
                        child.h = abs(child.x - end.x) + abs(child.y - end.y)
                        # child.h = math.sqrt(((child.x - end.x) ** 2)+((child.y - end.y) ** 2))
                        
                        child.f = child.g + child.h
                        # child.setValue("G")
                        # child.setValue(round(child.f,1))
                        self.open.append(child)
                    else:
                        # see if this path is better
                        if s.g + 1 < child.g:
                            child.parent = s
                            child.h = abs(child.x - end.x) + abs(child.y - end.y)
                            # child.h = math.sqrt(((child.x - end.x) ** 2)+((child.y - end.y) ** 2))
                            child.f = child.g + child.h
                            child.setValue("'")


                    
                #self.updateVertex(s,child)
        return "no path found"
                        


    def initialize(self, start: Node):
        #start.parent = start
        #self.open.insert(0,start)
        heapq.heappush(self.open,start)
        
    
    # def updateVertex(self, s,child):
    #     if s.g + 1 < child.g:
    #         child.g = s.g + 1
    #         child.parent = s
    #         if child in self.open:
    #             self.open.remove(0,child)
    #         self.open.insert(0,child)