from manage_system.manage_files import read_file, write_file
from manage_system.manage_bookreaders import remove_bookread

from suggestions.updater_matrix import update_rating_matrix


def add_book(new_book=""):
	"""
	Ajouter un livre dans /data/books.txt
	"""
	new_book = str(input("Enter the name of the book : "))
	while book_exist(new_book):
		new_book = str(input("Enter the name of the book : "))
	write_file("books_add", new_book)
	update_rating_matrix("add_book", None)
	return True


def delete_book(less_book=""):
	"""
	Supprimer un livre dans /data/books.txt
	"""

	show_books()

	less_book = str(input("Enter the name of the book : "))
	while book_exist(less_book) == False:
		less_book = str(input("Enter the name of the book : "))

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
	Vérifier l'existence d'un livre dans /data/books.txt
	Retourne un Booléen
	"""
	books = read_file("books")
	books = del_indice(books)
	for i in books:
		if verif_book == i:
			return True
	return False


def modify_book(old_book="", update_book=""):
	"""
	Modifier un livre dans /data/books.txt
	"""

	while book_exist(old_book) == False:
		old_book = str(input("Enter the name of the book : "))
	update_book = str(input("Enter the new name of the book : "))
	while book_exist(update_book):
		update_book = str(input("Enter the new name of the book : "))
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

	print("------------BOOKS LIST------------")
	for i in range(0, len(data)):
		print(data[i])
	print("------------BOOKS LIST------------")

	return True


