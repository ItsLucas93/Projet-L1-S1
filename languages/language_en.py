# main.py

text_bookmanager_language = "language:"
text_bookmanager_from = ".from 1991####"

text_login_phase = "------------LOGIN PHASE------------\nIf you want to exit, enter exit.\nIf you want to create an account, please type new.\n------------LOGIN PHASE------------"
text_login_phase_input = "Username : "
text_login_phase_new = "new"
text_login_phase_separator = "------------LOGIN PHASE------------"
text_login_rdv = "To add book on your profile, please go to the Manage Bookreader (after login enter 3) and go to Add Readedbook (enter 1) "

text_welcome = "Welcome"
text_welcome_librarian = "\nI'm the librarian and I'm happy to see you there !"

text_command_center = "------------COMMAND CENTER------------\nPlease select your choice :\n1. Manage Users\n2. Manage Books\n3. Manage Books Readers / Suggested books\n4. Exit program\n------------COMMAND CENTER------------"
text_command_center_input = "Your input : "
text_command_center_exit = "Exiting command center..."

text_command_manage_reader = "------------COMMAND MANAGE READER------------\nPlease select your choice : \n1. Add user\n2. Modify a profile\n3. Delete an user\n4. Show a profile\n5. Show all users\n6. Back to main menu\n------------COMMAND MANAGE READER------------"
text_command_manage_reader_input = "Your input : "
text_command_manage_reader_exiting_1 = "User added !"
text_command_manage_reader_exiting_2 = "User profile modified !"
text_command_manage_reader_exiting_3 = "Something went wrong or the command has been aborted. Please try again later."
text_command_manage_reader_exiting_4 = "Exiting user lists center..."
text_command_manage_reader_exit = "Exiting manage reader..."

text_command_manage_book =  "------------COMMAND MANAGE BOOK------------\nPlease select your choice :\n1. Add Book\n2. Rename book\n3. Delete book\n4. Lists books\n5. Back to main menu\n------------COMMAND MANAGE BOOK------------"
text_command_manage_book_input = "Your input : "
text_command_manage_book_exiting_1 = "Book added !"
text_command_manage_book_exiting_2 = "Book modified."
text_command_manage_book_exiting_3 = "Book removed."
text_command_manage_book_exiting_4 = "Something went wrong..."
text_command_manage_book_exit = "Exiting manage book menu..."

text_command_manage_bookreaders = "------------COMMAND MANAGE BOOKREADER------------\nPlease select your choice : \n1. Add Readedbook\n2. Add note review\n3. Suggested book\n4. Back to main menu\n------------COMMAND MANAGE BOOKREADER------------"
text_command_manage_bookreaders_input = "Your input : "
text_command_manage_bookreaders_exit = "Exiting program..."

text_command_manage_settings = "------------COMMAND SETTINGS (secret menu)------------\nPlease note that at the end of process 1 & 2, the program will shutdown.\nPlease select your choice : \n1. Change Language\n2. Reset factory\n3. Back to main menu\n------------COMMAND SETTINGS------------"
text_command_manage_settings_input = "Your input : "

text_exit_1 = "Goodbye"
text_exit_2 = "See you soon !"

# manage_system/utilities_func.py

text_ask_username_input = "------------------------\nPlease enter your username : \nMin. 3 char\nMax. 16 char\n------------------------\nYour input : "
text_ask_username_input_failed_1 = "User with the username"
text_ask_username_input_failed_2 = "already exist ! Please try another username."

text_ask_gender_input = "------------------------\nPlease enter your gender : \n1. MAN\n2. WOMAN\n3. DON'T CARE\n------------------------\nYour input : "

text_ask_age_input = "------------------------\nPlease enter your age : \n1. <= 18 yo\n2. Between 18 & 25 yo\n3. > 25 yo\n------------------------\nYour input : "

text_ask_preferences = "------------------------\nEnter your reading style :\n1. Science fiction\n2. Biography\n3. Horror\n4. Romance\n5. Fable\n6. History\n7. Comedy\n------------------------\nYour input : "

# manage_system/manage_readers.py

text_add_user_separator = "------------ADD USER------------"

text_remove_user_input = "Enter a username (enter exit to exit) : "
text_remove_user_warning = "-=-=-=-=-=- WARNING -=-=-=-=-=-\nYou're gonna delete a profile in data\nDo you want to proceed ?\n If yes, you will have to relaunch the program"
text_remove_user_warning_confirm = "Your input (Yes/No): "

