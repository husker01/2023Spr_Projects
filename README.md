# 2023Spr_Project Sudoku+
### Luwei Li     
### Abhisha Tarimane

## Deliverables and other Requirements:

* Targeted Algorithm Analysis:  The performance characteristics of some critical parts of the given program can be analyzed as follows:

1. Puzzle Generator (`generate()` function): The puzzle generation algorithm in the code is a backtracking algorithm. In the worst case, the algorithm might need to try all possible numbers in each cell. Since there are `SIZE` possible numbers and `SIZE^2` cells, the worst-case time complexity of the puzzle generator can be estimated as O(SIZE^(SIZE^2)). However, in practice, the algorithm should run faster than this upper bound because it does not need to explore all possibilities due to the constraints of the Sudoku puzzle.

2. Puzzle Solver (`puzzle_solver()` function): The puzzle solver is essentially the same as the generator, as it uses the same `generate()` function to solve the puzzle. Therefore, its worst-case time complexity can also be estimated as O(SIZE^(SIZE^2)). However, the average-case complexity should be significantly better due to the constraints of the Sudoku puzzle.

3. `is_valid()` function: The function checks whether a given number can be placed in a certain cell by checking the row, column, and subgrid. In the worst case, it may need to check all SIZE elements in the row, column, and subgrid, resulting in a time complexity of O(SIZE).

The choice of data structures and algorithms in the program is based on simplicity and ease of implementation. The backtracking algorithm is a straightforward and intuitive way to solve and generate Sudoku puzzles, and it can be easily adapted for different board sizes. The data structures used, mainly lists of lists, are chosen for their simplicity and ease of access. Although the backtracking algorithm's worst-case time complexity can be high, in practice, it should perform reasonably well for solving and generating Sudoku puzzles.
* Performance Measurement: Supplement the analysis above with run-time measurements of multiple iterations of the game or puzzles as discussed in class. Sample results from a run-time profiler is a good idea at least as part of the measurements.

## Summary of work:

* Luwei Li: Generated the whole 4x4, 9x9, 16x16 sudoku board, the valid Sudoku Puzzle board. Implemented SAT solver function. Created UI for players. 
* Abhisha Tarimane: Implemented Thermo Sudoku function, Sandwich Sudoku function and User Interface. 
