
class Node:
    def __init__(self):
        self.value = "O"
        self.cost = 0
        self.parent = None
    def setValue(self, value):
        self.value = value


class Map:
    def __init__(self, rows: int=20, cols: int=20):
        print("Creating map...")
        self.map = [[Node() for x in range(rows)] for y in range(cols)]
    
    def setStartPoint(self,x,y):
        self.map[x][y].setValue("S")
    def setEndPoint(self,x,y):
        self.map[x][y].setValue("E")
    
    def my_range(self, start, end, step):
        while start <= end:
            yield start
            start += step

    #for x in my_range(1, 10, 0.5):
    #    print(x)    

    def setWall(self,start_point: tuple,end_point: tuple):
        if start_point[1] != end_point[1] and start_point[0] != end_point[0]:
            print("Error: Not in same line")
            return
        elif start_point[0] == end_point[0]:
            print("Points in the same row, proceeding...")
        else:
            print("Points in the same col, proceeding...")
            
        """WRONG
        if start_point[0] < end_point[0]:
            #start at start_point and go right
            for p in self.my_range(start_point[0],end_point[0],1):
                self.map[p][start_point[1]].setValue("W")
        """


    def print(self):
        for row in reversed(self.map):
            for col in row:
                print(col.value,end=" ")
            print()


map = Map()
# Boundaries count start at 0 
map.setStartPoint(0,0)
map.setEndPoint(19,19)
map.setWall((9,0),(9,9))
map.print()