text_show_users_separator = "------------USERS LIST------------"
text_show_users_separator_1 = "------------USERS LIST ("
text_show_users_separator_2 = "users)------------"
text_show_users_separator_3 = "------------USERS LIST (Page"
text_show_users_separator_4 = ")------------"
text_show_users_commands_1 = "------------COMMANDS------------\nPlease select your choice : \n2. Previous page\n3. Exit\n------------COMMANDS------------"
text_show_users_commands_2 = "------------COMMANDS------------\nPlease select your choice : \n1. Page précédente\n3. Exit\n------------COMMANDS------------"
text_show_users_commands_3 = "------------COMMANDS------------\nPlease select your choice : \n1. Page précédente\n2. Page suivante\n3. Exit\n------------COMMANDS------------"

text_modify_user_separator = "------------MODIFY USER------------"
text_modify_user_input_request = "Enter a username : "
text_modify_user_command = "------------COMMAND MODIFY USER------------\nPlease select your choice : \nYou can't change the username, please delete the account to proceed.\n1. Modify Gender\n2. Modify Age\n3. Modify Preferences\n4. Back to main menu\n------------COMMAND MODIFY USER------------"
text_modify_user_input = "Your input : "

text_show_user_input = "Enter a username : "
text_show_user_separator = "------------YOUR PROFILE------------"
text_show_user_username = "Username : "
text_show_user_gender_1 = "Gender : Man"
text_show_user_gender_2 = "Gender : Woman"
text_show_user_gender_3 = "Gender : Doesn't care"
text_show_user_age_1 = "Age : < 18 yo"
text_show_user_age_2 = "Age : 18-25 yo"
text_show_user_age_3 = "Age : > 25 yo"
text_show_user_preference_1 = "Preferences : Sciences Fiction"
text_show_user_preference_2 = "Preferences : Biography"
text_show_user_preference_3 = "Preferences : Horror"
text_show_user_preference_4 = "Preferences : Romance"
text_show_user_preference_5 = "Preferences : Fable"
text_show_user_preference_6 = "Preferences : History"
text_show_user_preference_7 = "Preferences : Comedy"
text_show_user_books_readed = "Books readed : \n»»» "
text_show_user_books_note = "Note"
text_show_user_books_no_book_readed_yet = "Not any book readed yet."

# manage_system/manage_bookreaders.py

text_show_book_readed_separator = "------------BOOKS READED------------"

text_add_bookreaded_separator = "------------BOOKS LIST------------"
text_add_bookreaded_input_request_1 = "Please enter the id of the book you want to add to your profile."
text_add_bookreaded_input_request_2 = "If you want to exit, please enter 0"
text_add_bookreaded_input_1 = "Your input : "
text_add_bookreaded_already_readed_book = "You're already readed the book ! Please try another book"
text_add_bookreaded_book_added = "Book added to your profile !"

text_add_bookreaded_input_request_3 = "Do you want to review the book ? (Yes/No)"
text_add_bookreaded_input_2 = "Your input : "
text_add_bookreaded_end_review_book = "End of review process. Back to add book on profile."

# manage_system/manage_book.py

text_add_book_input_request = "Enter the name of the book : "
text_add_book_input_fail = "The book already exist !"

text_delete_book_input_request = "Enter the name of the book : "

text_modify_book_input_request_1 = "Enter the name of the book : "
text_modify_book_input_request_2 = "Enter the new name of the book : "

text_show_book_separator = "------------BOOKS LIST------------"

# suggestion/manage_review.py

text_review_book_show_user_books_readed_separator = "------------BOOKS READED------------"
text_review_book_show_user_books_readed = "Books readed : \n»»» "
text_review_book_show_user_books_note = "Note"
text_review_book_input_request_1 = "Enter the id of the book you want to review (that you readed), enter 0 to exit : "
text_review_book_input_request_not_readed = "Please enter a book you readed ! "
text_review_book_input_request_2 = "Please give a grade from 1 to 5 : "

# suggestion/manage_suggest.py

text_suggestion_recommend = "Recommanded books : "
text_suggestion_recommend_exit = "You will be redirected to the Manage Bookreaders menu. If you want to add these book, go to the add readed book center. After that if you want to review the book, go to the review book center."

