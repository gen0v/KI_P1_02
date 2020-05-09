from queue import Queue
from Map import Node
import heapq
import math

class Astar:
    def __init__(self, map, alg=1):
        self.open = []
        self.closed = []
        self.map = map
        self.alg = alg
    
    def findPath(self, start: Node, end: Node):
        self.initialize(start, end)
        # --------------------------
        while self.open:
            s = heapq.heappop(self.open)
            if s == end:
                # print("END FOUND")
                return s.setPath()
            self.closed.append(s)
            s.setValue(".")
            for child in self.map.nghbrs(s):
                if child.isWall():
                    continue
                # child.setValue(".")
                if child not in self.closed:
                    if child not in self.open:
                        child.g = 999
                        child.parent = None
                self.updateVertex(s,child, end)
        return "No path found"

                        


    def initialize(self, start: Node, end: Node):
        start.g = 0
        if self.alg == 1:
            start.h = abs(start.x - end.x) + abs(start.y - end.y)
        else:
            start.h = math.sqrt(((start.x - end.x) ** 2)+((start.y - end.y) ** 2))
        start.f = start.g + start.h
        heapq.heappush(self.open,start)
        self.closed = []
        
    
    def updateVertex(self, s,child, end):
        if s.g + 1 < child.g:
            child.g = s.g + 1
            child.parent = s
            if child in self.open:
                self.open.remove(child)
            if self.alg == 1:
                child.h = abs(child.x - end.x) + abs(child.y - end.y)
            else:
                child.h = math.sqrt(((child.x - end.x) ** 2)+((child.y - end.y) ** 2))
            child.f = child.g + child.h
            
            heapq.heappush(self.open,child)
            heapq.heapify(self.open)