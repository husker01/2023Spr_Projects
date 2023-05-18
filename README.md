# Title: Sudoku+
 
#### This is a classic sudoku game in different sizes with a slight twist of variants. As the classic sudoku, each cell has exactly one value from 1 to 9. Each row and column have unique numbers from 1 to 9 as well each 3 X 3 cells if the size is 9X9. We are providing 3 sizes i.e., 4X4 , 9X9 and 16X16 As the difficulty level increases, variants like sandwich, thermos etc., are given as part of the rules. 


## Sanwich rules:
#### As part of sandwich sum of numbers between 1 and 9 is displayed for some of the rows and columns. These hints may help the user to solve the puzzle more easily. The sandwich hint is provided only for the boards with difficulty 3 and above. Since 1 and 2 difficulty can be solved without the sandwich hints


## Thermos rules:
#### For thermos we display the patterns where the numbers are in ascending order. The initial number will always be 1. The initial cell is represented as a circle or bulb and then a line is extended from the initial bulb. The value of the number always increases along the line. The thermos hint is provided only for the boards with difficulty 3 and above. Since 1 and 2 difficulty can be solved without the thermos hints

## Targeted Algorithm Analysis:

#### We have used lists to store both the solved and unsolved puzzle board. This choice was made since the lists are easier to traverse and didn't need any overhead computation.

#### For solver, we are using the SAT solver with CNF rules. The sat solver works incredibly faster for sudoku since the rules of sudoku can be easily converted to CNF rules. One of the difficulty we faced is to integrate the sandwich rules into the SAT solver. As a workaround, we have different method which checks for sandwich rules after the SAT solver outputs the solved board. 


## Runtime complexity Analysis
### The Big Omega analysis 
#### The best case scenario for the solver is calculated by cumulating the best case scenario for most of the complex methods in the solver file.
#### validate_Sandwich : The Big Omega for the sandwich is same as the Big O of the sandwich since, for both worst and best cases the grid will be looped to calculate the sum. Hence, Big Omega is m*n where m is the number of rows and n is the number of columns
#### validate_thermos : The Big Omega for the thermos is x * y where x is the least possible length of the thermos and y is the number of thermos in the puzzle. In the best case scenario x is always 4 and y is always 2
#### solver(): The Big Omega for the solver method is combination of generating cnfs + solving the cnfs + adding the validations for thermos and sandwich. Hence the generation cnfs O((m) + (3*m) + (n)) where m is the row size and numbers are the numbers to be filled in the board. Here the best case scenario is same as the worst case since the cnf rules will iterate through the size and groups of the grid. 
##### The second aspect is the solving of cnfs which will iterate through all the cnf rules added in the generation step.                                           i.e. S * (O((m) + (3*m) + (n))) where S is number of solutions. Here the best case scenario is generating an appropriate puzzle on first try thus number of solutions S = 1

##### The third aspect is the sandwich and thermos i.e. O(m*n) + O(x*y). For the best case scenario x * y is 8. Thus we can remove it since it's a constant. Omega((m * n) + 8) = Omega(m*n)

##### The best case scenario for all these sections can be written as            Omega (((m) + (3*m)+ (n)) + ((m) + (3*m)+ (n)) + (m*n))
i.e. 2 * ((m) + (3*m)+ (n)) + (m*n)
i.e. (m^2*n) + (3*m*n) + (m*n^2)
By removing all constants
= (m^2*n) + (m*n) + (m*n^2)

#### generate_puzzle(): In this method the solver code is called in a while loop until we get 1 solution for the generated puzzle. This method comprises of 2 parts. The first part is iterating through the board to remove number as per the set difficulty level. The 2nd part is solving the generated puzzle with the cnf rules and variant hints, to find a single solution
 ##### For the first part of removing numbers, the equation would be Omega(p * q) where p is the number of cells to empty and q is the number of iteration to find empty cell. For the best case scenario, q will be 1 i.e. we get non empty cells each time a cell is picked randomly. Thus Omega(p)
 #### For the second part of solver, the equation would be R*(((m) + (3*m)+ (n)) + ((m) + (3*m)+ (n)) + (m*n)) where R is the number of loops until 1 solution is found, m is the row size and n is the numbers to fill int he cell. For best case scenario, R = 1
