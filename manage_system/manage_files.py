path_books = "../data/books.txt"
path_booksread = "../data/booksread.txt"
path_readers = "../data/readers.txt"

def read_file(path):
	"""
	Lecture du fichier readers.txt
	"""

	# match(path):
	# 	case "books":
	# 		path = path_books
	# 	case "booksread":
	# 		path = path_booksread
	# 	case "path_readers":
	# 		path = path_readers

	if path == "books":
		path = path_books

		with open(path, 'r') as f:
		data = f.readlines()

	elif path == "booksread":
		path = path_booksread

		with open(path, 'r') as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = data[i].split(',')

	elif path == "readers":
		path = path_readers

		with open(path, 'r') as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = data[i].split(',')

	return data

def write_file(path, liste):
	"""
	Ecriture du fichier
	"""

	if path == "books":
		path = path_books

		with open(path,'w') as f:
			for i in range(0, len(liste)):
				f.write(liste[i])


	elif path == "booksread":
		path = path_booksread
	elif path == "readers":
		path = path_readers