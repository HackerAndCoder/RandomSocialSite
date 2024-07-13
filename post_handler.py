import yaml, os

def get_post_id_number():
	with open('post_number.txt') as f:
		return int(f.read())

def set_post_id_number(number):
	with open('post_number.txt', 'w') as f:
		f.write(int(number))

def increment_post_id_number():
	set_post_id_number(get_post_id_number() + 1)

def new_post(username, post_text):
	increment_post_id_number()
	with open(os.path.join("posts", str(get_post_id_number)), 'w') as f:
		c = {"username": username, "message": post_text}
		f.write(yaml.dump(c, f))
	
	with open(os.path.join("users", username), 'w+') as f:
		c = yaml.load_all(f.read(), yaml.FullLoader)
		if not c["posts"]: c["posts"] = []
		c["posts"].append(get_post_id_number())

def get_posts(username):
	with open(os.path.join("users", username)) as f:
		c = yaml.load_all(f.read(), yaml.FullLoader)
		if not c["posts"]: return None
		else: return c["posts"]

def get_post(id):
	try:
		with open(os.path.join("posts", id)) as f:
			c = yaml.load_all(f, yaml.FullLoader)
			return c
	except:
		return "Error"