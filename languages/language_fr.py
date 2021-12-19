# main.py

text_bookmanager_language = "langue:"
text_bookmanager_from = ".depuis 1991###"

text_login_phase = "------------PHASE DE CONNEXION------------\nSi vous voulez quitter, entrez exit.\nSi vous voulez créer un compte, veuillez taper 'new'.\n------------PHASE DE CONNEXION ------------"
text_login_phase_input = "Nom d'utilisateur : "
text_login_phase_new = "new"
text_login_phase_separator = "------------PHASE DE CONNEXION------------"

text_welcome = "Bienvenue"
text_welcome_librarian = "\nJe suis le bibliothécaire et je suis heureux de vous voir ici !"

text_command_center = "------------MENU PRINCIPAL------------\nVeuillez sélectionner votre choix :\n1. Gérer les utilisateurs\n2. Gérer les livres\n3. Gérer les lecteurs de livre / Livres suggérés\n4. Quitter le programme\n------------MENU PRINCIPAL------------"
text_command_center_input = "Votre saisie : "
text_command_center_exit = "Sortie de centre du menu principal en cours..."

text_command_manage_reader = "------------MENU GESTION UTILISATEUR------------\nVeuillez sélectionner votre choix : \n1. Ajouter un utilisateur\n2. Modifier un profil\n3. Supprimer un utilisateur\n4. Afficher un profil\n5. Afficher tous les utilisateurs\n6. Retour au menu principal\n------------MENU GESTION UTILISATEUR------------"
text_command_manage_reader_input = "Votre saisie : "
text_command_manage_reader_exiting_1 = "Utilisateur ajouté !"
text_command_manage_reader_exiting_2 = "Profil utilisateur modifié !"
text_command_manage_reader_exiting_3 = "Une erreur s'est produite ou la commande a été abandonnée. Veuillez réessayer plus tard."
text_command_manage_reader_exiting_4 = "Sortie de la liste des utilisateurs..."
text_command_manage_reader_exit = "Sortie du menu gestion utilisateur en cours..."

text_command_manage_book = "------------MENU GESTION LIVRE------------\nVeuillez sélectionner votre choix :\n1. Ajouter un livre\n2. Renommer le livre\n3. Supprimer livre\n4. Liste les livres\n5. Retour au menu principal\n------------MENU GESTION LIVRE------------"
text_command_manage_book_input = "Votre saisie : "
text_command_manage_book_exiting_1 = "Livre ajouté !"
text_command_manage_book_exiting_2 = "Livre modifié."
text_command_manage_book_exiting_3 = "Livre supprimé."
text_command_manage_book_exiting_4 = "Une erreur s'est produite..."
text_command_manage_book_exit = "Sortie du menu de gestion du livre en cours..."

text_command_manage_bookreaders = "------------MENU GESTION LECTEURS DE LIVRE / SUGGESTIONS DE LIVRE------------\nVeuillez sélectionner votre choix : \n1. Ajouter une lecture à votre profil\n2. Évaluer un livre\n3. Chercher une suggestion de livre\n4. Retour au menu principal\n------------MENU GESTION LECTEURS DE LIVRE / SUGGESTIONS DE LIVRE------------"
text_command_manage_bookreaders_input = "Votre saisie : "
text_command_manage_bookreaders_exit = "Sortie du menu de gestions des lecteurs de livre en cours..."

text_command_manage_settings = "------------PARAMETRES (menu secret)-----------\nVeuillez noter qu'à la fin des processus 1 & 2, le programme s'arrêtera .\nVeuillez sélectionner votre choix : \n1. Changer la langue\n2. Réinitialiser les paramètres d'usine(données)\n3. Retour au menu principal\n------------PARAMETRES------------"
text_command_manage_settings_input = "Votre saisie : "

text_exit_1 = "Au revoir"
text_exit_2 = "A bientôt !"

# manage_system/utilities_func.py

text_ask_username_input = "-------------------------\nVeuillez saisir votre nom d'utilisateur : \nMin. 3 caractères\nMax. 16 caractères\n------------------------\nVotre saisie : "
text_ask_username_input_failed_1 = "Utilisateur avec le nom d'utilisateur"
text_ask_username_input_failed_2 = "existe déjà ! Veuillez essayer un autre nom d'utilisateur."

text_ask_gender_input = "------------------------\nVeuillez saisir votre genre: \n1. HOMME\n2. FEMME\n3. PEU IMPORTE\n------------------------\nVotre saisie : "

text_ask_age_input = "------------\nVeuillez saisir votre âge : \n1. <= 18 ans\n2. Entre 18 & 25 ans\n3. > 25 ans\n------------------------\nVotre saisie : "

text_ask_preferences = "------------------------\nEntrez votre style de lecture :\n1. Science-fiction\n2. Biographie\n3. Horreur\n4. Romance \n5. Fable\n6. Histoire\n7. Comédie\n------------------------\nVotre saisie : "

# manage_system/manage_readers.py

text_add_user_separator = "------------AJOUTER UN UTILISATEUR ------------"

text_remove_user_input = "Entrez un nom d'utilisateur (entrez exit pour quitter) : "
text_remove_user_warning = "-=-=-=-=-=- ATTENTION -=-=-=-=-=-\nVous allez supprimer un profil du stockeur de données.\nVoulez-vous continuer ?\n Si oui, le programme s'arrêtera."
text_remove_user_warning_confirm = "Votre saisie (Oui/Non): "

