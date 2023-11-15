from gurobipy import *
import numpy as np


cols = [1,2,3,4,5,6,7,8,9]
rows = [1,2,3,4,5,6,7,8,9]
nums = [1,2,3,4,5,6,7,8,9]
grid = np.zeros((9, 9))

# create empty model
m = Model("Sudoku Solver")

# add decision variables
numFound = m.addVars(rows, cols, nums, vtype=GRB.BINARY)

# set objective function
m.setObjective(0)

#Adding Constraints
#Loop for adding Known Numbers
exit= "N"
while(exit != "Y"):  
    rowInput = int(input("enter a row (1-9) (1 being top row 9 being bottom \n"))
    colInput = int(input("enter a column (1-9) (1 being left 9 being right)\n"))
    numInput = int(input("enter number in that box\n"))
    m.addConstr(numFound[rowInput, colInput, numInput] == 1)
    exit = input("are you finished entering inputs ? (Y/N)")
    1


 #For every slot there can be only one number
for row in rows:
    for col in cols:
        m.addConstr(quicksum(numFound[row, col, num] for num in nums) == 1)

#For every row a number can only appear once
for row in rows:
    for num in nums:
        m.addConstr(quicksum(numFound[row, col, num] for col in cols) == 1)

#For every column a number can only appear once
for col in cols:
    for num in nums:
         m.addConstr(quicksum(numFound[row, col, num] for row in rows) == 1)
        
#For every 3 by 3 a num can only appear once
for num in range (1, 10):
    m.addConstr(quicksum(numFound[row, col, num]for row in range(1, 4) for col in range (1, 4))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(4, 7) for col in range (1, 4))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(7, 10) for col in range (1, 4))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(1, 4) for col in range (4, 7))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(4, 7) for col in range (4, 7))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(7, 10) for col in range (4, 7))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(1, 4) for col in range (7, 10))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(4, 7) for col in range (7, 10))==1)
    m.addConstr(quicksum(numFound[row, col, num]for row in range(7, 10) for col in range (7, 10))==1)

# solve model
m.optimize()

# Print model
for row in range(1, 10):
    for col in range (1, 10):
        for num in range (1, 10):
            if numFound[row, col, num].x == 1:
                grid[row-1][col-1] = num

# Print the solved Sudoku grid
print(grid)