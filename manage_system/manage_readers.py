from manage_files import read_file

def add_user():
	"""
	Ajoute un utilisateur dans le fichier ./data/readers.txt
	"""

	# Import de la liste data

	data = read_file("books")

	username, already_exist = "", True
	while ((len(username) <= 0 or len(username) > 16) and (already_exist is True)):
		username = str(input("Saisir votre pseudonyme \nMinimum 3 caractères \nMaximum 16 caractères \nVotre saisie : "))


	genre = 0
	while ((genre < 0) or (genre > 3)):
		genre = int(input("Saisir votre genre : \n1. HOMME\n2. FEMME\n3.PEU IMPORTE\nVotre saisie : "))

	age = 0
	while ((age < 0) or (age > 3)):
		age = int(input("Saisir votre âge : \n1. <= 18 ans\n2. Entre 18 et 25 ans\n3. > 25 ans\nVotre saisie : "))

	preferences = 0
	while ((preferences < 0) or (preferences > 7):
		preferences = int(input("Saisir votre style de lecture : \n1. Sciences fiction\n2. Biographie\n3. Horreur\n4. Romance\n5. Fable \n6. Histoire \n7. Comédie \nVotre saisie :"))

	### Implémenter la partie 'Quels livres avez vous lu ?'