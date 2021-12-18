######### MODULES / IMPORT #############

from manage_system.manage_files import read_file

######### MODULES / IMPORT #############

######### SETTINGS #############

from config import language
if language == "fr":
    from languages.language_fr import *
elif language == "en":
    from languages.language_en import *

######### SETTINGS #############

def ask_username():
    """
    Ask user to set an username
    """
    username = ""
    while len(username) < 3 or len(username) > 16:
        username = str(input(text_ask_username_input))
        if user_exist(username):
            print(text_ask_username_input_failed_1 + " " + username + " " + text_ask_username_input_failed_2)
            username = ""
    return username


def ask_gender():
    """
    Ask the gender of the user
    """
    gender = 0
    while (gender <= 0) or (gender > 3):
        try:
            gender = int(input(text_ask_gender_input))
        except ValueError:
            pass
    return gender


def ask_age():
    """
    Ask the age of the user
    """
    age = 0
    while (age <= 0) or (age > 3):
        try:
            age = int(input(text_ask_age_input))
        except ValueError:
            pass
    return age


def ask_preferences():
    """
    Ask the type of book the user wants to read
    """
    preferences = 0
    while (preferences <= 0) or (preferences > 7):
        try:
            preferences = int(input(text_ask_preferences))
        except ValueError:
            pass
    return preferences


def position(data, username):
    """
    Give the position of the user in the data
    data: list
    username: str
    i: int
    """
    i = 0
    while (i < len(data)) and (username not in data[i]):
        i += 1

    if i > len(data):
        pass
    else:
        return i


def user_exist(username):
    """
    Verify if user exist
    """

    # Import de la liste data
    data = read_file("readers")

    for i in data:
        if i[0] == username:
            return True
    return False

####################### book

def has_read(username, marque):
    data = read_file("booksread")

    for i in data:
        if i[0] == username:
            for k in i:
                if k == str(marque):
                    return True
    return False


