# Daniela Rodrigues nr: 84919
# Miguel Viegas 	nr: 84747
# Grupo 6

import search
from utils import print_table
from copy import deepcopy

# TAI color 
# sem cor = 0 
# com cor > 0 

def get_no_color():     
	return 0 

def no_color (c):     
	return c==0 

def color (c):     
	return c > 0



# TAI pos 
# Tuplo (l, c) 

def make_pos (l, c):     
	return (l, c) 

def pos_l (pos):     
	return pos[0] 

def pos_c (pos):     
	return pos[1]



# Board Methods

def board_find_groups(board):	#falta garantir que não estou nos cantos e que posso andar

	#Vai adicionando ao vector de resultados
	#result.extend(tuple(pos));

	#Verifica posicao a cima
	#posAux = make_pos( (pos_l(pos)-1), pos_c(pos))
	#colorAux = board[pos_l(posAux)][pos_c(posAux)]
	

	#if(colorAux == color) and (posAux not in result):
		#result = find_groups(board, posAux, color, result)

	#Verifica posicao a baixo
	#posAux = make_pos( (pos_l(pos)+1), pos_c(pos))
	#colorAux = board[pos_l(posAux)][pos_c(posAux)]

	#if (colorAux == color) and (posAux not in result):
		#result = find_groups(board, posAux, color, result)
	
	#Verifica posicao a esquerda
	#posAux = make_pos(pos_l(pos), (pos_c(pos)-1))
	#colorAux = board[pos_l(posAux)][pos_c(posAux)]

	#if (colorAux == color) and (posAux not in result):
		#result = find_groups(board, posAux, color, result)
	
	#Verifica posicao a direita
	#posAux = make_pos(pos_l(pos), (pos_c(pos)+1))
	#colorAux = board[pos_l(posAux)][pos_c(posAux)]

	#if (colorAux == color) and (posAux not in result):
		#result = find_groups(board, posAux, color, result)

	#return result
	pass


def board_remove_group(board, group):

	# Gets the board size
	nr_lines = len(board)
	nr_colums = len(board[0])

	# Making a copy of the board
	result_board = deepcopy(board)

	# Scans the board and removes the group
	for pos in group:
		line = pos_l(pos)
		column = pos_c(pos)
		result_board[line][column] = get_no_color()

	# Activates GRAVITY!!!
	# Pulls the colors down so there isn't any "no color" in between the pieces on the board
	#
	# Can be easily optimized
	# This processes the entire matrix, instead of the specific columns
	for i in range(nr_lines):
		for j in range(nr_colums):
			if no_color(result_board[i][j]):
				# pulls down all the pieces from above for this particular position
				for k in range(i, -1, -1):
					if k != 0:
						result_board[k][j] = result_board[k-1][j]
					else:
						result_board[k][j] = get_no_color()

	# Pulls the pieces to the left side
	# It first stores the index's in a vector, then, for each index, it shrinks the matrix by one.
	# 	It then puts zeros in the right side of the matrix.
	lim = nr_lines - 1

	# Limits the shrinking. Excludes the final "no colors"
	for i in range(nr_colums - 1, -1, -1):
		if no_color(result_board[nr_lines - 1][i]):
			lim = i
		else:
			i = 0
			break

	# Actually shrinks
	i = 0
	while i < lim:
		if no_color(result_board[nr_lines - 1][i]):
			for j in range(len(result_board)):
				line = result_board[j]
				result_board[j] = line[:i] + line[i+1:] + [0]
		else:
			i = i + 1

	return result_board





# TESTE DE MERDA

# b = [[1,1,1,1,1],[1,1,2,1,1],[1,1,2,1,1],[1,2,1,2,1]] 
# g = [(0,2),(1,2),(2,2),(3,2),(3,3),(3,1)]

# print("Table:")
# print_table(table = b)
# print("Group:")
# print(g)
# print("==================")
# print_table(table = board_remove_group(b,g))
