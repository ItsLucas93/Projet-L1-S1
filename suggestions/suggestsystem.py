from manage_system.manage_files import read_file, write_file
from manage_system.manage_book import book_exist, show_books
from manage_system.manage_bookreaders import has_read
from manage_system.manage_readers import position

# Implémenter la matrice de notation à stocker
def rating_matrix_init():
	M = []
	for i in range(0, len(read_file("readers"))):
		temp = []
		for j in range(0, len(read_file("books"))):
			temp.append('0')
		M.append(temp)

	write_file("rating_matrix", M)


def update_rating_matrix(reason, indice=0):

	data_rating_matrix = read_file("rating_matrix")

	if reason == "add_user":
		temp = []
		for i in range(0, len(read_file("books"))):
			temp.append('0')
		data_rating_matrix.append(temp)
	elif reason == "remove_user":
		del data_rating_matrix[i]
	if reason == "add_book":
		for j in range(0, len(data_rating_matrix)):
			data_rating_matrix[j].append('0')
	elif reason == "remove_book":
		for j in range(0, len(data_rating_matrix)):
			del data_rating_matrix[j][indice-1] # -1 bc of id_book is from 1-n and list 0-(n-1)

	write_file("rating_matrix", data_rating_matrix)


def review_book(username, id_book_review=-1):
	"""
	Username: str
	id_book_review; index_user: int
	"""
	# print(id_book_review < 0, id_book_review > len(read_file("books")), has_read(username, id_book_review))

	if id_book_review == -1:
		show_books()

	while id_book_review < 0 or id_book_review > len(read_file("books")):
		try:
			id_book_review = int(input("Enter the id of the book you want to review (that you readed), enter 0 to exit : "))
		except ValueError:
			id_book_review = -1

		if id_book_review == 0:
			return True
		elif has_read(username, id_book_review) is False:
			id_book_review = -1
			print("Please enter a book you readed ! ")

	notation = -1
	while (notation <= 0) or (notation > 5):
		notation = int(input('Please give a grade from 1 to 5 : '))

	index_user = position(read_file("readers"), username)

	data_rating_matrix = read_file("rating_matrix")
	data_rating_matrix[index_user][id_book_review-1] = str(notation)
	write_file("rating_matrix", data_rating_matrix)


def get_review_book(username, id_book_review=-1):
	data_rating_matrix = read_file("rating_matrix")
	index_user = position(read_file("readers"), username)
	notation = data_rating_matrix[index_user][id_book_review-1]
	return notation

def suggested_book():
	return True