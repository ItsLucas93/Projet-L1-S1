"""
Project name: BOOK MANAGER
Author: MENIN TIBAUT & KOCOGLU LUCAS
Desc: This file manage write and read file.
"""

######### PATH VAR #############

path_books = "data/books.txt"
path_booksread = "data/booksread.txt"
path_readers = "data/readers.txt"
path_rating_matrix = "data/rating_matrix.txt"
path_suggest_matrix = "data/suggest_matrix.txt"
path_suggest_matrix_log = "logs/logs_suggest_matrix.txt"

######### PATH VAR #############

######### FUNCTIONS #############

def read_file(path):
    """
    Read files
    parameters:
        path (str) - modes : books / booksread / readers / rating_matrix / suggest_matrix
    """

    # Python 3.10 case/match instead of if/else
    # match(path):
    #     case "books":
    #         path = path_books
    #     case "booksread":
    #         path = path_booksread
    #     case "path_readers":
    #         path = path_readers

    if path == "books":
        path = path_books

        with open(path, 'r', encoding="UTF-8") as f:
            data = f.readlines()
            for i in range(0, len(data)):
                data[i] = remove_antislashn(data[i])


    elif path == "booksread":
        path = path_booksread

        with open(path, 'r', encoding="UTF-8") as f:
            data = f.readlines()
            for i in range(0, len(data)):
                data[i] = remove_antislashn(data[i])
            for i in range(0, len(data)):
                data[i] = data[i].split(',')



    elif path == "readers":
        path = path_readers

        with open(path, 'r', encoding="UTF-8") as f:
            data = f.readlines()
            for i in range(0, len(data)):
                data[i] = remove_antislashn(data[i])
            for i in range(0, len(data)):
                data[i] = data[i].split(',')


    elif path == "rating_matrix":
        path = path_rating_matrix

        with open(path, 'r', encoding="UTF-8") as f:
            data = f.readlines()
            for i in range(0, len(data)):
                data[i] = remove_antislashn(data[i])
            for i in range(0, len(data)):
                data[i] = data[i].split(' ')


    elif path == "suggest_matrix":
        path = path_suggest_matrix

        with open(path, 'r', encoding="UTF-8") as f:
            data = f.readlines()
            for i in range(0, len(data)):
                data[i] = remove_antislashn(data[i])
            for i in range(0, len(data)):
                data[i] = data[i].split(' ')

    return data


def write_file(path, liste, comment=""):
    """
    Write file
    parameters:
        path (str) - modes : books / books_add / booksread / booksreader_add / readers / readers_add / rating_matrix / suggest_matrix / logs_suggest_matrix
        liste (list)
        comment (str) - for logs_suggest_matrix
    """

    if path == "books_add":
        path = path_books


        with open(path, 'a', encoding="UTF-8") as f:
            f.write("\n" + str(len(read_file("books")) + 1) + " - " + liste)


    elif path == "books":
        path = path_books

        with open(path, 'w', encoding="UTF-8") as f:
            for i in range(0, len(liste) - 1):
                f.write(str(i + 1) + " - " + liste[i] + "\n")
            f.write(str(i + 2) + " - " + liste[-1])


    elif path == "booksreader_add":
        path = path_booksread

        with open(path, "a", encoding="UTF-8") as f:
            f.write("\n" + liste)


    elif path == "booksread":
        path = path_booksread

        liste = assemble_liste_2d(liste)
        with open(path, 'w', encoding="UTF-8") as f:
            for i in range(0, len(liste) - 1):
                f.write(liste[i] + "\n")
            f.write(liste[-1])


    elif path == "readers_add":
        path = path_readers

        with open(path, 'a', encoding="UTF-8") as f:
            f.write("\n" + assemble_liste_1d(liste))


    elif path == "readers":
        path = path_readers

        with open(path, 'w', encoding="UTF-8") as f:
            liste = assemble_liste_2d(liste)
            for i in range(0, len(liste) - 1):
                f.write(liste[i] + "\n")
            f.write(liste[-1])

    elif path == "rating_matrix":
        path = path_rating_matrix

        with open(path, 'w', encoding="UTF-8") as f:
            liste = assemble_liste_2d(liste, " ")
            for i in range(0, len(liste) - 1):
                f.write(liste[i] + "\n")
            f.write(liste[-1])

    elif path == "suggest_matrix":
        path = path_suggest_matrix

        with open(path, 'w', encoding="UTF-8") as f:
            liste = assemble_liste_2d(liste, " ")
            for i in range(0, len(liste) - 1):
                f.write(liste[i] + "\n")
            f.write(liste[-1])

    elif path == "logs_suggest_matrix":
        path = path_suggest_matrix_log

        with open(path, 'a', encoding="UTF-8") as f:
            f.write("--------------------------------\n")
            liste = assemble_liste_2d(liste, " ")
            for i in range(0, len(liste) - 1):
                f.write(liste[i] + "\n")
            f.write(liste[-1])
            f.write("\n\n" + str(comment))
            f.write("\n--------------------------------\n\n")


