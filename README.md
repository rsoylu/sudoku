# Sudoku
This is an implementation of the classic game of sudoku in Python. It is a program which uses Constraint Satisfaction Problem (CSP) back-tracking search and alternatively CSP with forward-checking and MRV heuristics in order to solve a given sudoku game file. The program also has the capability to judge whether a given file is a complete and correct sudoku game or not.  
The test cases have been given along with the code for the sudoku game.  

# How it works  
The program accepts two (2) command line arguments, so the code can be executed with  
python cs480_P02_AXXXXXXXX.py MODE FILENAME  
where:  
■ cs480_P02_AXXXXXXXX.py is your python code file name,  
■ MODE is mode in which your program should operate  
◆ 2 – Constraint Satisfaction Problem back-tracking search,  
◆ 3 – CSP with forward-checking and MRV heuristics,  
◆ 4 – test if the completed puzzle is correct.  
■ FILENAME is the input CSV file name (unsolved or solved sudoku puzzle),  
Example:  
python cs480_P02_A11111111.py 2 testcase4.csv  

# Example Game  
![image](https://github.com/rsoylu/sudoku/assets/70935031/e39c312f-51f3-4ef6-ad51-499715d438dc)

