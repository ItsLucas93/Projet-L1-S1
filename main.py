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
from suggestions.manage_review import *

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
			  "\nPlease select your choice : "
			  "\n1. Manage Users"
			  "\n2. Manage Books"
			  "\n3. Manage Books Readers / Suggested books"
			  "\n4. Exit program")
		print("------------COMMAND CENTER------------")

		try:
			command = int(input("Your input : "))
		except ValueError:
			command = 0
		# Commands to implant

		if command not in commandes:
			command = 0  # Does nothing, just relaunch the command_center()
		elif command == 1:
			if command_manage_reader():
				command = 0
		elif command == 2:
			if command_manage_book():
				command = 0
		elif command == 3:
			if command_manage_bookreaders():
				command = 0
		elif command == 4:
			print("Exiting command center...")
		elif command == 5:
			if command_settings():
				command = 0

	return True


def command_settings(command=0):
	"""
	1. Language
	2. Factory Reset (*secret implement*)
	3. Back to main menu
	"""
	return True


def command_manage_reader(command=0):
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

		try:
			command = int(input("Your input : "))
		except ValueError:
			command = 0
		# Commands to implant

		if command not in commandes:
			command = 0  # Does nothing, just relaunch the command_center()
		elif command == 1:
			if add_user():
				command = 0
		elif command == 2:
			if show_users():
				command = 0
		elif command == 3:
			if remove_user() is False:
				print("Something went wrong or the command has been aborted. Please try again later.")
		elif command == 4:
			if modify_user():
				command = 0
		elif command == 5:
			if show_user():
				command = 0
		elif command == 6:
			print("Exiting manage reader...")

	return True


def command_manage_book(command=0):
	"""
	1. Add book
	2. Delete book
	3. Rename book
	4. Lists books
	5. Back to main menu
	"""
	while command != 5:
		commandes = {1: "Add Book", 2: "Delete book", 3: "Rename book", 4: "List books", 5: "Back to main menu"}
		print("------------COMMAND MANAGE BOOK------------"
			  "\nPlease select your choice : "
			  "\n1. Add Book"
			  "\n2. Delete book"
			  "\n3. Rename book"
			  "\n4. Lists books"
			  "\n5. Back to main menu")
		print("------------COMMAND MANAGE BOOK------------")

		try:
			command = int(input("Your input : "))
		except ValueError:
			command = 0
		# Commands to implant

		if command not in commandes:
			command = 0  # Does nothing, just relaunch the command
		elif command == 1:
			if add_book():
				print("Book added !")
				command = 0
		elif command == 2:
			if delete_book():
				print("Book removed.")
				command = 0
		elif command == 3:
			if modify_book():
				print("Book modified.")
				command = 0
		elif command == 4:
			if show_books():
				command = 0
			else:
				print("Something went wrong...")
				command = 0
		elif command == 5:
			print("Exiting program...")

	return True


def command_manage_bookreaders(command=0):
	"""
	1. Add readed book
	2. Add note review
	3. Suggested book
	4. Back to main menu
	"""
	while command != 4:
		commandes = {1: "Add Readedbook", 2: "Add note review", 3: "Suggested book", 4: "Back to main menu"}
		print("------------COMMAND MANAGE BOOKREADER------------"
			  "\nPlease select your choice : "
			  "\n1. Add Readedbook"
			  "\n2. Add note review"
			  "\n3. Suggested book"
			  "\n4. Back to main menu")
		print("------------COMMAND MANAGE BOOKREADER------------")

		try:
			command = int(input("Your input : "))
		except ValueError:
			command = 0
		# Commands to implant

		if command not in commandes:
			command = 0  # Does nothing, just relaunch the command
		elif command == 1:
			if add_bookreaded(logged_username):
				command = 0
		elif command == 2:
			if review_book(username=logged_username, position_user=position(read_file("readers"), logged_username)):
				command = 0
		elif command == 3:
			if suggested_book():
				command = 0
		elif command == 4:
			print("Exiting program...")
	return True


def login():
	"""
	Username: logged_username
	If new user : Type "new"
	"""
	global logged_username
	logged_username = ""
	print("Please login. Type exit to exit")
	while True:
		while (user_exist(logged_username) is False) and (logged_username != 'new'):     # personne ne sait qu'il faut mettre new pour mettre un nouvel utilisateur
			logged_username = str(input("Username : "))
			if logged_username in ["exit()", "Exit()", "exit", "Exit"]:
				quit()

		if logged_username == "new":
			add_user()
			logged_username = ""
		else:
			return True


######### FONCTIONS #############

if __name__ == '__main__':
	welcome()
	if login():
		print("Welcome " + str(logged_username))
		if command_center():
			print("Exiting program...")
	print("Good bye !")
	quit()
