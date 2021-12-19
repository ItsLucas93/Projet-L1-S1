######### MODULES / IMPORT #############

from manage_system.manage_files import read_file, write_file
from manage_system.manage_bookreaders import add_bookreader, remove_bookreader
from manage_system.manage_book import del_indice
from manage_system.utilities_func import *

from suggestions.updater_matrix import update_rating_matrix
from suggestions.manage_review import get_review_book

######### MODULES / IMPORT #############

######### SETTINGS #############

from config import language
if language == "fr":
    from languages.language_fr import *
elif language == "en":
    from languages.language_en import *

######### SETTINGS #############

"""
Les fonctions retournent des bool pour déclarer si les opérations se sont déroulés avec succès.
En cas de False: Message d'erreur.
"""


def add_user():
    """
    Ajoute un utilisateur dans le fichier ./data/readers.txt
    """

    print(text_add_user_separator)

    # Entrée utilisateur

    username, gender, age, preferences = ask_username(), ask_gender(), ask_age(), ask_preferences()
    temp = [username, gender, age, preferences]

    # Auto-update function : reader, bookreader, rating_matrix
    add_bookreader(username)
    write_file("readers_add", temp)
    update_rating_matrix("add_user", None)
    return True


def remove_user(username=""):
    """
    Supprime un utilisateur dans le fichier ./data/readers.txt
    """

    # Import de la liste data
    data = read_file("readers")

    while user_exist(username) is False:
        username = str(input(text_remove_user_input))
        if username in ["exit", "Exit", "EXIT", "exit()", "Exit()"]:
            return False

    print(text_remove_user_warning)        
    while True:
        confirm = str(input(text_remove_user_warning_confirm))
        if confirm in ["Yes", "yes", "y", "Y", "YES", "oui", "Oui", "o", "OUI", "O"]:
            i = 0
            while (i < len(data)) and (data[i][0] != username):
                i += 1

            # Cas où l'utilisateur ne figure pas dans la base car i > len(data)
            if i > len(data):
                return False
            # Cas où l'utilisateur figure dans la base
            else:
                data.pop(i) # or del data[i]
                write_file("readers", data)
                remove_bookreader(username)
                update_rating_matrix("remove_user", i)
                quit()  # Built-in function to exit the program
        elif confirm in ["No", "no", "n", "N", "NO", "Non", "non", "NON"]:
            return False


def user_exist(username):
    """
    Vérifie si l'utilisateur existe dans le fichier ./data/readers.txt
    """

    # Import de la liste data
    data = read_file("readers")

    for i in data:
        if i[0] == username:
            return True
    return False


def show_users(command=0):
    """
    Affiche la liste des utilisateurs présents dans ./data/users
    """
    data = read_file("readers")

    nbdanspages = 15

    if len(data) <= nbdanspages:
        print(text_show_users_separator_1 + str(len(data)) + " " + text_show_users_separator_2)
        for i in range(len(data)):
            print(data[i][0])
        print(text_show_users_separator)
    else:
        pages = len(data) // nbdanspages
        page = 0

        while command != 3:

            if (page + 1) * nbdanspages > len(data):
                borne_a, borne_b = page * nbdanspages, len(data)
            else:
                borne_a, borne_b = page * nbdanspages, (page + 1) * nbdanspages

            print(text_show_users_separator_3 + " " + str(page + 1) + "/" + str(pages + 1) + text_show_users_separator_4)
            for i in range(borne_a, borne_b):  # vérifier la relation entre page actuel et
                print(data[i][0])
            print(text_show_users_separator_3 + " " + str(page + 1) + "/" + str(pages + 1) + text_show_users_separator_4)

            if page == 0:
                commandes = {2: "Page suivante", 3: "Exit"}
                print(text_show_users_commands_1)
            elif page == pages:
                commandes = {1: "Page précédente", 3: "Exit"}
                print(text_show_users_commands_2)
            else:
                commandes = {1: "Page précédente", 2: "Page suivante", 3: "Exit"}
                print(text_show_users_commands_3)
            try:
                command = int(input("Your input : "))
            except ValueError:
                pass

            if command not in commandes:
                pass
            elif command == 1:
                page -= 1
            elif command == 2:
                page += 1
            elif command == 3:
                return True

    return True


def modify_user(username="", command=0):
    """
    Modifier un utlisateur dans le fichier ./data/readers.txt
    Commandes : 
    1. Pseudo 
    2. gender
    3. Âge
    4. Préférences
    5. Livres que vous avez lu ?
    6. Exit
    """
    data = read_file("readers")

    print(text_modify_user_separator)
    print(text_modify_user_input_request)
    while user_exist(username) is False:
        username = str(input(text_modify_user_input))

    # Index user in data

    index = position(data, username)

    commandes = {1: "gender", 2: "age", 3: "preferences", 4: "back to main menu"}

    print(text_modify_user_command)
    while command != 4:
        try:
            command = int(input(text_modify_user_input))
        except ValueError:
            pass

        if command not in commandes:
            pass

        elif command == 1:
            data[index][1] = ask_gender()
            print(text_modify_user_command)

        elif command == 2:
            data[index][2] = ask_age()
            print(text_modify_user_command)

        elif command == 3:
            data[index][3] = ask_preferences()
            print(text_modify_user_command)

        elif command == 4:
            pass

        write_file("readers", data)
    return True


def show_profile(username=""):
    """
    Show profil of logged user # à modifier en username donné en input
    # Ajouter la liste des livres lu
    """

    data_readers = read_file("readers")
    data_bookreaders = read_file("booksread")
    data_book = read_file("books")

    while user_exist(username) is False:
        username = str(input(text_show_user_input))

    for i in data_readers:
        for j in i:
            if username == j:
                print(text_show_user_separator)
                print(text_show_user_username + str(i[0]))
                if i[1] == '1':
                    print(text_show_user_gender_1)
                elif i[1] == '2':
                    print(text_show_user_gender_2)
                elif i[1] == '3':
                    print(text_show_user_gender_3)
                if i[2] == '1':
                    print(text_show_user_age_1)
                elif i[2] == '2':
                    print(text_show_user_age_2)
                elif i[2] == '3':
                    print(text_show_user_age_3)
                if i[3] == '1':
                    print(text_show_user_preference_1)
                elif i[3] == '2':
                    print(text_show_user_preference_2)
                elif i[3] == '3':
                    print(text_show_user_preference_3)
                elif i[3] == '4':
                    print(text_show_user_preference_4)
                elif i[3] == '5':
                    print(text_show_user_preference_5)
                elif i[3] == '6':
                    print(text_show_user_preference_6)
                elif i[3] == '7':
                    print(text_show_user_preference_7)
                print(text_show_user_books_readed, end="")
                temp = []
                for i in data_bookreaders:
                    if i[0] == username:
                        for j in i[1:]:
                            temp.append(j)
                data_book = del_indice(data_book)
                if temp == []:
                    print(text_show_user_books_no_book_readed_yet)
                else:
                    for i in temp:
                        print(data_book[int(i)-1] + " (" + text_show_user_books_note + " : " + str(get_review_book(username, position(data_readers, username), int(i))) + "/5)", end=" ; ")
                    print("\n" + text_show_user_separator)
                return True
    return False

