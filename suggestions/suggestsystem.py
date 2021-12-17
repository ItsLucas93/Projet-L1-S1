from manage_system.manage_files import read_file, write_file

# Implémenter la matrice de notation à stocker
def rating_matrix():
	M = []
	for i in range(0, len(read_file("readers"))):
		temp = []
		for j in range(0, len(read_file("books"))):
			temp.append(0)
		M.append(temp)

	write_file("rating_matrix", M)

def review_book():
	return True


def suggested_book():
	return True