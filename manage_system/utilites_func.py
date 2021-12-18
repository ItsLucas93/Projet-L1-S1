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