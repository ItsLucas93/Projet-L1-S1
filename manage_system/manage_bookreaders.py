from manage_system.manage_files import write_file, read_file


def add_bookreader(username):
	"""
	Add user in booksread
	"""
	write_file("booksreader_add", username)


def remove_bookread(marque):
	"""
	Remove book id in data/bookread.txt
	"""
	bookread = read_file("booksread")
	marque += 1
	for i in range(0, len(bookread)):
		for j in range(0, len(bookread[i])):
			if marque == bookread[i][j]:
				del bookread[i][j]
				break
	write_file("booksread", bookread)