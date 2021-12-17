from manage_system.manage_files import read_file, write_file
from manage_system.manage_bookreaders import add_bookreader

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

    return True


def remove_user(username):
    """
    Supprime un utilisateur dans le fichier ./data/readers.txt
    """

    # Import de la liste data
    data = read_file("readers")

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
        return True


def user_exist(username):
    """
    Vérifie si l'utilisateur existe dans le fichier ./data/readers.txt
    """

    # Import de la liste data
    data = read_file("readers")

    for i in data:
        for j in i:
            if j == username:
                return True
    return False


def show_users(command=0):
    """
    Affiche la liste des utilisateurs présents dans ./data/users
    """
    data = read_file("readers")

    nbdanspages = 15

    if data < nbdanspages:
        print("------------USERS LIST------------")
        for i in range(len(data)):
            print(data[i][0])
        print("------------USERS LIST------------")
    else:
        pages = len(data) // nbdanspages
        page = 0

        while command != 3:

            print("------------USERS LIST (Page " + str(page) + "/" + str(pages) + ")------------")
            for i in range(page * nbdanspages, (page + 1) * nbdanspages):  # vérifier la relation entre page actuel et
                print(data[i][0])
            print("------------USERS LIST (Page " + str(page) + "/" + str(pages) + ")------------")

            if page == 0:
                commandes = {1: "Page suivante", 3: "Exit"}
                print("------------COMMANDS------------"
                      "\nPlease select your choice : "
                      "\n1. Page suivante"
                      "\n3. Exit")
                print("------------COMMANDS------------")
            if page == pages:
                commandes = {2: "Page suivante", 3: "Exit"}
                print("------------COMMANDS------------"
                      "\nPlease select your choice : "
                      "\n2. Page précédente"
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


def modify_user(username, command=0):
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

    # Index user in data

    index = position(data, username)

    commandes = {1: "gender", 2: "age", 3: "preferences", 4: "back to main menu"}

    while command != 4:
        print("------------COMMAND MODIFY USER------------"
              "\nPlease select your choice : "
              "\nYou can't change your username, please delete your account to proceed."
              "\n1. Modify Gender"
              "\n2. Modify Age"
              "\n3. Modify Preferences"
              "\n4. Back to main menu")
        print("------------COMMAND MODIFY USER------------")
        command = int(input("Votre entrée : "))

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


def show_user(username):
    """
    Show profil of logged user
    """

    data = read_file("readers")

    for i in data:
        for j in i:
            if username == j:
                print("------------YOUR PROFILE------------"
                      "\nUsername : " + str(i[0]))
                if i[1] == 1:
                    print("Gender : H")
                elif i[1] == 2:
                    print("Gender : F")
                elif i[1] == 3:
                    print("Gender : Peu importe")
                print("Age : " + str(i[2]))
                if i[3] == 1:
                    print("Preferences : Sciences Fiction")
                elif i[3] == 2:
                    print("Preferences : Biographie")
                elif i[3] == 3:
                    print("Preferences : Horreur")
                elif i[3] == 4:
                    print("Preferences : Romance")
                elif i[3] == 5:
                    print("Preferences : Fable")
                elif i[3] == 6:
                    print("Preferences : Histoire")
                elif i[3] == 7:
                    print("Preferences : Comédie")
                print("------------YOUR PROFILE------------")
                return True
    return False


#########################

def ask_username(username=""):
    """
    Ask user to set an username
    """
    while ((len(username) <= 0 or len(username) > 16) and (user_exist(username) is True)):
        username = str(input("Saisir votre pseudonyme \nMinimum 3 caractères \nMaximum 16 caractères \nVotre saisie : "))
    return username


def ask_gender(gender=0):
    """
    Ask the gender of the user
    """
    while ((gender < 0) or (gender > 3)):
        try:
            gender = int(input("Saisir votre gender : \n1. HOMME\n2. FEMME\n3.PEU IMPORTE\nVotre saisie : "))
        except ValueError:
            pass
    return gender


def ask_age(age=0):
    """
    Ask the age of the user
    """
    while ((age < 0) or (age > 3)):
        try:
            age = int(input("Saisir votre âge : \n1. <= 18 ans\n2. Entre 18 et 25 ans\n3. > 25 ans\nVotre saisie : "))
        except ValueError:
            pass
    return age


def ask_preferences(preferences=0):
    """
    Ask the type of book the user wants to read
    """
    while ((preferences < 0) or (preferences > 7)):
        try:
            preferences = int(input("Saisir votre style de lecture : \n1. Sciences fiction\n2. Biographie\n3. Horreur\n4. Romance\n5. Fable \n6. Histoire \n7. Comédie \nVotre saisie :"))
        except ValueError:
            pass
    return preferences


# def ask_livres_lu(livres_lu=""):
#     """
#     Ask the user which book he readed
#     """
#     temp = []
#     while ((livres_lu == "") or (livres_lu not in ["exit()", "Exit()"])):
#         livres_lu = int(
#             input("Saisissez vos livres lu. Lorsque vous aurez terminé, veuillez saisir 'Exit()'. \nVotre saisie : "))
#         temp.append(livres_lu)
#     return livres_lu


def position(data, username):
    i = 0
    while (i < len(data)) and (username not in data[i]):
        i += 1

    if i > len(data):
        pass
    else:
        return i
