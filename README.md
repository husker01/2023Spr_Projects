# Title: Sudoku+
 
#### This is a classic sudoku game in different sizes with a slight twist of variants. As the classic sudoku, each cell has exactly one value from 1 to 9. Each row and column have unique numbers from 1 to 9 as well each 3 X 3 cells if the size is 9X9. We are providing 3 sizes i.e., 4X4 , 9X9 and 16X16 As the difficulty level increases, variants like sandwich, thermos etc., are given as part of the rules. 


## Sandwich rules:
#### As part of sandwich sum of numbers between 1 and 9 is displayed for some of the rows and columns. These hints may help the user to solve the puzzle more easily. The sandwich hint is provided only for the boards with difficulty 3 and above. Since 1 and 2 difficulty can be solved without the sandwich hints


## Thermos rules:
#### For thermos we display the patterns where the numbers are in ascending order. The initial number will always be 1. The initial cell is represented as a circle or bulb and then a line is extended from the initial bulb. The value of the number always increases along the line. The thermos hint is provided only for the boards with difficulty 3 and above. Since 1 and 2 difficulty can be solved without the thermos hints

## Targeted Algorithm Analysis:

#### We have used lists to store both the solved and unsolved puzzle board. This choice was made since the lists are easier to traverse and didn't need any overhead computation.

#### For solver, we are using the SAT solver with CNF rules. The sat solver works incredibly faster for sudoku since the rules of sudoku can be easily converted to CNF rules. One of the difficulty we faced is to integrate the sandwich rules into the SAT solver. As a workaround, we have different method which checks for sandwich rules after the SAT solver outputs the solved board. 


### Runtime Complexity Analysis

#### Sudoku Board Generator Analysis

#### The Big Omega analysis for Standard 9x9 Sudoku Board Generator is Omega(1) because in the best case scenario, the algorithm may produce a valid board on its first attempt, which means no backtracking is needed. As a result, the Big Omega is Omega(1). The Big O analysis of a backtracking Sudoku generator is considered to be O(N^(N^2)), where N is the size of the grid (9 in the case of a standard Sudoku board).

#### Sudoku SAT Solver Analysis

#### SAT problems are NP-complete. The worst-case time complexity for any algorithm that solves an NP-complete problem is exponential in the size of the input, which in this case is the size of the Sudoku grid. So the worst-case time complexity is O(2^N), where N is the total number of cells in the grid. With the constraints of Sudoku may make it easier to solve than an arbitrary SAT problem. For example, for a standard 9x9 Sudoku grid, there are a lot of constraints that reduce the number of valid Sudoku grids significantly. Therefore, while the theoretical worst-case complexity is O(2^N), a Sudoku SAT solver will typically perform much better in practice. But the exact runtime can still vary significantly depending on the specific puzzle and the specific SAT solver used.

#### Sudoku Puzzle Generator Analysis

#### The Big Omega analysis for Standard 9x9 Sudoku Puzzle Generator is Omega(1) * O(2^N) because in the best case scenario, the algorithm may produce a valid puzzle on its first attempt, As a result, the Big Omega is Omega(1) * the runtime for SAT solver, which is O(2^N). So finally, the runtime is Omega(1) * O(2^N). But in real case, the runtime is much faster because we have lots of constraint in SAT solver. 

#### The Big O analysis for the board is O(infinity) where the board may produce the puzzle boards with multiple solutions infinitely.

## Graphs
### For 10 games
 ![Test-10.jpg](Test-10.jpg)

### For 100 games
#### Eg 1, with more 3 level difficulty
![Test-100.jpg](Test-100.jpg)

#### Eg 2, with more 4 level difficulty
![Test-100-with max 4.jpg](Test-100-with%20max%204.jpg)


## Summary of Work
#### Luwei Li : Implemented first part of the project i.e., build the generator and SAT solver for the sudoku that includes for both regular size and different size. Added GUI for the sudoku. 

#### Abhisha: Implemented second part which includes adding the sandwich and thermo variants as well as analysis. Worked on performance improvement and Integrated the variants both in solver as well as GUI.

## REFERENCES
#### 1. SAT Solver and SAT Utils were referred from: https://rhettinger.github.io/einstein.html#sudoku-puzzles



