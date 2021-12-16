###########################################################################
# ██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗░░░██╗███████╗ #
# ██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║░░░██║██╔════╝ #
# ██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║░░░██║█████╗░░ #
# ██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║░░░██║██╔══╝░░ #
# ██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║╚██████╔╝███████╗ #
# ╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝ # src : https://fsymbols.com/generators/wide/
########################################################################### ur book manager from 1991


######### MODULES / IMPORT #############

from manage_system.manage_files import *
from manage_system.manage_bookreaders import *
from manage_system.manage_readers import *
from manage_system.manage_book import *

import os
from time import sleep


######### MODULES / IMPORT #############

######### FONCTIONS #############

def welcome():
	"""
	Message de bienvenue
	"""
	print("#####################################################################################################")
	print("# ██████╗░░█████╗░░█████╗░██╗░░██╗░░░░███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░ #")
	print("# ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░░████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗ #")
	print("# ██████╦╝██║░░██║██║░░██║█████═╝░░░░░██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝ #")
	print("# ██╔══██╗██║░░██║██║░░██║██╔═██╗░░░░░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗ #")
	print("# ██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗░░░░██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║ #")
	print("# ╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝ #")
	print("#######################################################################################.from 1991####")


def command_center(command=0):
	"""
	----- Main Menu -----

	1. Manage Users
	2. Manage Books
	3. Manage Books Readers
	4. Exit program
	"""
	while command != 4:
		commandes = {1: "Manage Users", 2: "Manage Books", 3: "Manage Books Readers", 4: "Exit Program"}
		print("------------COMMAND CENTER------------"
		  "Please select your choice : "
		  "1. Manage Users"
		  "2. Manage Books"
		  "3. Manage Books Readers"
		  "4. Exit program")
		print("------------COMMAND CENTER------------")

		command = int(input("Your input : "))
		# Commands to implant

		if command not in commandes:
			pass # Does nothing, just relaunch the command_center()
		elif command == 1:
			pass
		elif command == 2:
			pass
		elif command == 3:
			pass
		elif command == 4
			print("Exiting program...")

	return True


def command_settings():
	"""
	1. Language
	2. Factory Reset (*secret implement*)
	3. Back to main menu
	"""
	return True


def command_manage_user():
	"""
	1. Add User
	2. Show User list
	3. Delete User
	4. Modify User
	5. Show profil
	6. Back to main menu
	"""
	return True


def command_manage_book():
	"""
	1. Add book
	2. Delete book
	3. Rename book
	4. Book exist ?
	5. Back to main menu
	"""
	return True


def login():
	"""
	Username: logged_username
	If new user : Type "new"
	"""
	global logged_username
	logged_username = ""
	while (user_exist(logged_username) == False) or (logged_username == "new"):
		logged_username = str(input("Username : "))

	if logged_username == "new":
		if add_user() == True:
			return True
	else:
		return True


# Sinon recommencer

######### FONCTIONS #############

if __name__ == '__main__':
	if login() == True:
		while command_center() == True:
			pass
	print("Good bye !")