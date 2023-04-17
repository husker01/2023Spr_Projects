import copy
from sat_utils import solve_one, one_of, basic_fact, solve_all
from sys import intern
from itertools import chain
import random



def SudokuSolver(SIZE, num_to_remove, board):
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
        new_board = copy.deepcopy(board)
        for i in range(num_to_remove):
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
            while board[row][col] == 0:
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board[0]) - 1)
            new_board[row][col] = 0
        return new_board


    def solver(board):
        flatten_board_chr = ''
        flatten_board = list(map(str, list(chain.from_iterable(board))))
        for item in flatten_board:
            flatten_board_chr += mapping[item]
        cnf = []

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

        # solve it and display the results
        num_solutions = len(solve_all(cnf))
        solutions = solve_all(cnf)
        return num_solutions, solutions


    def generate_puzzle():
        solution_board = []
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
        return puzzle_board, solution_board

    return generate_puzzle()

