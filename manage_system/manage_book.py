from manage_system.manage_files import read_file, write_file, assemble_liste
from manage_system.manage_bookreaders import remove_bookread

def add_book(new_book):
	"""
	Ajouter un livre dans /data/books.txt
	"""
	if book_exist(new_book) == False:
		write_file("books_add",new_book)
	# penser à faire un booléen pour dire si existe déjà
	pass


def delete_book(less_book):
	"""
	Supprimer un livre dans /data/books.txt
	"""
	if book_exist(less_book) == False:
		book_liste = read_file("books")
		for i in range(len(book_liste)):
			if less_book == book_liste[i]:
				marque = i
		del book_liste[marque]
		write_file("books",book_liste)

		remove_bookread(marque)

	# penser à faire un boléen pour dire si effectuer ou non 


def book_exist(verif_book):
	"""
	Vérifier l'existence d'un livre dans /data/books.txt
	Retourne un Booléen
	"""
	books = read_file("books")
	for i in books:
		place = 0
		for j in i:    # permet de comparer sans les indices
			place += 1
			if j == "-":
				break
		p = place+1
		i = i[p:]
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