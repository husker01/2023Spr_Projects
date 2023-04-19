import random
import copy
import math
from sudoku_solver import SudokuSolver
import pygame
import sys

class Sudoku:
    def __init__(self, SIZE, level):
        # Define the size of the board
        self.SIZE = SIZE
        self.level = level
        # initialize the numbers to be removed
        self.empty_cell_coordinate = []
        self.num_to_remove = 0
        self.board = self.generate_random_solution()
        self.puzzle_board, self.solution = self.play_game()

    # ------------------------------------------------------------------------------------------
    # generate the complete and valid sudoku board

    def select_difficulty(self, level):
        if level == 1:
            self.num_to_remove = int(0.5 * self.SIZE ** 2)
        elif level == 2:
            self.num_to_remove = int(0.6 * self.SIZE ** 2)
        elif level == 3:
            self.num_to_remove = int(0.67 * self.SIZE ** 2)
        return self.num_to_remove

    # print the board to the player
    def print_board(self, board):
        print("- " * self.SIZE + "- " * int(math.sqrt(self.SIZE)))
        for i in range(self.SIZE):
            if i % int(math.sqrt(self.SIZE)) == 0 and i != 0:
                print("- " * self.SIZE + "- " * int(math.sqrt(self.SIZE)))
            for j in range(self.SIZE):
                if j % int(math.sqrt(self.SIZE)) == 0 and j != 0:
                    print(" | ", end="")

                if j == self.SIZE - 1:
                    print(board[i][j])

                else:
                    print(str(board[i][j]) + " ", end="")
                    # print("i=" + str(i) + " j=" + str(j))
        print("- " * self.SIZE + "- " * int(math.sqrt(self.SIZE)))
        print("\n")

    # Function to check if a number can be placed in a given cell
    def is_valid(self, board, row, col, num):
        # Check if the number is already present in the row or column
        for i in range(self.SIZE):
            if board[row][i] == num or board[i][col] == num:
                return False
        # Check if the number is already present in the subgrid
        sub_row = (row // int(math.sqrt(self.SIZE))) * int(math.sqrt(self.SIZE))
        sub_col = (col // int(math.sqrt(self.SIZE))) * int(math.sqrt(self.SIZE))
        for i in range(sub_row, sub_row + int(math.sqrt(self.SIZE))):
            for j in range(sub_col, sub_col + int(math.sqrt(self.SIZE))):
                if board[i][j] == num:
                    return False
        # If the number can be placed in the cell, return True
        return True

    # find empty cell
    def find_empty(self, board):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == 0:
                    return i, j
        return None

    def generate(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find
        numbers = []
        for i in range(1, self.SIZE + 1):
            numbers.append(i)
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


    def add_sandwich(self, board):
        horiz_list, vert_list = [], []
        for i in range(0, self.SIZE):
            horiz_sum, vert_sum = 0, 0
            is_horiz_start = False
            is_vert_start = False
            for j in range(0, self.SIZE):
                if (board[i][j] == 1 or board[i][j] == self.SIZE) and not is_horiz_start:
                    is_horiz_start = True
                elif (board[i][j] == 1 or board[i][j] == self.SIZE) and is_horiz_start:
                    is_horiz_start = False
                elif is_horiz_start:
                    horiz_sum += board[i][j]

                if (board[j][i] == 1 or board[j][i] == self.SIZE) and not is_vert_start:
                    is_vert_start = True
                elif (board[j][i] == 1 or board[j][i] == self.SIZE) and is_vert_start:
                    is_vert_start = False
                elif is_vert_start:
                    vert_sum += board[j][i]
            horiz_list.append(horiz_sum)
            vert_list.append(vert_sum)
        print("---------Sandwich----------------")
        print(horiz_list, vert_list)
        print("-----------------------------------")


    # generate the complete and valid board
    def generate_random_solution(self):
        # generate the all 0 board
        board = [[0 for x in range(self.SIZE)] for y in range(self.SIZE)]
        # generate the valid board
        self.generate(board)
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

        self.select_difficulty(level)

        # ----------------------------------------------------------------------------------------
        # remove numbers to create the puzzle board

        puzzle_board, solutions = SudokuSolver(self.SIZE, self.num_to_remove, copy_board)
        for i in range(len(puzzle_board[0])):
            for j in range(len(puzzle_board)):
                if puzzle_board[i][j] == 0:
                    self.empty_cell_coordinate.append((i, j))
        return puzzle_board, solutions


class SudokuGUI:
    def __init__(self, sudoku, screen_width=900, screen_height=600):
        pygame.init()
        self.sudoku = sudoku
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.cell_size = self.screen_height // sudoku.SIZE
        self.font = pygame.font.Font(None, self.cell_size // 2)
        self.selected_cell = None

        # Create buttons
        self.button_font = pygame.font.Font(None, 30)
        self.check_solution_rec = pygame.Rect(650, 80, 200, 50)

        self.new_game_button = pygame.Rect(650, 220, 200, 50)
        self.new_game_text = self.button_font.render("Start New Game", True, (0, 0, 0))
        self.quit_button = pygame.Rect(650, 290, 200, 50)
        self.quit_text = self.button_font.render("Quit Game", True, (0, 0, 0))
        self.run()

    def draw_buttons(self):
        pygame.draw.rect(self.screen, (192, 192, 192), self.new_game_button)
        pygame.draw.rect(self.screen, (192, 192, 192), self.quit_button)
        pygame.draw.rect(self.screen, (192, 192, 192), self.check_solution_rec)
        self.screen.blit(self.new_game_text, (665, 230))
        self.screen.blit(self.quit_text, (685, 300))


    def highlight_cell(self, row, col):
        cell_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (173, 216, 230), cell_rect, 0)

    def draw_board(self):
        self.screen.fill((255, 255, 255))

        # Add this line to get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i in range(self.sudoku.SIZE + 1):
            line_thickness = 3 if i % int(self.sudoku.SIZE ** 0.5) == 0 else 1
            pygame.draw.line(
                self.screen, (0, 0, 0),
                (i * self.cell_size, 0),
                (i * self.cell_size, self.screen_height),
                line_thickness
            )
            pygame.draw.line(
                self.screen, (0, 0, 0),
                (0, i * self.cell_size),
                (self.screen_height, i * self.cell_size),
                line_thickness
            )

        # Add these lines to highlight the cell under the mouse
        row, col = self.get_cell_from_mouse(mouse_x, mouse_y)
        if col < self.sudoku.SIZE and row < self.sudoku.SIZE:  # Check if the mouse is within the board
            self.highlight_cell(row, col)

        for row in range(self.sudoku.SIZE):
            for col in range(self.sudoku.SIZE):
                cell_value = self.sudoku.puzzle_board[row][col]
                if (row, col) not in self.sudoku.empty_cell_coordinate:
                    text_color = (200, 0, 0)
                else:
                    text_color = (0, 0, 0)
                if cell_value != 0:
                    # Convert values 10-16 to hexadecimal characters
                    cell_text = hex(cell_value)[2:].upper()
                    num_text = self.font.render(cell_text, True, text_color)
                    x = col * self.cell_size + self.cell_size // 3
                    y = row * self.cell_size + self.cell_size // 5
                    self.screen.blit(num_text, (x, y))
        self.draw_buttons()
        pygame.display.flip()

    def get_cell_from_mouse(self, mouse_x, mouse_y):
        return mouse_y // self.cell_size, mouse_x // self.cell_size

    def start_new_game(self):
        # Create a new instance of the Sudoku class
        new_sudoku = Sudoku(self.sudoku.SIZE, self.sudoku.level)
        # Update the sudoku attribute of the SudokuGUI class
        self.sudoku = new_sudoku
        # Clear the selected cell
        self.selected_cell = None
        # Redraw the board with the new puzzle
        self.draw_board()
    def handle_click(self, mouse_x, mouse_y):
        row, col = self.get_cell_from_mouse(mouse_x, mouse_y)
        if self.new_game_button.collidepoint(mouse_x, mouse_y):
            print("Clicked New Game button")
            self.start_new_game()
            # Add code to start a new game
        elif self.quit_button.collidepoint(mouse_x, mouse_y):
            print("Clicked Quit button")
            pygame.quit()
            sys.exit()
        else:
            self.selected_cell = (row, col)
            print(f"Clicked cell: ({row + 1}, {col + 1})")

    def handle_key(self, key):
        if self.selected_cell is not None:
            key_name = pygame.key.name(key)
            input_values = [str(i) for i in range(1, 17)]

            # Check if the key name is in the range 1-9 or if it is a, b, c, d, e or f
            if key_name in input_values or key_name in ['a', 'b', 'c', 'd', 'e', 'f']:
                row, col = self.selected_cell
                if (row, col) in self.sudoku.empty_cell_coordinate:
                    # Convert the input value to an integer, handling letters for values 10-16
                    if key_name in input_values:
                        value = int(key_name)
                    else:
                        value = int(key_name, 16)

                    self.sudoku.puzzle_board[row][col] = value
                    self.draw_board()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(*event.pos)
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)
            self.draw_board()
            self.draw_buttons()
            if self.sudoku.puzzle_board == self.sudoku.solution:
                # Display a message on the screen
                congratulation_text = self.button_font.render("Congratulations!", True, (0, 0, 0))
                text_rect = congratulation_text.get_rect(center=(750, 100))
                self.screen.blit(congratulation_text, text_rect)
                pygame.display.flip()
            else:
                # Display a message on the screen
                try_again_text = self.button_font.render("Incorrect Solution", True, (200, 0, 0))
                text_rect = try_again_text.get_rect(center=(750, 100))
                self.screen.blit(try_again_text, text_rect)
                pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    # select the size of the sudoku game
    print("Please choose the size of the sudoku (size x size)")
    SIZE = int(input("Enter Size 4: (4x4) or 9: (9x9) or 16: (16x16):"))
    print("Please choose the level of difficulty")
    print("1-easy (50% cells unknown), 2-medium (60% cells unknown), 3-hard (67% cells unknown)")
    level = int(input("Enter difficulty number (1-easy, 2-medium, 3-hard): "))
    sudoku = Sudoku(SIZE, level)
    gui = SudokuGUI(sudoku)

