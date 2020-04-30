from queue import Queue
from Map import Node


class Astar:
    def __init__(self, map):
        self.open = list()
        self.closed = []
        self.map = map
    
    def findPath(self, start: Node, end: Node):
        self.initialize(start)
        while len(self.open) > 0:
            s = self.open.pop()
            if s == end:
                return s.path
            self.closed.insert(0,s)
            for s2 in self.map.nghbrs(s):
                if s2 not in self.closed:
                    if s2 not in self.open:
                        s2.g = 999
                        s2.parent = None
                    
                self.updateVertex(s,s2)
            return "no path found"
                        


    def initialize(self, start: Node):
        start.g = 0
        start.parent = start
        self.open.insert(0,start)
        
    
    def updateVertex(self, s,s2):
        if s.g + 1 < s2.g:
            s2.g = s.g + 1
            s2.parent = s
            if s2 in self.open:
                self.open.remove(0,s2)
            self.open.insert(0,s2)