from manage_system.manage_files import write_file, read_file


def add_bookreader(username):
	"""
	Add user in booksread
	"""
	write_file("booksreader_add", username)


def remove_bookread(marque):
	"""
	Remove book id in data/bookread.txt
	Et baisse l'indice de tous les autres livres car un livre supprimé (indice mobile)
	"""
	bookread = read_file("booksread")
	marque += 1
	for i in range(0, len(bookread)):
		for j in range(0, len(bookread[i])):
			if (j > 0) and (marque == int(bookread[i][j])):
				del bookread[i][j]
				break
		for j in range(len(bookread[i])):
			if (j > 0) and (marque < int(bookread[i][j])):
				bookread[i][j] = int(bookread[i][j]) - 1
	write_file("booksread", bookread)