text_show_users_separator = "------------LISTE DES UTILISATEURS------------"
text_show_users_separator_1 = "------------LISTE DES UTILISATEURS ("
text_show_users_separator_2 = "utilisateurs)------------"
text_show_users_separator_3 = "------------LISTE DES UTILISATEURS (Page"
text_show_users_separator_4 = ")------------"
text_show_users_commands_1 = "------------COMMANDES------------\nVeuillez sélectionner votre choix : \n2. Page précédente\n3. Quitter\n------------COMMANDES------------"
text_show_users_commands_2 = "------------COMMANDES------------\nVeuillez sélectionner votre choix : \n1. Page précédente\n3. Quitter\n------------COMMANDES------------"
text_show_users_commands_3 = "------------COMMANDES------------\nVeuillez sélectionner votre choix : \n1. Page précédente\n2. Page suivante\n3. Quitter\n ------------COMMANDES------------"

text_modify_user_separator = "------------MODIFIER L'UTILISATEUR------------"
text_modify_user_input_request = "Entrez un nom d'utilisateur : "
text_modify_user_command = "------------MENU MODIFICATION UTILISATEUR------------\nVeuillez sélectionner votre choix : \nVous ne pouvez pas changer le nom d'utilisateur, veuillez supprimer le compte et en recréer un.\n1. Modifier le genre\n2. Modifier l'âge\n3. Modifier les préférences\n4. Retour au menu principal\n------------MENU MODIFICATION UTILISATEUR------------"
text_modify_user_input = "Votre saisie : "

text_show_user_input = "Entrez un nom d'utilisateur : "
text_show_user_separator = "------------VOTRE PROFIL ------------"
text_show_user_username = "Nom d'utilisateur : "
text_show_user_gender_1 = "Genre : Homme"
text_show_user_gender_2 = "Genre : Femme"
text_show_user_gender_3 = "Genre : Peu importe"
text_show_user_age_1 = "Age : < 18 ans"
text_show_user_age_2 = "Age : 18-25 ans"
text_show_user_age_3 = "Age : > 25 ans"
text_show_user_preference_1 = "Préférences : Sciences Fiction"
text_show_user_preference_2 = "Préférences : Biographie"
text_show_user_preference_3 = "Préférences : Horreur"
text_show_user_preference_4 = "Préférences : Romance"
text_show_user_preference_5 = "Préférences : Fable"
text_show_user_preference_6 = "Préférences : Historique"
text_show_user_preference_7 = "Préférences : Comédie"
text_show_user_books_readed = "Livres lus : \n»»» "
text_show_user_books_note = "Note"
text_show_user_books_no_book_readed_yet = "Aucun livre n'a encore été lu."

# manage_system/manage_bookreaders.py

text_show_book_readed_separator = "------------LIVRES LUS------------"

text_add_bookreaded_separator = "------------LISTE DE LIVRES------------"
text_add_bookreaded_input_request_1 = "Veuillez saisir l'identifiant du livre que vous souhaitez ajouter à votre profil."
text_add_bookreaded_input_request_2 = "Si vous voulez quitter, veuillez entrer 0"
text_add_bookreaded_input_1 = "Votre saisie : "
text_add_bookreaded_already_readed_book = "Vous avez déjà lu le livre ! Veuillez essayer un autre livre."
text_add_bookreaded_book_added = "Livre ajouté à votre profil !"

text_add_bookreaded_input_request_3 = "Voulez-vous évaluer le livre ? (Oui/Non)"
text_add_bookreaded_input_2 = "Votre saisie : "
text_add_bookreaded_end_review_book = "Fin du processus d'évaluation. Retour au menu d'ajout de livre sur votre profil."

# manage_system/manage_book.py

text_add_book_input_request = "Entrez le nom du livre : "
text_add_book_input_fail = "Le livre existe déjà !"

text_delete_book_input_request = "Entrez le nom du livre : "

text_modify_book_input_request_1 = "Entrez le nom du livre : "
text_modify_book_input_request_2 = "Entrez le nouveau nom du livre : "

text_show_book_separator = "------------LISTE DE LIVRES------------"

# suggestion/manage_review.py

text_review_book_show_user_books_readed_separator = "------------LIVRES LUS------------"
text_review_book_show_user_books_readed = "Livres lus : \n»»» "
text_review_book_show_user_books_note = "Note"
text_review_book_input_request_1 = "Entrez l'identifiant du livre que vous souhaitez évaluer (que vous avez lu), entrez 0 pour quitter : "
text_review_book_input_request_not_readed = "Veuillez entrer un livre que vous avez lu !"
text_review_book_input_request_2 = "Veuillez donner une note de 1 à 5 : "

# suggestion/manage_suggest.py

text_suggestion_recommend = "Livres recommandés : "
text_suggestion_recommend_exit = "Vous serez redirigé vers le menu lecteur de livres / suggestions de livres. Si vous souhaitez ajouter ces livres, accédez au centre d'ajout de livres lus. Après cela, si vous souhaitez évaluer le livre, accédez au centre d'évaluation de livres."

