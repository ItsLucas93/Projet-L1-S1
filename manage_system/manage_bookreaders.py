from manage_system.manage_files import write_file, read_file

def add_bookreader(username):
	"""
	Add user in booksread
	"""
	write_file("booksreader_add", username)