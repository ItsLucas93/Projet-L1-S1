from manage_system.manage_files import read_file, write_file

def rating_matrix_init():
	M = []
	for i in range(0, len(read_file("readers"))):
		temp = []
		for j in range(0, len(read_file("books"))):
			temp.append('0')
		M.append(temp)

	write_file("rating_matrix", M)


def update_rating_matrix(reason, indice):

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