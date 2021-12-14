path_books = "data/books.txt"
path_booksread = "data/booksread.txt"
path_readers = "data/readers.txt"
# Implémenter une fonction qui permet de modifier le path depuis la console 


def read_file(path):
	"""
	Lecture du fichier readers.txt
	"""

	# Python 3.10 case/match instead of if/else
	# match(path):
	# 	case "books":
	# 		path = path_books
	# 	case "booksread":
	# 		path = path_booksread
	# 	case "path_readers":
	# 		path = path_readers

	if path == "books":
		path = path_books

		with open(path, 'r', encoding="UTF-8") as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = antislashn(data[i])


	elif path == "booksread":
		path = path_booksread

		with open(path, 'r', encoding="UTF-8") as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = antislashn(data[i])
			for i in range(0, len(data)):
				data[i] = data[i].split(',')
			


	elif path == "readers":
		path = path_readers

		with open(path, 'r', encoding="UTF-8") as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = antislashn(data[i])
			for i in range(0, len(data)):
				data[i] = data[i].split(',')


	return data

def write_file(path, liste):
	"""
	Ecriture du fichier
	"""

	if path == "books_add":
		path = path_books

		with open(path,'a', encoding="UTF-8") as f:
			f.write("\n" + liste) # à valider


	elif path == "books":
		path = path_books

		with open(path,'w', encoding="UTF-8") as f:
			for i in range(0, len(liste)):
				f.write(liste[i])


	elif path == "booksread":
		path = path_booksread

		with open(path,'w', encoding="UTF-8") as f:
			for i in range(0, len(liste)):
				f.write(liste[i])		


	elif path == "readers":
		path = path_readers

		with open(path,'w', encoding="UTF-8") as f:
			for i in range(0, len(liste)):
				f.write(liste[i])



def antislashn(charactere):
	if charactere[-1] == "\n":
		charactere = charactere[:-1]
		return charactere




def regenerate_file():
	"""
	à utiliser seulement en cas de reset, très explosif
	"""