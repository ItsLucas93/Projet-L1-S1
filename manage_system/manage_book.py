"""
Project name: BOOK MANAGER
Author: MENIN THIBAUT & KOCOGLU LUCAS
Desc: This file manage books.
"""

######### MODULES / IMPORT #############
from manage_system.manage_files import read_file, write_file
from manage_system.manage_bookreaders import remove_bookread

from suggestions.updater_matrix import update_rating_matrix

######### MODULES / IMPORT #############

######### SETTINGS #############

from config import language
if language == "fr":
    from languages.language_fr import *
elif language == "en":
    from languages.language_en import *

######### SETTINGS #############

######### FUNCTIONS #############

def add_book(new_book=""):
	"""
	Add book in /data/books.txt
	"""
	new_book = str(input(text_add_book_input_request))

	if book_exist(new_book):
		print(text_add_book_input_fail)

	while book_exist(new_book):
		new_book = str(input(text_add_book_input_request))
		if book_exist(new_book):
			print(text_add_book_input_fail)

	write_file("books_add", new_book)
	update_rating_matrix("add_book", None)

	return True


def delete_book(less_book=""):
	"""
	Remove book in /data/books.txt
	"""

	show_books()

	less_book = str(input(text_delete_book_input_request))

	while book_exist(less_book) == False:
		less_book = str(input(text_delete_book_input_request))

	book_liste = read_file("books")
	book_liste = del_indice(book_liste)

	for i in range(len(book_liste)):
		if less_book == book_liste[i]:
			marque = i

	del book_liste[marque]

	write_file("books", book_liste)
	remove_bookread(marque)
	update_rating_matrix("remove_book", marque)

	return True


def book_exist(verif_book):
	"""
	Verify if book exist /data/books.txt
	"""

	books = read_file("books")
	books = del_indice(books)

	for i in books:
		if verif_book == i:
			return True
	return False


def modify_book(old_book="", update_book=""):
	"""
	Modify name of book in /data/books.txt
	"""

	show_books()

	while book_exist(old_book) == False:
		old_book = str(input(text_modify_book_input_request_1))
	update_book = str(input(text_modify_book_input_request_2))

	while book_exist(update_book):
		update_book = str(input(text_modify_book_input_request_2))

	books = read_file("books")
	books = del_indice(books)

	for i in range(len(books)):
		if books[i] == old_book:
			books[i] = update_book
			break

	write_file("books", books)
	return True


def del_indice(books):
	"""
	Permet d'avoir que les titres des livres sans les indices
	"""
	k = 0
	for i in books:
		place = 0
		for j in i:  # permet de comparer sans les indices
			place += 1
			if j == "-":
				break
		p = place + 1
		chara = i
		chara = chara[p:]
		books[k] = chara
		k += 1
	return books


def show_books():
	"""
	Show books in data/books
	"""

	data = read_file("books")

	print(text_show_book_separator)

	for i in range(0, len(data)):
		print(data[i])

	print(text_show_book_separator)

	return True

######### FUNCTIONS #############

