import copy
import itertools
from sat_utils import *
from sys import intern
from itertools import chain
import random


def SudokuSolver(SIZE, num_to_remove, board, sw_horizontal, sw_vertical, thermos):
    puzzle_board = []
    mapping = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
               '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '0': ' '}

    mapping_rev = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
                   'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16'}

    if SIZE == 4:
        grid = '''\
            AA AB BA BB 
            AC AD BC BD
            CA CB DA DB
            CC CD DC DD'''
    elif SIZE == 9:
        grid = '''\
        AA AB AC BA BB BC CA CB CC
        AD AE AF BD BE BF CD CE CF
        AG AH AI BG BH BI CG CH CI
        DA DB DC EA EB EC FA FB FC
        DD DE DF ED EE EF FD FE FF
        DG DH DI EG EH EI FG FH FI
        GA GB GC HA HB HC IA IB IC
        GD GE GF HD HE HF ID IE IF
        GG GH GI HG HH HI IG IH II'''
    elif SIZE == 16:
        grid = '''\
        AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
        AE AF AG AH BE BF BG BH CE CF CG CH DE DF DG DH
        AI AJ AK AL BI BJ BK BL CI CJ CK CL DI DJ DK DL
        AM AN AO AP BM BN BO BP CM CN CO CP DM DN DO DP
        EA EB EC ED FA FB FC FD GA GB GC GD HA HB HC HD
        EE EF EG EH FE FF FG FH GE GF GG GH HE HF HG HH
        EI EJ EK EL FI FJ FK FL GI GJ GK GL HI HJ HK HL
        EM EN EO EP FM FN FO FP GM GN GO GP HM HN HO HP
        IA IB IC ID JA JB JC JD KA KB KC KD LA LB LC LD
        IE IF IG IH JE JF JG JH KE KF KG KH LE LF LG LH
        II IJ IK IL JI JJ JK JL KI KJ KK KL LI LJ LK LL
        IM IN IO IP JM JN JO JP KM KN KO KP LM LN LO LP 
        MA MB MC MD NA NB NC ND OA OB OC OD PA PB PC PD
        ME MF MG MH NE NF NG NH OE OF OG OH PE PF PG PH
        MI MJ MK ML NI NJ NK NL OI OJ OK OL PI PJ PK PL
        MM MN MO MP NM NN NO NP OM ON OO OP PM PN PO PP'''
    if SIZE == 4:
        values = list('1234')
    elif SIZE == 9:
        values = list('123456789')
    elif SIZE == 16:
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    table = [row.split() for row in grid.splitlines()]
    points = grid.split()
    subsquares = dict()
    for point in points:
        subsquares.setdefault(point[0], []).append(point)
    # Groups:  rows   + columns           + subsquares
    groups = table[:] + list(zip(*table)) + list(subsquares.values())

    def comb(point, value):
        'Format a fact (a value assigned to a given point)'
        return intern(f'{point} {value}')

    def str_to_facts(s):
        'Convert str in row major form to a list of facts'
        return [comb(point, mapping_rev[value]) for point, value in zip(points, s) if value != ' ']

    def facts_to_str(facts):
        'Convert a list of facts to a string in row major order with blanks for unknowns'
        point_to_value = dict(map(str.split, facts))
        return ''.join(point_to_value.get(point, ' ') for point in points)

    def remove_cell_from_board(board, num_to_remove):
        """
        Removes the number of cells as per the user chosen difficulty level
        :param board: The solved board
        :param num_to_remove: Number of cells to be removed
        :return: The puzzle board
        """
        new_board = copy.deepcopy(board)
        for i in range(num_to_remove):
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
            while new_board[row][col] == 0:
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board[0]) - 1)
            new_board[row][col] = 0
        return new_board

    def solver(board):
        """
        The method which generates the CNF rules for the puzzle. Using the solve all method from sat_utils.py, each and
        every CNF rule is checked. If one of the rule doesn't satisfy then that board is discarded and next board is
        checked for validity until we find a single solution.
        :param board: The solution board
        :return: The solution boards and the number of solutions

        Big O Analysis:
            Big O can be calculated as O((m) + (3*m) + (n)) where m is the size of the board and n is the numbers
            already filled in the cell
                O(4m + n) => O(m+n)
        """
        flatten_board_chr = ''
        flatten_board = list(map(str, list(chain.from_iterable(board))))
        for item in flatten_board:
            flatten_board_chr += mapping[item]
        cnf = []
        variables = {}

        # Create Boolean variables for each cell
        # cells = [[solver.new_var() for j in range(SIZE)] for i in range(SIZE)]
        # poss_values = generate_possible_values(board, SIZE, points)
        # for value in poss_values:
        #     value2 = points[((value[0] + 1)*(value[1] + 1))-1]
        # for point in poss_values:
        #     cnf += one_of(comb(point, value) for value in poss_values[point])
        # each point assigned exactly one value
        for point in points:
            cnf += one_of(comb(point, value) for value in values)

        # each value gets assigned to exactly one point in each group
        for group in groups:
            for value in values:
                cnf += one_of(comb(point, value) for point in group)

        # add facts for known values in a specific puzzle
        for known in str_to_facts(flatten_board_chr):
            cnf += basic_fact(known)

        # add CNF rules for each group of thermos cells
        # for thermos_cell in thermos:
        #     for i in range(len(thermos_cell)):
        #         for j in range(i + 1, len(thermos_cell)):
        #             clause = []
        #             for k in range(len(thermos_cell[i])):
        #                 if thermos_cell[i][k] < thermos_cell[j][k]:
        #                     clause.append("~" + points[((thermos_cell[i][k] + 1)*(thermos_cell[j][k] + 1))-1])
        #                 else:
        #                     clause.append("~" + points[(((thermos_cell[j][k] + 1) * (thermos_cell[i][k] + 1)) - 1)])
        #
        #             cnf.append(clause)

        num_solutions = len(solve_all(cnf))
        solutions = solve_all(cnf)
        return num_solutions, solutions

    def get_sum_clause(variables, sum_value):
        # This function returns a list of clauses that ensure the sum of the given variables is equal to sum_value.

        n = len(variables)
        clauses = []

        # Ensure that the sum is greater than or equal to sum_value.
        for i in range(1, n):
            for subset in itertools.combinations(variables, i):
                clause = list

    def validate_sandwich(sand_board):
        """
        The method to validate the sandwich hints for the solved board
        :param sand_board: The solution board
        :return: True if the condition satisfies else False
        """
        horiz_list, vert_list = [], []
        for i in range(0, SIZE):
            horiz_sum, vert_sum = 0, 0
            is_horiz_start = False
            is_vert_start = False
            for j in range(0, SIZE):
                if (sand_board[i][j] == 1 or sand_board[i][j] == SIZE) and not is_horiz_start:
                    is_horiz_start = True
                elif (sand_board[i][j] == 1 or sand_board[i][j] == SIZE) and is_horiz_start:
                    is_horiz_start = False
                elif is_horiz_start:
                    horiz_sum += sand_board[i][j]

                if (sand_board[j][i] == 1 or sand_board[j][i] == SIZE) and not is_vert_start:
                    is_vert_start = True
                elif (sand_board[j][i] == 1 or sand_board[j][i] == SIZE) and is_vert_start:
                    is_vert_start = False
                elif is_vert_start:
                    vert_sum += sand_board[j][i]
            horiz_list.append(horiz_sum)
            vert_list.append(vert_sum)

        if horiz_list == sw_horizontal and vert_list == sw_vertical:
            return True
        return False

    def validate_thermos(thermo_board):
        """
        The method to validate thermos hints.
        :param thermo_board: The solution board
        :return: True if the condition satisfies else False
        """
        prev_value = 0
        for new_thermo in thermos:
            for each_cell in new_thermo:
                if prev_value and prev_value > thermo_board[each_cell[0]][each_cell[1]]:
                    return False
                elif new_thermo[0] == each_cell:
                    prev_value = thermo_board[each_cell[0]][each_cell[1]]
        return True

    def generate_puzzle():
        """
        Generates the puzzle board by emptying the number of cells as per the difficulty level. Then the puzzle board
        generated is solved using the solver. If there are more than 1 solution, then the board is looped to check
        if all the CNF rules satisfies. If one of the rules doesn't then that solution is discarded and the next
        solution is checked, until we arrive at a single solution.
        :return: The puzzle board for the user and the solution board for reference

        Big O Analysis:
            The Big O can be calculated as O(infinite) since in the worst case, and as the difficulty increases, the
            loop may execute infinitely to solve the boards
        """
        solution_board = []
        sol, solutions = 0, []
        puzzle_board = remove_cell_from_board(board, num_to_remove)
        sol, solutions = solver(puzzle_board)
        while sol != 1:
            puzzle_board = remove_cell_from_board(board, num_to_remove)
            sol, solutions = solver(puzzle_board)
        # display the solution board by the solver
        for num, item in enumerate(solutions[0]):
            if num % SIZE == 0:
                solution_board.append([])
            solution_board[-1].append(int(item.split(' ')[1]))
        if validate_sandwich(solution_board) and validate_thermos(solution_board):
            return puzzle_board, solution_board

    return generate_puzzle()