i.e. Omega((m^2*n) + (m*n) + (m*n^2))

#### Combining both parts Omega((p) + ((m^2*n) + (3*m*n) + (m*n^2))). Since p is constant for each difficulty level, we can simplify this as 
i.e. Omega((m^2*n) + (m*n) + (m*n^2))

-----------------------------------------------------------------------------------

### The Big Theta analysis:
#### Average case analysis for the solver is calculated similar to the Omega calculations.

#### validate_Sandwich : The Big Theta for the sandwich is same as the Big O of the sandwich since, for both worst and average cases the grid will be looped to calculate the sum. Hence, Big Theta is m*n where m is the number of rows and n is the number of columns
#### validate_thermos : The Big Theta for the thermos is x * y where x is the least possible length of the thermos and y is the number of thermos in the puzzle. In the average case scenario x is 6 or 7 i.e. (3/4)*SIZE  and y is always 2
#### solver(): The Big Theta for the solver method is combination of generating cnfs + solving the cnfs + adding the validations for thermos and sandwich. Hence the generation cnfs O((m) + (3*m) + (n)) where m is the row size and numbers are the numbers to be filled in the board. Here the average case scenario is same as the worst case since the cnf rules will iterate through the size and groups of the grid. 
##### The second aspect is the solving of cnfs which will iterate through all the cnf rules added in the generation step.                                           i.e. S * (O((m) + (3*m) + (n))) where S is number of solutions. Here the average case scenario is generating an appropriate puzzle on first try thus number of solutions S = (m^2) where m is the number of rows and m^2 will be the number of total cells in the grid.

##### The third aspect is the sandwich and thermos i.e. O(m*n) + O(x*y). For the average case scenario x * y is ((3/4)*m) * 2 . Thus we can remove the constants in the expression. Omega((m * n) + ((3/4)*m) * 2) = Omega((m^2)*n)

##### The average case scenario for all these sections can be written as            Omega (((m) + (3*m)+ (n)) + ((m^2) * ((m) + (3*m)+ (n))) + ((m^2)*n))
i.e.  ((m) + (3*m)+ (n)) + (m^3 + (3*m^3) + ((m^2)* n)) + ((m^2)*n)
Removing the constants
i.e. (m^3) + ((m^2)*n) + m + n

#### generate_puzzle(): In this method the solver code is called in a while loop until we get 1 solution for the generated puzzle. This method comprises 2 parts. The first part is iterating through the board to remove number as per the set difficulty level. The 2nd part is solving the generated puzzle with the cnf rules and variant hints, to find a single solution
 ##### For the first part of removing numbers, the equation would be Theta(p * q) where p is the number of cells to empty and q is the number of iteration to find empty cell. For the average case scenario, q will be p/2 i.e. we get non empty cells nearly half of the time. Thus Theta(p^2)
 #### For the second part of solver, the equation would be R*(((m) + (3*m)+ (n)) + ((m) + (3*m)+ (n)) + (m*n)) where R is the number of loops until 1 solution is found, m is the row size and n is the numbers to fill int he cell. For average case scenario, R can be written as m^2 where the solutions found can be, on an average the size of grid
i.e. Theta((m^2) * ((m^2*n) + (3*m*n) + (m*n^2)))
i.e. ((m^4)*n) + ((m^3)*(n^2)) + ((m^3)*n)

#### Combining both parts Theta((p^2) + (((m^4)*n) + ((m^3)*(n^2)) + ((m^3)*n))). We can simplify this as 
i.e. Theta((p^2) + (((m^4)*n) + ((m^3)*(n^2)) + ((m^3)*n)))
i.e. Theta (((m^4)*(p^2)*n) + ((m^3)*(p^2)*(n^2)) + ((m^3)*(p^2)*n))

------------------------------------------------------------------------------------
#### The Big O analysis for the board is O(infinity) where the board may produce the puzzle boards infinitely.

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



