import sys
import csv
import copy
import time

#Making sure input is correct
error = False
if len(sys.argv) == 3:
    error = False
else:
    error = True

if error == True:
    print("ERROR: Not enough/too many/illegal input arguments.")
    exit()

if sys.argv[1] == '1' or sys.argv[1] == '2' or sys.argv[1] == '3' or sys.argv[1] == '4': #Check if the first input is 1 2 3 or 4
    error = False
else:
    error = True   
try:
    f = open(sys.argv[2], 'rb')
except OSError:
    print ("ERROR: Not enough/too many/illegal input arguments.")
    sys.exit()

if error == True:
    print("ERROR: Not enough/too many/illegal input arguments.")
    exit()

f.close()
#-------------------------------------------------------------------------------------------------------------

#Brute force would take the given file/table
#From a decided order of moves (1 2 3 4 5 6 7 8 9) pick next move
#Enter next move into table
#Run bruteForce again on table
#At the start of the code check if the table is completed(Whether there are any x's)
#If table is completed, check if completed table is correct. if completed table is correct, return completed table
#                                                           elif completed table isnt correct, run 
#If table isnt completed, go ahead with brute force and decide next move, input it into a table, run brute force algo


#Take given file'
#
#if table completed: 
#       if table is correct:
#           return table
#       else:
#           return 1
#if table not completed:
#    for i in 9:
#           for j in 9:
#               if table[i][j] is empty:
#                   put 1 to 9 in table[i][j]
#                       result = run bruteforce() on altered table (THIS WILL BE EITHER THE CORRECT TABLE OR 1)
#                       if result == 1 :passn
#                       else: return result (table)
#               if j is not empty:
#                   pass
#
#From a decided order of moves (1 2 3 4 5 6 7 8 9) pick next move
#


#My attempt at brute force. Currently it gets stuck in an infinite loop, although it sort of works (sort of). Make sure to Ctrl^C after you run it
def bruteForce(table):
    if completed(table):
        print("I reached here!")
        print(*table, sep='\n')
        if correctOrNot(table):
            return table
        else:
            return None
    else:
        for i in range(9):
            for j in range(9):
                if table[i][j] == 0:
                    for k in range(1, 10):
                        newTable = copy.deepcopy(table)
                        newTable[i][j] = k
                        print(f"Trying {k} at position ({i}, {j})")
                        result = bruteForce(newTable)
                        if result is not None:
                            return result
                        table[i][j] = 0
                    return None
    return None

    

def makeList(file):#Make initial list that will be used
     with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        mylist = []
        for row in csvreader:
            mylist.append(row)
        return mylist
 
def fix(mylist): #maps each item into int instead of original string
    newlist = []
    for i in mylist:
        newlist.append(list(map(int,i)))
    return newlist



def bt1(square, row, node_count):
    return backTracking(square, row+1, 0, node_count)

