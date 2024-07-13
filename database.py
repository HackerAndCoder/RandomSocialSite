import yaml

database_name = "database"

database_copy : dict = {}

def get_database_name():
	return

def set_database_name(name):
	global database_name
	database_name = name

def restore_from_disk():
	global database_copy

	with open(f"{database_name}.yml") as f:
		database_copy = yaml.load(f, yaml.FullLoader)

def save_to_disk():
	global database_copy
	with open(f"{database_name}.yml", "w") as f:
		f.write(yaml.dump(database_copy))

def does_user_exist(username):
	try:
		return str(username.lower()) in database_copy.keys()
	except:
		return False

def set_user_and_password(username, password):
	global database_copy
	database_copy[username.lower()] = str(password)

def is_right_password(username, password):
	return database_copy[username.lower()] == str(password)


if __name__ == "__main__":
	# do tests 
	restore_from_disk()
	print(database_copy)