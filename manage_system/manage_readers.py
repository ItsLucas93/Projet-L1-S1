from manage_files import read_file, write_file

"""
Les fonctions retournent des bool pour déclarer si les opérations se sont déroulés avec succès.
En cas de False: Message d'erreur.
"""


def add_user():
	"""
	Ajoute un utilisateur dans le fichier ./data/readers.txt
	"""

	# Import de la liste data

	data = read_file("readers")

	# Entrée utilisateur

	username = ""
	while ((len(username) <= 0 or len(username) > 16) and (user_exist(username) is True)):
		username = str(input("Saisir votre pseudonyme \nMinimum 3 caractères \nMaximum 16 caractères \nVotre saisie : "))

	genre = 0
	while ((genre < 0) or (genre > 3)):
		genre = int(input("Saisir votre genre : \n1. HOMME\n2. FEMME\n3.PEU IMPORTE\nVotre saisie : "))

	age = 0
	while ((age < 0) or (age > 3)):
		age = int(input("Saisir votre âge : \n1. <= 18 ans\n2. Entre 18 et 25 ans\n3. > 25 ans\nVotre saisie : "))

	preferences = 0
	while ((preferences < 0) or (preferences > 7)):
		preferences = int(input("Saisir votre style de lecture : \n1. Sciences fiction\n2. Biographie\n3. Horreur\n4. Romance\n5. Fable \n6. Histoire \n7. Comédie \nVotre saisie :"))

	### Implémenter la partie 'Quels livres avez vous lu ?
	### IMPLEMENTER write_file("readers", data)
	return True


def remove_user(username):
	"""
	Supprime un utilisateur dans le fichier ./data/readers.txt
	"""

	assert user_exist(username) == True, "Cet utilisateur n'existe pas"

	# Import de la liste data
	data = read_file("readers")

	i = 0
	while ((i < len(data)) and (data[i][0] != username)):
		i += 1

	# Cas où l'utilisateur ne figure pas dans la base car i > len(data)
	if i > len(data):
		return False
	# Cas où l'utilisateur figure dans la base
	else:
		del data[i]
		### IMPLEMENTER write_file("readers", data)
		return True


def user_exist(username):
	"""
	Vérifie si l'utilisateur existe dans le fichier ./data/readers.txt
	"""

	# Import de la liste data
	data = read_file("readers")
	cond = False

	for i in data:
		for j in i:
			if (j == username):
				cond = True
	return cond

def show_users():
	"""
	Affiche la liste des utilisateurs présents dans ./data/users
	"""
	data = read_file("readers")
	
	

	if (data < 25):
		print("------------USERS LIST------------")
		for i in range(len(data)):
			print(data[i][0])
		print("------------USERS LIST------------")	
	else:
		pages = len(data) // 25
		page = 0

		while True:

			print("------------USERS LIST (Page " + str(page) + "/" + str(pages) + ")------------")
			for i in range(page * 25, (page + 1) * 25): # vérifier la relation entre page actuel et 
				print(data[i][0])
			print("------------USERS LIST (Page " + str(page) + "/" + str(pages) + ")------------")


			commandes = {0: "Page précédente", 1: "Page suivante", 2: "Exit"}
			print("Liste des commandes : ", end=" ")
			if (page == 0):
				print("1 : " + str(commandes[1]) + " ; 2 : " + str(commande[2])) # à voir comment print la valeur de la clé associé en vue d'une implémentation future
			if (page == pages):
				print("0 : " + str(commandes[0]) + " ; 2 : " + str(commande[2]))
			else:
				print("0 : " + str(commandes[0]) + " ; 1 : " + str(commandes[1]) + " ; 2 : " + str(commande[2]))
			command = int(input("Votre entrée :"))

