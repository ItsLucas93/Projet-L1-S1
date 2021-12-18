from manage_system.manage_files import read_file, write_file
from manage_system.manage_bookreaders import add_bookreader, remove_bookreader
from manage_system.manage_book import del_indice
from suggestions.updater_matrix import update_rating_matrix
from suggestions.manage_review import get_review_book

"""
Les fonctions retournent des bool pour déclarer si les opérations se sont déroulés avec succès.
En cas de False: Message d'erreur.
"""


def add_user():
    """
    Ajoute un utilisateur dans le fichier ./data/readers.txt
    """

    # Entrée utilisateur

    username, gender, age, preferences = ask_username(), ask_gender(), ask_age(), ask_preferences()
    temp = [username, gender, age, preferences]

    add_bookreader(username)

    # Implémenter
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
        username = str(input("Enter a username : (enter exit to exit)"))

    if username == ["exit", "Exit", "EXIT", "exit()", "Exit()"]:
        return False

    print("-=-=-=-=-=- WARNING -=-=-=-=-=-"
         "\nYou're gonna delete a profile in data"
         "\nDo you want to proceed ?"
         "\n If yes, you will have to relaunch the program")        

    confirm = str(input("Your input (Yes/No): "))
    if confirm in ["Yes", "yes", "y", "Y"]:
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
    elif confirm in ["No", "no", "n", "N"]:
        print("Command aborted. Back to Manage Reader")
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
        print("------------USERS LIST (" + str(len(data)) + " users)------------")
        for i in range(len(data)):
            print(data[i][0])
        print("------------USERS LIST------------")
    else:
        pages = len(data) // nbdanspages
        page = 0

        while command != 3:

            if (page + 1) * nbdanspages > len(data):
                borne_a, borne_b = page * nbdanspages, len(data)
            else:
                borne_a, borne_b = page * nbdanspages, (page + 1) * nbdanspages

            print("------------USERS LIST (Page " + str(page + 1) + "/" + str(pages + 1) + ")------------")
            for i in range(borne_a, borne_b):  # vérifier la relation entre page actuel et
                print(data[i][0])
            print("------------USERS LIST (Page " + str(page + 1) + "/" + str(pages + 1) + ")------------")

            if page == 0:
                commandes = {2: "Page suivante", 3: "Exit"}
                print("------------COMMANDS------------"
                      "\nPlease select your choice : "
                      "\n2. Page suivante"
                      "\n3. Exit")
                print("------------COMMANDS------------")
            elif page == pages:
                commandes = {1: "Page précédente", 3: "Exit"}
                print("------------COMMANDS------------"
                      "\nPlease select your choice : "
                      "\n1. Page précédente"
                      "\n3. Exit")
                print("------------COMMANDS------------")
            else:
                commandes = {1: "Page précédente", 2: "Page suivante", 3: "Exit"}
                print("------------COMMANDS------------"
                      "\nPlease select your choice : "
                      "\n1. Page précédente"
                      "\n2. Page suivante"
                      "\n3. Exit")
                print("------------COMMANDS------------")
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
                print("Exiting user lists...")

    return True


def modify_user(username="", command=0):
    """
    Modifier un utlisateur dans le fichier ./data/readers.txt
    """

    data = read_file("readers")

    """
    Commandes : 
    1. Pseudo 
    2. gender
    3. Âge
    4. Préférences
    5. Livres que vous avez lu ?
    6. Exit
    """
    print(username, user_exist(username))
    while user_exist(username) is False:
        username = str(input("Enter a username : "))

    # Index user in data

    index = position(data, username)

    commandes = {1: "gender", 2: "age", 3: "preferences", 4: "back to main menu"}

    while command != 4:
        print("------------COMMAND MODIFY USER------------"
              "\nPlease select your choice : "
              "\nYou can't change the username, please delete the account to proceed."
              "\n1. Modify Gender"
              "\n2. Modify Age"
              "\n3. Modify Preferences"
              "\n4. Back to main menu")
        print("------------COMMAND MODIFY USER------------")
        try:
            command = int(input("Votre entrée : "))
        except ValueError:
            pass

        if command not in commandes:
            pass
        elif command == 1:
            data[index][1] = ask_gender()
        elif command == 2:
            data[index][2] = ask_age()
        elif command == 3:
            data[index][3] = ask_preferences()
        elif command == 4:
            pass

        write_file("readers", data)
    return True


