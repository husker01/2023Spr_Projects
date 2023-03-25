import random
import copy


class Sudoku:

    def __init__(self):
        # Define the size of the board
        self.SIZE = 9
        # initialize the numbers to be removed
        self.num_to_remove = 0

    # ------------------------------------------------------------------------------------------
    # generate the complete and valid sudoku board

    def select_difficulty(self, level):
        if level == 1:
            self.num_to_remove = 40
        elif level == 2:
            self.num_to_remove = 50
        elif level == 3:
            self.num_to_remove = 55
        return self.num_to_remove

    # print the board to the player
    def print_board(self, board):
        print("- - - - - - - - - - - - -")
        for i in range(self.SIZE):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - -")
            for j in range(self.SIZE):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")
        print("- - - - - - - - - - - - -")
        print("\n")

    # Function to check if a number can be placed in a given cell
    def is_valid(self, board, row, col, num):
        # Check if the number is already present in the row or column
        for i in range(self.SIZE):
            if board[row][i] == num or board[i][col] == num:
                return False
        # Check if the number is already present in the 3x3 subgrid
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, sub_row + 3):
            for j in range(sub_col, sub_col + 3):
                if board[i][j] == num:
                    return False
        # If the number can be placed in the cell, return True
        return True

    # find empty cell

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def generate(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        # Try placing numbers from 1 to 9 in the cell
        for num in numbers:
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                # Recursively solve the board
                if self.generate(board):
                    return True
                # If no solution is found, backtrack and try the next number
                board[row][col] = 0
        return False

    # generate the complete and valid board
    def generate_random_solution(self):
        # generate the all 0 board
        board = [[0 for x in range(self.SIZE)] for y in range(self.SIZE)]
        # generate the valid board
        self.generate(board)
        return board

    # ----------------------------------------------------------------------------------------
    # removing the numbers to create the puzzle board

    # Function to solve the Sudoku board using backtracking and return the number of solutions
    def solve(self, board, count_solutions=False):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if board[row][col] == 0:
                    solutions = 0
                    for num in range(1, self.SIZE + 1):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            # Recursively solve the board
                            if count_solutions:
                                solutions += self.solve(board, count_solutions)
                            elif self.solve(board):
                                return 1
                            # If no solution is found, backtrack and try the next number
                            board[row][col] = 0
                    return solutions if count_solutions else 0
        return 1 if count_solutions else 0

    # Function to remove numbers from the Sudoku board while ensuring unique solution
    def remove_numbers(self, board, num_to_remove):
        cells = [(i, j) for i in range(self.SIZE) for j in range(self.SIZE)]

        random.shuffle(cells)

        for cell in cells:
            row, col = cell
            num = board[row][col]
            board[row][col] = 0

            board_copy = [row[:] for row in board]
            solutions = self.solve(board_copy, count_solutions=True)

            if solutions != 1:
                board[row][col] = num
            else:
                num_to_remove -= 1

            if num_to_remove == 0:
                break
        return board

    # ----------------------------------------------------------------------------------------
    # Build a solver to solve the puzzle board

    def puzzle_solver(self, puzzle_board):
        solver_board = copy.deepcopy(puzzle_board)
        self.generate(solver_board)
        return solver_board

    # ----------------------------------------------------------------------------------------
    # check if the solver solution matches the original puzzle that is generated by generator
    def check_solver_solution(self, solver_solution_board, board, show=False):
        if show:
            if solver_solution_board == board:
                print('The solver solution matches the original puzzle from generator\n')
                print('-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x\n')
            else:
                print('The solver fail to solve the puzzle\n')
                print('-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x\n')

    # ----------------------------------------------------------------------------------------
    # player User Interface for the Sudoku game

    def play_game(self):
        # generate the valid board
        board = self.generate_random_solution()
        print('valid and solved board, hidden to player')
        self.print_board(board)
        copy_board = copy.deepcopy(board)

        # New game starts here
        print("Welcome to the Sudoku game!\n")

        # select game difficulty
        print("Please choose the level of difficulty")
        print("1-easy (40 cells unknown), 2-medium (50 cells unknown), 3-hard (55 cells unknown)")
        level = int(input("Enter difficulty number (1-easy, 2-medium, 3-hard): "))
        self.select_difficulty(level)

        # remove numbers to create the puzzle board
        puzzle_board = self.remove_numbers(copy_board, self.num_to_remove)
        print('puzzle board')
        self.print_board(puzzle_board)

        # implement the solver engine to solve the puzzle
        solver_solution_board = self.puzzle_solver(puzzle_board)
        print('solver_solution')
        self.print_board(solver_solution_board)

        # check if the solver engine matches the original valid board
        self.check_solver_solution(solver_solution_board, board, show=True)

        # input the number in the selected cell to solve the puzzle
        print("Enter the number for the empty cells or 0 to leave it empty")
        print("\n")
        self.print_board(puzzle_board)
        while True:
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                num = int(input("Enter number (0-9): "))
                if num not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    raise ValueError
                if row < 0 or row > 8 or col < 0 or col > 8:
                    raise ValueError
                if puzzle_board[row][col] == 0:
                    puzzle_board[row][col] = num
                    self.print_board(puzzle_board)
                else:
                    print("This cell is not empty. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
            if puzzle_board == solver_solution_board:
                print("Congratulations! You have solved the puzzle.")
                break


if __name__ == '__main__':
    game = Sudoku()
    game.play_game()