def v1(square, row, column, i):
    return i not in [square[i][j] for i in range(row//3*3, row//3*3+3) for j in range(column//3*3, column//3*3+3)]

def v2(square, row, column, i):
    return i not in [square[i][column] for i in range(9)]

def completed(table):
        for row in table:
            for innerRows in row:
                if innerRows == 'X' or innerRows == '0'or innerRows == 0:
                    return False
        return True

def validOrNot(square, row, column, i):
    checkSquare = v1(square, row, column, i)
    checkRow = i not in square[row]
    checkColumn = v2(square, row, column, i)
    return checkRow and checkColumn and checkSquare

def backTracking(square, row=0, column=0, node_count=0):
    numero = 9
    if row == numero:
        return True, node_count
    elif column == numero:
        return bt1(square, row, node_count)


    elif square[row][column] != 0:
        return backTracking(square, row, column + 1, node_count + 1)
    else:
        r = range(1, 10)
        for num in r:
            if validOrNot(square, row, column, num):
                square[row][column] = num
                success, updated_node_count = backTracking(square, row, column + 1, node_count + 1)
                node_count = updated_node_count
                if success:
                    return True, node_count

                square[row][column] = 0
        return False, node_count
    

def correctOrNot(table): #need to put in a converted table
    iscorrect = True
    
    if repeatsOrNot(table) == True:
        iscorrect = False

    currentcols = []

    currentRange = range(9)
    for i in currentRange:
        currentcols.append(list(j[i] for j in table))

    if repeatsOrNot(currentcols) == True:
        iscorrect = False

    curBox = []    
    allboxes = []
    lineStart = range(0,7,3)
    
    for i in lineStart:
        for j in lineStart:
            for k in range(0+i,3+i):
                for m in range(0+j,3+j):
                    curBox.append(table[k][m])
            allboxes.append(curBox)
            curBox = []
    
    if repeatsOrNot(allboxes) == True:
        iscorrect = False

    return iscorrect

def convert(mylist):
    for i, sublist in enumerate(mylist):
        for j, item in enumerate(sublist):
            if item == 'X':
                mylist[i][j] = 0
    return mylist

def repeatsOrNot(table):
    for i in table:
        have = []
        for j in i:
            if j not in have:
                have.append(j)
            else: 
                return True
    return False        
    
#Used Chatgpt to help create this function

def csp_solver(sudoku_grid):
    def is_valid_choice(r, c, num):
        for i in range(9):
            if sudoku_grid[r][i] == num or sudoku_grid[i][c] == num:
                return False

        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if sudoku_grid[sr + i][sc + j] == num:
                    return False

        return True

    def find_empty_cell():
        for i in range(9):
            for j in range(9):
                if sudoku_grid[i][j] == 0:
                    return i, j
        return None

    def get_choices(r, c):
        if sudoku_grid[r][c] != 0:
            return [sudoku_grid[r][c]]

        choices = set(range(1, 10))

        for i in range(9):
            if sudoku_grid[r][i] in choices:
                choices.remove(sudoku_grid[r][i])
            if sudoku_grid[i][c] in choices:
                choices.remove(sudoku_grid[i][c])

        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if sudoku_grid[sr + i][sc + j] in choices:
                    choices.remove(sudoku_grid[sr + i][sc + j])

        return list(choices)

    def eliminate_options(r, c, num):
        for i in range(9):
            if i != c and sudoku_grid[r][i] == 0 and num in choices[r * 9 + i]:
                choices[r * 9 + i].remove(num)

            if i != r and sudoku_grid[i][c] == 0 and num in choices[i * 9 + c]:
                choices[i * 9 + c].remove(num)

        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                rr, cc = sr + i, sc + j
                if (rr != r or cc != c) and sudoku_grid[rr][cc] == 0 and num in choices[rr * 9 + cc]:
                    choices[rr * 9 + cc].remove(num)

    def heuristic_selection():
        min_values = float('inf')
        min_location = None

        for i in range(9):
            for j in range(9):
                if sudoku_grid[i][j] == 0 and len(choices[i * 9 + j]) < min_values:
                    min_values = len(choices[i * 9 + j])
                    min_location = (i, j)

        return min_location

    def solve():
        nonlocal node_count
        empty_cell = find_empty_cell()
        if empty_cell is None:
            return True

        r, c = empty_cell
        min_location = heuristic_selection()
        if min_location:
            r, c = min_location

        for num in choices[r * 9 + c]:
            if is_valid_choice(r, c, num):
                sudoku_grid[r][c] = num
                eliminate_options(r, c, num)
                node_count += 1

                if solve():
                    return True

                sudoku_grid[r][c] = 0
                eliminate_options(r, c, num)

        return False

    choices = [get_choices(i, j) for i in range(9) for j in range(9)]
    node_count = 0
    result = solve()
    return result, node_count

#-------------------------------------------------------------------------------------------------------------
finalAnsw = []
timeItTook = 0
currentFile = sys.argv[2]
printThis = []
nodes = 0
if sys.argv[1] == '1': #Implementing brute force algorithm
    pass
#Couldnt get my brute force algorithm to work properly, however i left it in regardless (It's all the way at the top)

elif sys.argv[1] == '2': #Implementing CSP Backtracking search
    mylist = makeList(currentFile)

    newlist = convert(mylist)
    newnewlist = fix(newlist)
    start_time = time.time()
    answ, nodes = backTracking(newnewlist)
    end_time = time.time()
    
    timeItTook = end_time - start_time
    finalAnsw = newnewlist
elif sys.argv[1] == '3': #Implementing CSP with forward checking and MRV Heuristics
    mylist = makeList(currentFile)

    newlist = convert(mylist)
    newnewlist = fix(newlist)
    
    start_time = time.time()
    answ, nodes = csp_solver(newnewlist)
    end_time = time.time()
    timeItTook = end_time - start_time
    finalAnsw = newnewlist
elif sys.argv[1] == '4': #Testing if the completed puzzle is correct
    mylist = makeList(currentFile)

    newlist = convert(mylist)
    newnewlist = fix(newlist)
    
    iscorrect = True
    printThis = "This is a valid, solved, Sudoku puzzle."

    if repeatsOrNot(newnewlist) == True:
        printThis = "ERROR: This is NOT a solved sudoku puzzle."
        iscorrect = False

    currentcols = []

    currentRange = range(9)
    for i in currentRange:
        currentcols.append(list(j[i] for j in newnewlist))

    if repeatsOrNot(currentcols) == True:
        printThis = "ERROR: This is NOT a solved sudoku puzzle."
        iscorrect = False

    curBox = []    
    allboxes = []
    lineStart = range(0,7,3)
    
    for i in lineStart:
        for j in lineStart:
            for k in range(0+i,3+i):
                for m in range(0+j,3+j):
                    curBox.append(newnewlist[k][m])
            allboxes.append(curBox)
            curBox = []
    
    if repeatsOrNot(allboxes) == True:
        printThis = "ERROR: This is NOT a solved sudoku puzzle."
        iscorrect = False



#-------------------------------------------------------------------------------------------------------------
#TESTING AREA

#mylist = makeList(currentFile)

#newlist = convert(mylist)
#newnewlist = fix(newlist)

#solve_board(newnewlist)
#for row in newnewlist:
#    print(row)

#print("IGNORE UNDERNEATH******************")

#-------------------------------------------------------------------------------------------------------------
#MAIN
print("Soylu, Rana, A20465152 solution:")
print("Input file: ", sys.argv[2])

if sys.argv[1] == '1': #Implementing brute force algorithm
    currentAlgo = "Brute Force"
elif sys.argv[1] == '2': #Implementing CSP Backtracking search
    currentAlgo = "CSP Backtracking search"
elif sys.argv[1] == '3': #Implementing CSP with forward checking and MRV Heuristics
    currentAlgo = "CSP With Forward Checking and MRV Heuristics"
elif sys.argv[1] == '4': #Testing if the completed puzzle is correct
    currentAlgo = "Testing if completed puzzle is correct"

print("Algorithm: ", currentAlgo)

print("Input puzzle:")

listofRows = makeList(currentFile)

for row in listofRows:
    print(row)

if finalAnsw != []:
    print("Number of search tree nodes generated: ", nodes)
    print("Search time: ",timeItTook, " seconds")
    print("Solved puzzle:")
    
else:
    print(printThis)

for row in finalAnsw:
    print(row)




