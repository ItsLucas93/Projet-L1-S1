from manage_system.manage_files import read_file, write_file

def add_book(new_book):
	"""
	Ajouter un livre dans /data/books.txt
	"""
	if book_exist(new_book) == False:
		write_file("books_add",new_book)
	pass


def delete_book():
	pass
	"""
	Supprimer un livre dans /data/books.txt
	"""

def book_exist(verif_book):
	"""
	Vérifier l'existence d'un livre dans /data/books.txt
	Retourne un Booléan
	"""
	books = read_file("books")
	for i in books:
		if verif_book == i:
			return True
	return False


def modify_book():
	"""
	Modifier un livre dans /data/books.txt
	"""
	pass


def review_book():
	"""
	Donenr une note au livre
	"""
	pass