def assemble_liste_1d(liste):
    """
    Assemble list in char before write_file
    """
    char = ""
    for i in range(0, len(liste) - 1):
        char += str(liste[i]) + ','
    char += str(liste[-1])
    return char


def assemble_liste_2d(liste, separateur=','):
    """
    Assemble lists in list before write_file
    """
    temp = []
    for i in range(0, len(liste)):
        char = ""
        for j in range(0, len(liste[i]) - 1):
            char += str(liste[i][j]) + separateur
        char += str(liste[i][-1])
        temp.append(char)
    return temp


def remove_antislashn(charactere):
    """
    Remove backslash n from char
    """
    if charactere[-1] == "\n":
        charactere = charactere[:-1]
    return charactere


def regenerate_file():
    """
    reset factory of all data in /data/*
    """
    from suggestions.updater_matrix import rating_matrix_init, suggest_matrix_init

    path = path_readers
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(
            "Gilbert,1,2,1\nWilliam,3,3,7\nAlienRoXoR17,2,1,3\nanonyme,3,3,2\nLecteur_assidu,1,1,3\nharipoteur,3,2,5\nLili,2,2,2\nArchiBald_fx,1,3,4")

    path = path_books
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(
            "1 - Débuter la programmation Java\n2 - Apprendre Python\n3 - Les Citations du Président Mao Tse-Toung\n4 - Don Quichotte de la Manche\n5 - Un conte de deux villes\n6 - Le Seigneur des Anneaux\n7 - Le Petit Prince\n8 - Harry Potter à l’école des sorciers\n9 - Le Hobbit\n10 - Dix Petits Nègres\n11 - Le rêve dans le Pavillon rouge\n12 - Le Lion, la Sorcière blanche et l’Armoire magique\n13 - Elle – She : a history of Adventure\n14 - The Da Vinci Code\n15 - Réfléchissez et devenez riche\n16 - Harry Potter et le Prince de Sang mêlé\n17 - L’Alchimiste\n18 - Harry Potter et la Chambre des Secrets\n19 - L’attrape-cœurs, The Catcher in the Rye")

    path = path_booksread
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(
            "Gilbert,5,7,8,9\nWilliam,1,8,9,10\nAlienRoXoR17,3,4,5,6,10\nAnonyme,1,2,4,7\nLecteur_assidu,1,2,3,5,6,8,9,10\nHaripoteur,3,5,8,9,10\nLili,1,2,4,6,8,10\nArchiBald_fx,7,9,10")

    path = path_readers
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(
            "Gilbert,1,2,1\nWilliam,3,3,7\nAlienRoXoR17,2,1,3\nanonyme,3,3,2\nLecteur_assidu,1,1,3\nharipoteur,3,2,5\nLili,2,2,2\nArchiBald_fx,1,3,4")

    rating_matrix_init()
    suggest_matrix_init()

######### FUNCTIONS #############