def show_user(username=""):
    """
    Show profil of logged user # à modifier en username donné en input
    # Ajouter la liste des livres lu
    """

    data_readers = read_file("readers")
    data_bookreaders = read_file("booksread")
    data_book = read_file("books")

    while user_exist(username) is False:
        username = str(input("Enter a username : "))

    for i in data_readers:
        for j in i:
            if username == j:
                print("------------YOUR PROFILE------------")
                print("Username : " + str(i[0]))
                if i[1] == '1':
                    print("Gender : H")
                elif i[1] == '2':
                    print("Gender : F")
                elif i[1] == '3':
                    print("Gender : Peu importe")
                if i[2] == '1':
                    print("Age : < 18")
                elif i[2] == '2':
                    print("Age : 18-25")
                elif i[2] == '3':
                    print("Age : > 25")
                if i[3] == '1':
                    print("Preferences : Sciences Fiction")
                elif i[3] == '2':
                    print("Preferences : Biographie")
                elif i[3] == '3':
                    print("Preferences : Horreur")
                elif i[3] == '4':
                    print("Preferences : Romance")
                elif i[3] == '5':
                    print("Preferences : Fable")
                elif i[3] == '6':
                    print("Preferences : Histoire")
                elif i[3] == '7':
                    print("Preferences : Comédie")
                print("Books readed : \n»»» ", end="")
                temp = []
                for i in data_bookreaders:
                    if i[0] == username:
                        for j in i[1:]:
                            temp.append(j)
                data_book = del_indice(data_book)
                for i in temp:
                    print(data_book[int(i)-1] + " (Note : " + str(get_review_book(username, position(data_readers, username), int(i))) + "/5)", end=" ; ")
                print("\n------------YOUR PROFILE------------")
                return True
    return False


#########################

def ask_username():
    """
    Ask user to set an username
    """
    username = ""
    while len(username) < 1 or len(username) > 16:
        username = str(input("Saisir votre pseudonyme \nMinimum 3 caractères \nMaximum 16 caractères \nVotre saisie : "))
        if user_exist(username):
            print("User with the username " + username + " already exist ! Please try another username.")
            username = ""
    return username


def ask_gender():
    """
    Ask the gender of the user
    """
    gender = 0
    while ((gender <= 0) or (gender > 3)):
        try:
            gender = int(input("Saisir votre gender : \n1. HOMME\n2. FEMME\n3.PEU IMPORTE\nVotre saisie : "))
        except ValueError:
            pass
    return gender


def ask_age():
    """
    Ask the age of the user
    """
    age = 0
    while ((age <= 0) or (age > 3)):
        try:
            age = int(input("Saisir votre âge : \n1. <= 18 ans\n2. Entre 18 et 25 ans\n3. > 25 ans\nVotre saisie : "))
        except ValueError:
            pass
    return age


def ask_preferences():
    """
    Ask the type of book the user wants to read
    """
    preferences = 0
    while ((preferences <= 0) or (preferences > 7)):
        try:
            preferences = int(input("Saisir votre style de lecture : \n1. Sciences fiction\n2. Biographie\n3. Horreur\n4. Romance\n5. Fable \n6. Histoire \n7. Comédie \nVotre saisie : "))
        except ValueError:
            pass
    return preferences


def position(data, username):
    i = 0
    while (i < len(data)) and (username not in data[i]):
        i += 1

    if i > len(data):
        pass
    else:
        return i
