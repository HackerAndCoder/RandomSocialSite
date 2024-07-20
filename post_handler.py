import yaml, os, json, random, re, time, datetime, math

keywords = {
		'technology': ['tech', 'technology', 'gadgets', 'AI', 'artificial intelligence', 'machine learning', 'ML', 'data science', 'robotics', 'innovation', 'software', 'hardware'],
		'music': ['music', 'song', 'songs', 'band', 'album', 'concert', 'artist', 'musician', 'rock', 'pop', 'hip hop', 'jazz', 'classical', 'playlist'],
		'sports': ['sports', 'game', 'games', 'tournament', 'player', 'match', 'athlete', 'team', 'football', 'soccer', 'basketball', 'tennis', 'baseball', 'golf'],
		'travel': ['travel', 'trip', 'destination', 'vacation', 'tour', 'tourism', 'holiday', 'explore', 'adventure', 'beach', 'mountains', 'city', 'road trip'],
		'food': ['food', 'recipe', 'cooking', 'cuisine', 'dish', 'meal', 'restaurant', 'taste', 'flavor', 'ingredient', 'baking', 'dining'],
		'health': ['health', 'wellness', 'fitness', 'exercise', 'workout', 'nutrition', 'diet', 'mental health', 'well-being', 'yoga', 'meditation', 'healthcare'],
		'education': ['education', 'learning', 'school', 'university', 'college', 'course', 'study', 'teacher', 'student', 'class', 'homework', 'degree'],
		'finance': ['finance', 'money', 'investment', 'stocks', 'market', 'economy', 'banking', 'savings', 'budget', 'crypto', 'cryptocurrency', 'taxes'],
		'entertainment': ['entertainment', 'movie', 'film', 'TV', 'show', 'series', 'theater', 'music', 'concert', 'festival', 'celebrity', 'actor', 'actress'],
		'fashion': ['fashion', 'style', 'clothing', 'outfit', 'designer', 'brand', 'trend', 'accessory', 'wear', 'look', 'vintage', 'runway'],
		'science': ['science', 'research', 'experiment', 'study', 'biology', 'chemistry', 'physics', 'space', 'astronomy', 'geology', 'scientist', 'discovery'],
		'politics': ['politics', 'government', 'policy', 'election', 'vote', 'law', 'senate', 'congress', 'president', 'democracy', 'campaign', 'debate'],
		'business': ['business', 'company', 'corporate', 'entrepreneur', 'startup', 'industry', 'market', 'trade', 'commerce', 'enterprise', 'management'],
		'art': ['art', 'painting', 'sculpture', 'drawing', 'gallery', 'museum', 'artist', 'exhibition', 'design', 'craft', 'creative', 'illustration'],
		'literature': ['literature', 'book', 'novel', 'poetry', 'author', 'writer', 'fiction', 'non-fiction', 'story', 'reading', 'library', 'publication']
	}

def get_plaintext_file(path):
    with open(os.path.join('site', path)) as f:
        return f.read()


def get_post_id_number():
	with open('post_number.txt') as f:
		return int(f.read())

def set_post_id_number(number):
	with open('post_number.txt', 'w') as f:
		f.write(str(int(number)))

def increment_post_id_number():
	set_post_id_number(get_post_id_number() + 1)

def is_post_number_used(num):
	return False

def new_post(username, post_text):
	increment_post_id_number()
	with open(os.path.join("posts", str(get_post_id_number())), 'w') as f:
		c = {"username": username, 
	   "message": post_text, 
	   "tags": get_post_tags(post_text), 
	   "likes": 0, 
	   "days": math.floor(round(time.time()) / 86400)}
		
		#f.write(yaml.dump(c))
		f.write(json.dumps(c))
		f.truncate()
	
	with open(os.path.join("users", username), 'r+') as f:
		try:
			c = json.loads(f.read())
		except json.decoder.JSONDecodeError as e: # file is empty
			print(e)
			c = {"posts": [], "liked": [], "sway": {}}
			for i in keywords.keys():
				c["sway"][i] = 0
			print(f"User: {username} does not have any posts, posting")
		#c = yaml.load_all(f.read(), yaml.FullLoader)
		c["posts"].append(get_post_id_number())
		f.seek(0)
		f.write(json.dumps(c))
		f.truncate()
		

	with open("post_list.data", "r+") as f:
		try:
			c = json.loads(f.read())
		except: # file is empty
			c = {"posts": [], "taged": {}}
		
		c["posts"].append(get_post_id_number())
		for tag in get_post_tags(post_text):
			try:
				c["tagged"][tag].append(get_post_id_number())
			except:
				c["tagged"][tag] = []
				c["tagged"][tag].append(get_post_id_number())
		f.seek(0)
		f.write(json.dumps(c))
		f.truncate()

def get_posts(username):
	with open(os.path.join("users", username)) as f:
		c = json.loads(f.read())
		#c = yaml.load_all(f.read(), yaml.FullLoader)
		if not c["posts"]: 
			return None
		else: return c["posts"]

