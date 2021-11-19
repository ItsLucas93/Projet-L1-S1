# Plan

## Structure du projet

```
├── Plan.md
├── README.txt
├── Ressources\ (Sujet)
│		├── Sujet\ Projet.pdf
│		└── books.txt
├── data
│		├── books.txt
│		├── booksread.txt
│		└── readers.txt
├── main.py
├── manage_system
│		├── manage_book.py
│		├── manage_files.py
│		└── manage_readers.py
└── suggestions
    	└── suggestsystem.py
```

## Calendrier / Deadlines

*Chaque semaine doit être inscrit dans le compte rendu `./Rapport.pdf` avec les actions qui ont été prises cette semaine, les problèmes rencontrés, solutions, etc.*


| Semaine      | Objectifs 										|
|--------------|------------------------------------------------|
| 22/11 | Faire la partie 1 (*Profil des lecteurs*)				|
| 29/11 | Faire la partie 2 (*Visiter le dépôt des livres*)		|
| 06/12 | Faire la partie 3 (*Système de recommendations*)		|
| 13/12 | Finaliser et paufiner	le menu							|


## Détails des parties

#### Menu 

- Choix (à l'ouverture du fichier):
(rajouter un système de login à l'ouverture du fichier)
	1. Profils des lecteurs
		1. Afficher un autre lecteur / soi-même
		2. Modifier son compte / profil
		3. Supprimer son compte
		4. Ajouter un compte
			1. Pseudonyme
			2. Genre
			3. Âge
			4. Style de lecture
				1. Plusieurs ?
				2. Un seul
			5. Livres lu selons livres dans `books.txt`
	2. Visiter le dépôt des livres
		1. Afficher tous les livres
		2. Ajouter un livre
		3. Modifier un livre
		4. Supprimer un livre
	3. Recommandation
		1. Noter un livre
		2. Suggérer un livre
	4. Sortir du programme
- Ne se ferme pas tant que exit n'est pas appelé 


#### Partie 1 - Profil des lecteurs / Gestion des lecteurs

- Ajouter un lecteur
- Afficher un lecteur
- Modifier un lecteur
- Supprimer un lecteur
- Système de Login
- Vérifier si le lecteur existe

#### Partie 2 - Visiter le dépôt des livres / Gestion des livres

- Ajouter des livres
- Afficher des livres
	1. Afficher par liste de 10, navigation par input(gauche droite)/listening keyboard left or right arrow
- Modifier un livre
- Supprimer un livre

#### Partie 3 - Système de recommendations

- Suggérer des livres
- Notes des livres



