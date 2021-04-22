## Code to check runtime the program
import time
import numpy as np
from scipy.spatial.distance import cdist


print("Welcome to the 8-Puzzle solver, please enter if you want to solve using h1 (number of misplaced tiles) or h2 (Manhattan distance).")

h_method = input("h1 or h2?")
# h_method ="h2"

start_time = time.time()

#Calculates the misplaced tiles and return h1
def calc_h1(start, end):
    h1 = 0
    j = 0
    for number in end:
        i = 0
        while(i<3):
            if(number[i]==start[j][i]):
                i = i+1
                continue
            h1 = h1+1
            i = i+1

        j = j+1

    # print(h1)
    return h1

#Calculates the distance of the misplaced tiles from their goal destination, returns h2
def calc_h2(start, end):
    h2 = 0

    tempstart = np.array(start)
    # print()
    # print((type(start)))
    # print()
    for val in range(1,9):

        xval = np.where(tempstart==(val))[1][0]
        yval = np.where(tempstart==(val))[0][0]
        
        xvaldiff = np.where(end==(val))[1][0]
        yvaldiff = np.where(end==(val))[0][0]

        temp = abs(xval-xvaldiff) + abs(yval-yvaldiff)
        h2 += temp

    return h2


#Calculates the F-value (f(s)=g(s)+h(s), where g(s) is level, h(s) is calculated)
def CalcF(start, goal):
    if(h_method=="h1"):
        return calc_h1(start.data, goal)+start.level    
    if(h_method=="h2"):
        return calc_h2(start.data, goal)+start.level

class Node:
    #Constructor for the node
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def __lt__(self, other):
        return (self.fval < other.fval)
    #Returns all the possible scenarios that are legal when the empty tile is moved.
    def move_tile(self):
        if(h_method=="h1"):
            x,y = self.find(self.data, "")
        else:
            x,y = self.find(self.data, 0)
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children

    def find(self, puz, x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    # print(i,j)
                    return i,j

    def copy(self,root):
    #Copy function to create a similar matrix of the given node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def shuffle(self,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

#Start with an arbritrary matrix filled with 1-9 and one empty slot
# startPuzzle = np.array([[1,2,3], ["",6,4], [7,5,8]])
# startPuzzle = np.array([[1,"",2], [4,5,3], [7,8,6]])

def conv2string(i):
    h = ""
    if(h_method=="h2"):
        for a in i.data:
            for s in a:
                h+=str(s)

    else:
        for a in i.data:
            for s in a:
                h+=s
                if(s==""):
                    h+="0"
    return h

startPuzzle = np.array( [[7, 2, 4], [5, "", 6], [8, 3, 1]])

# startPuzzle = np.array([[6, 4, 7], [8, 5, ""], [3, 2, 1]])

# startPuzzle = np.array([[4, 1, 3], [7, 2, 6], ["", 5, 8]])


#Goal array
# goalPuzzle = np.array([[1,2,3], [4,5,6], [7,8,""]])

#Create a node object from the start puzzle, where default level and fval is 0.

if(h_method=="h1"):
    # startPuzzle = np.array([[6, 4, 7], [8, 5, ""], [3, 2, 1]])
    startPuzzle = np.array( [[7, 2, 4], [5, "", 6], [8, 3, 1]])
    goalPuzzle = np.array([[1,2,3], [4,5,6], [7,8,""]])
    h = calc_h1(startPuzzle, goalPuzzle)
if(h_method=="h2"):
    startPuzzle = np.array( [[7, 2, 4], [5, 0, 6], [8, 3, 1]])
    goalPuzzle = np.array([[1,2,3], [4,5,6], [7,8,0]])
    h = calc_h2(startPuzzle, goalPuzzle)

start = Node(startPuzzle, 0, 0)
start.fval = h+start.level

#Declare two lists, one open and one closed.
import heapq
open = []
close = set()
heapq.heappush(open, start)

#Try heapq close
close.add(conv2string(start))
# close.append(conv2string(start))

while True:

    if(len(open)==0):
        print("unsolvable")
        break

    current = heapq.heappop(open)

    # # For printing out the puzzle as it is being moved.
    # print("\n")
    # for i in current.data:
    #     for j in i:
    #         print(j,end=" ")
    #     print("")
        
    # if(calc_h1(current.data, goalPuzzle)==0):
    #     print("Successful")
    #     break
    for i in current.move_tile():
        if(conv2string(i) not in close):
        # if(conv2string(i) not in close):
            if(h_method=="h1"):
                temp = calc_h1(i.data, goalPuzzle)
            else:
                temp = calc_h2(i.data, goalPuzzle)
            i.fval = temp+i.level
            if(temp==0):
                print("Solved in", i.level, "steps.")
                print("--- %s seconds ---" % (time.time() - start_time))
                exit()

            heapq.heappush(open, i)
            close.add(conv2string(i))


# # Print runtime