def get_post(id):
	try:
		with open(os.path.join("posts", str(id))) as f:
			#c = yaml.load_all(f, yaml.FullLoader)
			return json.loads(f.read())
	except:
		print(f'Error: no post: {id}')
		return {"username": "null", "message": "null", "tags":[], "likes": 0, "days": 0}
	
def get_recommended_posts(username, load_length = 100):


	# THIS IS TEMPORARY CODE WHILE WE WAIT FOR NEW POSTS TO COME IN: DELETE ASAP WHEN DONE!!

	
	'''import temp_random_populator

	for i in range(100):
		new_post("bot", temp_random_populator.make_random_post())
	
	'''


	

	current_day = math.floor(round(time.time()) / 86400)

	time_interest_reduction = 1 # interest reduced per day
	user_interest = 2

	population = [random.randint(1, get_post_id_number()) for _ in range(load_length)]
	with open(os.path.join("users", username), 'r+') as f:
		try:
			userinfo = json.loads(f.read())
		except:
			userinfo = {"posts": [], "liked": [], "sway": {}}
			for i in keywords.keys():
				userinfo["sway"][i] = 0
			
			f.seek(0)
			f.write(json.dumps(userinfo))
			f.truncate()
	
	post_likeness = {}

	user_sway = userinfo["sway"]
	for post in population:
		user_likeness = 0
		for tag in get_post_tags(get_post(post)["message"]):
			user_likeness += user_sway[tag]
		
		try:
			user_likeness += get_post(post)["username"] * user_interest
		except: # the user has never interected with that accouts posts so do nothing
			pass

		#print(get_post(post))

		user_likeness -= (current_day - int(get_post(post)["days"])) * time_interest_reduction
		post_likeness[post] = user_likeness
	
	sorted_items = sorted(post_likeness.items(), key=lambda item: item[1])
	sorted_items.reverse()
	
	return_stuff = []

	for i in range(load_length // 10 if len(sorted_items) > load_length//10 else len(sorted_items) -1):
		return_stuff.append(sorted_items[i][0])
	
	print(f'User {username} likes {get_post(return_stuff[0])["tags"]}')
	
	#return_stuff.append(sorted_items[-1][0]) # recommend a random offtopic post to keep the users interest open


	#print(f'Username {username} has content: {return_stuff} from {sorted_items}')

	return return_stuff

	#return [random.randrange(0, get_post_id_number()+1) for _ in range(25)]

def get_formatted_post(username, post_id):
	post = get_post(post_id)
	
	return json.dumps({
			"message": post["message"],
			"username": post["username"],
			"id": post_id,
			"liked": has_user_liked_post(username, post_id),
			"like_num": post["likes"]
		}
	)

def get_tag_words(tag):
	if tag.lower() in keywords.keys():
		return keywords[tag]
	else:
		return [""]
	
def get_post_tags(post_content):
	text = post_content.lower()
	text = re.sub(r'\W+', ' ', text)
	tokens = text.split()

	tags = set()
	for tag, keywords_list in keywords.items():
		if any(keyword in tokens for keyword in keywords_list):
			tags.add(tag)
    
	return list(tags)

def like_post(username, post_id):
	post_id = int(post_id)
	with open(os.path.join("users", username), 'r+') as f:
		info = json.loads(f.read())
		if not post_id in info["liked"]:
			info["liked"].append(post_id)

			post_tags = get_post(post_id)["tags"]
			for i in post_tags:
				info["sway"][i] += 1
			
			try:
				_ = info["sway"]["users"]
			except:
				info["sway"]["users"] = {}
			
			try:
				_ = info["sway"]["users"][username]
			except:
				info["sway"]["users"][username] = 0

			info["sway"]["users"][username] += 1
			
			f.seek(0)
			f.write(json.dumps(info))
	
	with open(os.path.join("posts", str(post_id)), "r+") as f:
		data = json.loads(f.read())
		data["likes"] += 1
		f.seek(0)
		f.write(json.dumps(data))

def unlike_post(username, post_id):
	post_id = int(post_id)
	with open(os.path.join("users", username), 'r+') as f:
		info = json.loads(f.read())
		if post_id in info["liked"]:
			info["liked"].remove(post_id)

			post_tags = get_post(post_id)["tags"]
			for i in post_tags:
				if info["sway"][i] > 0:
					info["sway"][i] -= 1
			
			try:
				_ = info["sway"]["users"]
			except:
				info["sway"]["users"] = {}
			
			try:
				_ = info["sway"]["users"][username]
			except:
				info["sway"]["users"][username] = 0

			info["sway"]["users"][username] -= 1
			
			f.seek(0)
			f.write(json.dumps(info))
			f.truncate()
	
	with open(os.path.join("posts", str(post_id)), "r+") as f:
		data = json.loads(f.read())
		data["likes"] -= 1
		f.seek(0)
		f.write(json.dumps(data))

def has_user_liked_post(username, post_id : int):
	with open(os.path.join("users", username)) as f:
		info = json.loads(f.read())
		if int(post_id) in info["liked"]:
			return True
		return False