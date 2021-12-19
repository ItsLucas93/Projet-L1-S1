"""
Project name: BOOK MANAGER
Author: MENIN THIBAUT & KOCOGLU LUCAS
Desc: This file update matrix
"""

######### MODULES / IMPORT #############

from manage_system.manage_files import read_file, write_file

######### MODULES / IMPORT #############

######### FUNCTIONS #############

def rating_matrix_init():
	"""
	reset to factory data the rating matrix
	"""
	# M = []
	# for i in range(0, len(read_file("readers"))):
	# 	temp = []
	# 	for j in range(0, len(read_file("books"))):
	# 		temp.append('0')
	# 	M.append(temp)

	M = [
		['0', '0', '0', '0', '1', '0', '2', '3', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['2', '0', '0', '0', '0', '0', '0', '4', '1', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['0', '0', '4', '2', '3', '5', '0', '0', '0', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['4', '3', '0', '3', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['2', '1', '4', '0', '4', '4', '0', '3', '2', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['0', '0', '2', '0', '2', '0', '0', '3', '2', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['5', '2', '0', '4', '0', '2', '0', '2', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		['0', '0', '0', '0', '0', '0', '4', '0', '2', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0']
	]

	write_file("rating_matrix", M)


def update_rating_matrix(reason, indice):
	"""
	add or delete user/book in the rating matrix
	"""

	data_rating_matrix = read_file("rating_matrix")

	if reason == "add_user":
		temp = []
		for i in range(0, len(read_file("books"))):
			temp.append('0')
		data_rating_matrix.append(temp)


	elif reason == "remove_user":
		del data_rating_matrix[indice]


	elif reason == "add_book":
		for j in range(0, len(data_rating_matrix)):
			data_rating_matrix[j].append('0')


	elif reason == "remove_book":
		for j in range(0, len(data_rating_matrix)):
			del data_rating_matrix[j][indice]


	write_file("rating_matrix", data_rating_matrix)


def suggest_matrix_init():
	"""
	reset suggest matrix
	"""
	M = []
	for i in range(0, len(read_file("readers"))):
		temp = []
		for j in range(0, len(read_file("readers"))):
			temp.append('0')
		M.append(temp)
	write_file("suggest_matrix", M)


def update_suggest_matrix(reason, indice):
	"""
	add or delete user in the suggest matrix
	"""

	data_suggest_matrix = read_file("suggest_matrix")

	if reason == "add_user":
		temp = []
		for i in range(0, len(read_file("readers"))):
			temp.append('0')
		data_suggest_matrix.append(temp)
		for i in range(0, len(read_file("readers"))-1):
			data_suggest_matrix[i].append('0')


	elif reason == "remove_user":
		del data_suggest_matrix[indice]
		for i in range(0, len(data_suggest_matrix)):
			del data_suggest_matrix[i][indice]

	write_file("suggest_matrix", data_suggest_matrix)

######### FUNCTIONS #############