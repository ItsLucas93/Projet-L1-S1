from manage_system.manage_files import write_file, read_file
from suggestions.suggestsystem import *

def add_bookreader(username):
	"""
	Add user in booksread
	"""
	write_file("booksreader_add", username)


def remove_bookreader(username):
	"""
	Remove user in booksread
	"""
	data = read_file("booksread")

	i = 0
	while (i < len(data)) and (data[i][0] != username):
		i += 1
	# Cas où l'utilisateur ne figure pas dans la base car i > len(data)
	if i > len(data):
		return False
	# Cas où l'utilisateur figure dans la base
	else:
		data.pop(i) # or del data[i]
		write_file("booksread", data)
		return True

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


def has_read(username, marque):
	data = read_file("booksread")

	for i in data:
		if i[0] == username:
			for k in i:
				if k == str(marque):
					return True
	return False

def add_bookreaded(username, marque=-1):


	data_book = read_file("books")

	print("------------BOOKS LIST------------")
	for i in range(0, len(data_book)):
		print(data_book[i])
	print("------------BOOKS LIST------------")
	while marque != 0:
		print("Please enter the id of the book you want to add to your profile.")
		print("If you want to exit, please enter 0")
		try:
			marque = int(input("Your input : "))
		except ValueError:
			marque = -1

		if marque == 0:
			return True
		elif (marque >= 1) and (marque <= len(data_book)):
			if has_read(username, marque) == True:
				print("You're already readed the book ! Please try another book")
			else:
				data_bookreaders = read_file("booksread")
				for i in range(0, len(data_bookreaders)):
					if data_bookreaders[i][0] == username:
						data_bookreaders[i].append(str(marque))
						write_file("booksread", data_bookreaders)
						break
	return True