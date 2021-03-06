"""
Project name: BOOK MANAGER
Author: MENIN THIBAUT & KOCOGLU LUCAS
Desc: This file manage bookreaders.
"""

######### MODULES / IMPORT #############

from manage_system.manage_files import write_file, read_file
from manage_system.utilities_func import position, has_read

######### MODULES / IMPORT #############

######### SETTINGS #############

from config import language
if language == "fr":
    from languages.language_fr import *
elif language == "en":
    from languages.language_en import *

######### SETTINGS #############

######### FUNCTIONS #############

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
	Remove book id in data/bookreaders.txt
	And drop the index of all the other books because a deleted book (moving index)
	This func is used only by removing book.
	User is not supposed to lie on readers book and will not be able to remove
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


def show_books_readed(username):
	"""
	Show books readed
	"""
	data_book = read_file("books")
	data_bookreaders = read_file("booksread")

	index = position(read_file("readers"), username)
	readed_book = data_bookreaders[index][1:]
	readed_book_name = [data_book[int(j)-1] for j in readed_book]

	print(text_show_book_readed_separator)
	for i in range(0, len(readed_book_name)):
		print(readed_book_name[i])
	print(text_show_book_readed_separator)

	return True


def add_bookreaded(username, marque=-1):
	"""
	Add readed book at the end of the line of user profile in data/booksread.txt
	"""
	
	data_book = read_file("books")

	print(text_add_bookreaded_separator)
	for i in range(0, len(data_book)):
		print(data_book[i])
	print(text_add_bookreaded_separator)
	while marque != 0:
		print(text_add_bookreaded_input_request_1)
		print(text_add_bookreaded_input_request_2)
		try:
			marque = int(input(text_add_bookreaded_input_1))
		except ValueError:
			marque = -1

		if marque == 0:
			return 'Ok'
		elif (marque >= 1) and (marque <= len(data_book)):
			if has_read(username, marque) == True:
				print(text_add_bookreaded_already_readed_book)
			else:
				data_bookreaders = read_file("booksread")
				for i in range(0, len(data_bookreaders)):
					if data_bookreaders[i][0] == username:
						data_bookreaders[i].append(str(marque))
						for j in range(1, len(data_bookreaders[i])):
							if marque < int(data_bookreaders[i][j]):
								for l in range((len(data_bookreaders[i]) - j)-1):
									data_bookreaders[i][(len(data_bookreaders[i])-1) - l] = data_bookreaders[i][(len(data_bookreaders[i])-2) - l]
								data_bookreaders[i][j] = str(marque)
								break
						write_file("booksread", data_bookreaders)
						print(text_add_bookreaded_book_added)
						break

				review_request = ""
				print(text_add_bookreaded_input_request_3)
				while review_request not in ["Yes", "yes", "Y", "y", "YES", "oui", "Oui", "o", "OUI", "O"]:
					review_request = str(input(text_add_bookreaded_input_2))
					if review_request in ["No", "no", "n", "N", "NO", "Non", "non", "NON"]:
						return 'Ok'

				return marque

	return 'Ok'

######### FUNCTIONS #############
