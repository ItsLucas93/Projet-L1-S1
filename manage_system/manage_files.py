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
				data[i] = remove_antislashn(data[i])


	elif path == "booksread":
		path = path_booksread

		with open(path, 'r', encoding="UTF-8") as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = remove_antislashn(data[i])
			for i in range(0, len(data)):
				data[i] = data[i].split(',')



	elif path == "readers":
		path = path_readers

		with open(path, 'r', encoding="UTF-8") as f:
			data = f.readlines()
			for i in range(0, len(data)):
				data[i] = remove_antislashn(data[i])
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
			f.write("\n" + str(len(liste)+1) + " - " + liste)


	elif path == "books":
		path = path_books

		with open(path,'w', encoding="UTF-8") as f:
			for i in range(0, len(liste) - 1):
				f.write(str(i+1) + " - " + liste[i] + "\n")
			f.write(str(i+1) + " - " + liste[-1])


	elif path == "booksreader_add":
		path = path_booksread

		with open(path,"a", encoding="UTF-8") as f:
			f.write("\n" + liste)

	# modifier pour ajouter derrière le username
	elif path == "booksread":
		path = path_booksread

		liste = assemble_liste_2d(liste)
		with open(path,'w', encoding="UTF-8") as f:
			for i in range(0, len(liste) - 1):
				f.write(liste[i] + "\n")
			f.write(liste[-1])


	elif path == "readers_add":
		path = path_readers

		with open(path,'a', encoding="UTF-8") as f:
			f.write("\n" + assemble_liste_1d(liste))


	elif path == "readers":
		path = path_readers

		with open(path,'w', encoding="UTF-8") as f:
			liste = assemble_liste_2d(liste)
			for i in range(0, len(liste) - 1):
				f.write(liste[i] + "\n")
			f.write(liste[-1])


def assemble_liste_1d(liste):
	"""
	Assemble list in char before write_file
	"""
	char = ""
	for i in range(0, len(liste) - 1):
		char += str(liste[i]) + ','
	char += str(liste[-1])
	return char


def assemble_liste_2d(liste):
	"""
	Assemble lists in list before write_file
	"""
	temp = []
	for i in range(0, len(liste)):
		char = ""
		for j in range(0, len(liste[i])-1):
			char += str(liste[i][j]) + ','
		char += str(liste[i][-1])
		temp.append(char)
	return temp


def remove_antislashn(charactere):
	"""
	Retire l'antislash n de la chaîne de caractère
	"""
	if charactere[-1] == "\n":
		charactere = charactere[:-1]
	return charactere


def regenerate_file():
	"""
	à utiliser seulement en cas de reset, très explosif
	écrase tt
	"""
	path = path_readers
	with open(path, 'w', encoding="UTF-8") as f:
		f.write("Gilbert,1,2,1\nWilliam,3,3,7\nAlienRoXoR17,2,1,3\nanonyme,3,3,2\nLecteur_assidu,1,1,3\nharipoteur,3,2,5\nLili,2,2,2\nArchiBald_fx,1,3,4\n")

	path = path_books
	with open(path, 'w', encoding="UTF-8") as f:
		f.write("Long Walk to Freedom\nThings I Did and Things I Think I Did\nThe Bloody Chamber\nThe Memoirs of an Amnesiac\nThe Silence of the Lambs\nThe Hunger\nWild Eyes\nWhite Teeth\nThe Resisters\nThe Power\n")

	path = path_readers
	with open(path, 'w', encoding="UTF-8") as f:
		f.write("Gilbert,5,7,8,9\nWilliam,1,8,9,10\nAlienRoXoR17,3,4,5,6,10\nAnonyme,1,2,4,7\nLecteur_assidu,1,2,3,5,6,8,9,10\nHaripoteur,3,5,8,9,10\nLili,1,2,4,6,8,10\nArchiBald_fx,7,9,10\n")
