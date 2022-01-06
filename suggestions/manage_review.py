"""
Project name: BOOK MANAGER
Author: MENIN THIBAUT & KOCOGLU LUCAS
Desc: This file manage reviews
"""

######### MODULES / IMPORT #############

from manage_system.manage_files import read_file, write_file

from manage_system.utilities_func import position

######### MODULES / IMPORT #############

######### SETTINGS #############

from config import language
if language == "fr":
	from languages.language_fr import *
elif language == "en":
	from languages.language_en import *

######### SETTINGS #############

######### FUNCTIONS #############

def review_book(username, position_user, id_book_review=-1):
	"""
	This func is used to give a grade a book and is stocked into /data/rating_matrix.txt
	with:
		i : index user
		j : index book
	example:
		0 0 0 0 0 0
		0 0 0 0 0 0
		0 0 0 3 0 0
		0 0 0 0 0 0
		0 0 0 0 0 0
	user with index 2 gived 3/5 to book 4
	"""

	if id_book_review == -1:
		data_book = read_file("books")
		data_bookreaders = read_file("booksread")

		print("\n" + text_review_book_show_user_books_readed_separator)
		print(text_review_book_show_user_books_readed, end="")

		temp = []
		for i in data_bookreaders:
			if i[0] == username:
				for j in i[1:]:
					temp.append(j)

		for i in temp:
			print(data_book[int(i)-1] + " (" + text_review_book_show_user_books_note + " : " + str(get_review_book(username, position(read_file("readers"), username), int(i))) + "/5)", end="\n")
		print(text_review_book_show_user_books_readed_separator)

	while id_book_review < 0 or id_book_review > len(read_file("books")):
		try:
			id_book_review = int(input(text_review_book_input_request_1))
		except ValueError:
			id_book_review = -1

		if id_book_review == 0:
			return True
		elif has_read(username, id_book_review) is False:
			id_book_review = -1
			print(text_review_book_input_request_not_readed)

	notation = -1
	while (notation <= 0) or (notation > 5):
		try:
			notation = int(input(text_review_book_input_request_2))
		except ValueError:
			notation = -1

	index_user = position_user # position(read_file("readers"), username)

	data_rating_matrix = read_file("rating_matrix")
	data_rating_matrix[index_user][id_book_review-1] = str(notation)
	write_file("rating_matrix", data_rating_matrix)

	return True


def get_review_book(username, position_user, id_book_review=-1):
	"""
	Get the grade of the book by user
	NE is Not Evaluated (en) / Non évalué (fr)
	"""
	data_rating_matrix = read_file("rating_matrix")
	index_user = position_user # position(read_file("readers"), username)
	notation = data_rating_matrix[index_user][id_book_review-1]

	if notation == '0':
		notation = "NE"
	return notation


def has_read(username, marque):
	"""
	Verify if the user has read the book
	"""
	data = read_file("booksread")

	for i in data:
		if i[0] == username:
			for k in i:
				if k == str(marque):
					return True
	return False

######### FUNCTIONS #############
