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
	+-------------------+
	|---- Main Menu ----|
	+-------------------+

	1. Manage Users
	2. Manage Books
	3. Manage Books Readers
	4. Exit program
	"""
	while command != 4:
		commandes = {1: "Manage Users", 2: "Manage Books", 3: "Manage Books Readers", 4: "Exit Program", 5: "Settings"}
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
			pass  # Does nothing, just relaunch the command_center()
		elif command == 1:
			if command_manage_reader():
				pass
		elif command == 2:
			if command_manage_book():
				pass
		elif command == 3:
			if command_maange_bookreaders():
				pass
		elif command == 4:
			print("Exiting program...")
		elif command == 5:
			if command_settings():
				pass

	return True


def command_settings():
	"""
	1. Language
	2. Factory Reset (*secret implement*)
	3. Back to main menu
	"""
	return True


def command_manage_reader():
	"""
	1. Add User
	2. Show User list
	3. Delete User
	4. Modify User
	5. Show your profil
	6. Back to main menu
	"""
	while command != 6:
		commandes = {1: "Add user", 2: "Show user list", 3: "Delete user", 4: "Modify your profile", 5: "Show your profile", 6: "Back to main menu"}
		print("------------COMMAND MANAGE READER------------"
			  "\nPlease select your choice : "
			  "\n1. Add User"
			  "\n2. Show User list"
			  "\n3. Delete User"
			  "\n4. Modify your profile"
			  "\n5. Show your profile"
			  "\n6. Back to main menu")
		print("------------COMMAND MANAGE READER------------")

		command = int(input("Your input : "))
		# Commands to implant

		if command not in commandes:
			pass  # Does nothing, just relaunch the command_center()
		elif command == 1:
			if add_user():
				pass
		elif command == 2:
			if show_users():
				pass
		elif command == 3:
			print("-=-=-=-=-=- WARNING -=-=-=-=-=-"
				 "\nYou're gonna delete yourself in data"
				 "\nDo you want to proceed ?"
				 "\n If yes, the program will exit itself")
			confirm = str(input("Your input (Yes/No): "))
			if confirm in ["Yes", "yes", "y", "Y"]:
				if remove_user(logged_username):
					quit()  # Built-in function to exit the program
			elif confirm in ["No", "no", "n", "N"]:
				print("Command aborted. Back to Manage Reader")
		elif command == 4:
			if modify_user(logged_username):
				pass
		elif command == 5:
			if show_user(logged_username):
				pass
		elif command == 6:
			print("Exiting manage reader...")

	return True


def command_manage_book():
	"""
	1. Add book
	2. Delete book
	3. Rename book
	4. Book exist ?
	5. Back to main menu
	"""
	while command != 4:
		commandes = {1: "Add Book", 2: "Delete book", 3: "Rename book", 4: "Book Exist", 5: "Back to main menu"}
		print("------------COMMAND MANAGE BOOK------------"
			  "\nPlease select your choice : "
			  "\n1. Add Book"
			  "\n2. Delete book"
			  "\n3. Rename book"
			  "\n4. Book Exist"
			  "\n5. Back to main menu")
		print("------------COMMAND MANAGE BOOK------------")

		command = int(input("Your input : "))
		# Commands to implant

		if command not in commandes:
			pass  # Does nothing, just relaunch the command
		# elif command == 1:
		# 	if command_manage_reader():
		# 		pass
		# elif command == 2:
		# 	if command_manage_book():
		# 		pass
		# elif command == 3:
		# 	if command_maange_bookreaders():
		# 		pass
		# elif command == 4:
		# 	print("Exiting program...")

	return True


def command_maange_bookreaders():
	"""
	1. ???
	2. ???
	3. Back to main menu
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
		if add_user():
			return True
	else:
		return True


# Sinon recommencer

######### FONCTIONS #############

if __name__ == '__main__':
	if login():
		if command_center():
			pass
	print("Good bye !")
