
class Node:
    def __init__(self):
        self.value = "."
        self.cost = 0
        self.parent = None
    def setValue(self, value):
        self.value = value


#Attention: for right display of graph x and y are switched
class Map:
    def __init__(self, rows: int=20, cols: int=20):
        print("Creating map...")
        self.cols = cols
        self.rows = rows
        self.map = [[Node() for x in range(rows)] for y in range(cols)]
        
    
    def setStartPoint(self,y,x):
        self.map[x-1][y-1].setValue("S")
    def setEndPoint(self,y,x):
        self.map[x-1][y-1].setValue("E")
    
    def my_range(self, start, end, step):
        while start <= end:
            yield start
            start += step

    #for x in my_range(1, 10, 0.5):
    #    print(x)    

    def setWall(self,start_point: tuple,end_point: tuple=None):
        start_point = (start_point[1]-1,start_point[0]-1)
        if end_point is None:
            self.map[start_point[0]][start_point[1]].setValue("W")
            return
        end_point = (end_point[1]-1,end_point[0]-1)
        if ( not (0 <= start_point[0] < self.rows) 
        or not (0 <= start_point[1] < self.cols)
        or not (0 <= end_point[0] < self.rows)
        or not(0 <= end_point[1] < self.cols)
        ):
            print(len(self.map))
            print(len(self.map[0]))
            
            print("Wrong dimensions...")
            return
        if start_point[1] != end_point[1] and start_point[0] != end_point[0]:
            print("Error: Not in same line")
            return
        elif start_point[0] == end_point[0]:
            print("Points in the same col, proceeding...")
            if start_point[1] < end_point[1]:
                for p in self.my_range(start_point[1],end_point[1],1):
                    self.map[start_point[0]][p].setValue("W")
            else:
                 for p in self.my_range(end_point[0],start_point[0],1):
                    self.map[start_point[0]][p].setValue("W")
            
        else:
            print("Points in the same row, proceeding...")
            if start_point[0] < end_point[0]:
                for p in self.my_range(start_point[0],end_point[0],1):
                    self.map[p][start_point[1]].setValue("W")
            else:
                 for p in self.my_range(end_point[0],start_point[0],1):
                    self.map[p][start_point[1]].setValue("W")

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




