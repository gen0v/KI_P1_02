
class Node:
    def __init__(self, y, x):
        self.value = " "
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None
        self.path = []
        self.x = x
        self.y = y
    def setValue(self, value):
        self.value = value
    def __lt__(self, other):
        return self.f > other.f
    def isWall(self):
        #print(" ++ " + self.value == "W")
        return self.value == "W"
    def setPath(self):
        p = self.parent
        count = 0
        while p is not None:
            # print("Parent position is : " + str(p.x)
            #     + " " + str(p.y))
            p.setValue('X')
            p = p.parent
            count += 1
        print("Cost: " + str(count))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
            




#Attention: for right display of graph x and y are switched
class Map:
    def __init__(self, rows: int=20, cols: int=20):
        print("Creating map...")
        self.cols = cols
        self.rows = rows
        self.map = [[Node(x,y) for x in range(rows)] for y in range(cols)]
        self.startPoint = 0
        self.endPoint = 0
        
    
    def setStartPoint(self,y,x):
        self.map[x-1][y-1].setValue("S")
        self.startPoint = self.map[x-1][y-1]
    def setEndPoint(self,y,x):
        self.map[x-1][y-1].setValue("E")
        self.endPoint = self.map[x-1][y-1]
    
    def my_range(self, start, end, step):
        while start <= end:
            yield start
            start += step

    #for x in my_range(1, 10, 0.5):
    #    print(x)    
    def nghbrs(self, node):
        res = []
        if node.x < 19 :#and self.map[node.x+1][node.y] is not None:
            res.append(self.map[node.x+1][node.y])
        if node.y < 19 :#and self.map[node.x][node.y+1] is not None:
            res.append(self.map[node.x][node.y+1])
        if node.x > 1:#self.map[node.x-1][node.y] is not None:
            res.append(self.map[node.x-1][node.y])
        if node.y > 1:#self.map[node.x][node.y-1] is not None:
            res.append(self.map[node.x][node.y-1])
        return res


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
            # print("Points in the same col, proceeding...")
            if start_point[1] < end_point[1]:
                for p in self.my_range(start_point[1],end_point[1],1):
                    self.map[start_point[0]][p].setValue("W")
            else:
                 for p in self.my_range(end_point[0],start_point[0],1):
                    self.map[start_point[0]][p].setValue("W")
            
        else:
            # print("Points in the same row, proceeding...")
            if start_point[0] < end_point[0]:
                for p in self.my_range(start_point[0],end_point[0],1):
                    self.map[p][start_point[1]].setValue("W")
            else:
                 for p in self.my_range(end_point[0],start_point[0],1):
                    self.map[p][start_point[1]].setValue("W")



    def print(self):
        for row in reversed(self.map):
            for col in row:
                # if len(str(col.value)) == 4:
                #     print(col.value,end="")
                # if len(str(col.value)) == 3:
                #     print(col.value,end=" ")
                # if len(str(col.value)) == 2:
                #     print(col.value,end=" ")
                # if len(str(col.value)) == 1:
                #     print(col.value,end="   ")
                # else:
                #     print(col.value,end=" ")

                print(col.value,end="   ")
            print()




