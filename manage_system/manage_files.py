path_book = "../data/books.txt"
path_booksread = "../data/booksread.txt"
path_readers = "../data/readers.txt"

def read_file(path):
	"""
	Lecture du fichier readers.txt
	"""

	# match(path):
	# 	case "books":
	# 		path = path_book
	# 	case "booksread":
	# 		path = path_booksread
	# 	case "path_readers":
	# 		path = path_readers

	if path == "book":
		path = path_book
	elif path == "booksread":
		path = path_booksread
	elif path == "readers":
		path = path_readers

	with open(path, "r") as f:
		data = f.readlines()

	return data

def write_file(path, list):
	"""
	Ecriture du fichier
	"""

	if path == "book":
		path = path_book
	elif path == "booksread":
		path = path_booksread
	elif path == "readers":
		path = path_readers