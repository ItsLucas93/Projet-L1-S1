######### MODULES / IMPORT #############
from manage_system.manage_files import read_file, write_file
from manage_system.utilities_func import position

from suggestions.updater_matrix import suggest_matrix_init

from math import sqrt
######### MODULES / IMPORT #############

######### SETTINGS #############

from config import language
if language == "fr":
    from languages.language_fr import *
elif language == "en":
    from languages.language_en import *

######### SETTINGS #############

def common_review(user1, user2):
    """
    sum (   user1: note_review & user2: note_review (in common)   )
    """
    data_rating_matrix = read_file("rating_matrix")
    index_a, index_b = position(read_file("readers"), user1), position(read_file("readers"), user2)
    a = data_rating_matrix[index_a]
    b = data_rating_matrix[index_b]
    common = []
    res = 0
    for i in range(0, len(a)):
        if a[i] != '0' and b[i] != '0':
            res += int(a[i]) * int(b[i])

    return res

def note_user(user):
    """
    sqrt(sum(a(_i) ^2))
    """

    data_rating_matrix = read_file("rating_matrix")
    index = position(read_file("readers"), user)
    result = 0

    for i in range(0, len(data_rating_matrix[index])):
        result += int(data_rating_matrix[index][i]) ** 2

    return result


def func_sim_cos(user1, user2):

    if sqrt(note_user(user1)) * sqrt(note_user(user2)) == 0:
        result = 0
    else:
        result = common_review(user1, user2) / (sqrt(note_user(user1)) * sqrt(note_user(user2)))

    return result


def calc_suggest_matrix(suggest_matrix):

    data_readers = read_file("readers")
    temp = [data_readers[i][0] for i in range(0, len(data_readers))]

    for i in range(0, len(suggest_matrix)):
        for j in range(0, len(suggest_matrix)):
            suggest_matrix[i][j] = round(func_sim_cos(user1=temp[i], user2=temp[j]), 2)

    write_file("suggest_matrix", suggest_matrix)


def similar_user(user1):
	data_suggest_matrix = read_file("suggest_matrix")
	data_readers = read_file("readers")

	index = position(data_readers, user1)

	temp = data_suggest_matrix[index]
	temp.pop(index)

	for i in range(0, len(temp)):
		if temp[i] == max(temp):
			index_user2 = i
			break

	if index <= index_user2:
		index_user2 +=1
	else:
		pass

	user2 = data_readers[index_user2][0]
	return user2


def suggest_book(user1):

    calc_suggest_matrix(read_file("suggest_matrix"))
    user2 = similar_user(user1)

    data_booksread = read_file("booksread")
    data_readers = read_file("readers")
    data_book = read_file("books")
    index_user1 = position(data_readers, user1)
    index_user2 = position(data_readers, user2)
    data_booksread_user1 = data_booksread[index_user1][1:]
    data_booksread_user2 = data_booksread[index_user2][1:]

    similar_books = [i for i in data_booksread_user1 for j in data_booksread_user2 if i == j]

    i = 0
    while (i < len(data_booksread_user2)):
        if data_booksread_user2[i] in similar_books:
            del data_booksread_user2[i]
            i = 0
        else:
            i += 1

    print(text_suggestion_recommend)
    for i in data_booksread_user2:
        print(data_book[int(i)-1])

    print(text_suggestion_recommend_exit)

    return True