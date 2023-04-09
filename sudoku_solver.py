import copy
from sat_utils import solve_one, one_of, basic_fact, solve_all
from sys import intern
from itertools import chain
import random
from pprint import pprint

flatten_board_string = ''
puzzle_board = []
num_to_remove = 100
SIZE = 16
board = [[9, 4, 7, 3, 8, 2, 5, 6, 1],
         [1, 3, 6, 4, 5, 9, 8, 2, 7],
         [2, 5, 8, 7, 1, 6, 4, 9, 3],
         [7, 1, 2, 5, 4, 8, 9, 3, 6],
         [5, 8, 9, 6, 7, 3, 1, 4, 2],
         [4, 6, 3, 9, 2, 1, 7, 5, 8],
         [8, 2, 4, 1, 6, 5, 3, 7, 9],
         [3, 7, 1, 2, 9, 4, 6, 8, 5],
         [6, 9, 5, 8, 3, 7, 2, 1, 4]]
board = [[2, 4, 1, 3], [3, 1, 2, 4], [1, 3, 4, 2], [4, 2, 3, 1]]

board = [[7, 3, 10, 16, 8, 2, 4, 9, 14, 5, 1, 12, 11, 15, 6, 13],
 [15, 5, 1, 8, 12, 6, 14, 3, 16, 13, 2, 11, 7, 10, 4, 9],
 [14, 12, 13, 2, 10, 1, 11, 15, 4, 9, 6, 7, 3, 16, 8, 5],
 [4, 6, 11, 9, 7, 5, 16, 13, 3, 8, 15, 10, 2, 1, 12, 14],
 [2, 13, 6, 14, 11, 3, 9, 8, 10, 1, 4, 15, 16, 7, 5, 12],
 [1, 9, 12, 3, 2, 15, 10, 4, 11, 16, 7, 5, 6, 13, 14, 8],
 [10, 8, 5, 7, 16, 12, 1, 14, 9, 2, 13, 6, 4, 3, 11, 15],
 [11, 15, 16, 4, 5, 13, 6, 7, 12, 3, 14, 8, 1, 9, 2, 10],
 [12, 10, 3, 5, 15, 14, 7, 16, 8, 4, 9, 2, 13, 11, 1, 6],
 [9, 7, 15, 13, 1, 4, 12, 10, 6, 14, 11, 3, 5, 8, 16, 2],
 [16, 14, 2, 6, 3, 11, 8, 5, 13, 7, 10, 1, 15, 12, 9, 4],
 [8, 11, 4, 1, 13, 9, 2, 6, 15, 12, 5, 16, 10, 14, 7, 3],
 [5, 2, 8, 12, 14, 10, 3, 11, 1, 15, 16, 4, 9, 6, 13, 7],
 [6, 1, 9, 11, 4, 7, 13, 12, 5, 10, 3, 14, 8, 2, 15, 16],
 [3, 16, 7, 15, 9, 8, 5, 1, 2, 6, 12, 13, 14, 4, 10, 11],
 [13, 4, 14, 10, 6, 16, 15, 2, 7, 11, 8, 9, 12, 5, 3, 1]]

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

del grid, subsquares, table     # analysis requires only:  points, values, groups

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


def remove_random_cell(board):
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board[0]) - 1)
    while board[row][col] == 0:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
    # num = board[row][col]
    new_board = copy.deepcopy(board)
    new_board[row][col] = 0
    return new_board


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
    solutions = len(solve_all(cnf))
    return solutions


def generate_puzzle():
    puzzle_board = remove_cell_from_board(board, num_to_remove)
    sol = solver(puzzle_board)
    while sol != 1:
        puzzle_board = remove_cell_from_board(board, num_to_remove)
        sol = solver(puzzle_board)
    return puzzle_board


print(generate_puzzle())