import yaml, os, json, random, re

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
		c = {"username": username, "message": post_text, "tags": get_post_tags(post_text)}
		#f.write(yaml.dump(c))
		f.write(json.dumps(c))	
	
	with open(os.path.join("users", username), 'r+') as f:
		try:
			c = json.loads(f.read())
		except json.decoder.JSONDecodeError as e: # file is empty
			print(e)
			c = {"posts": []}
			print(f"User: {username} does not have any posts, posting")
		#c = yaml.load_all(f.read(), yaml.FullLoader)
		c["posts"].append(get_post_id_number())
		f.seek(0)
		f.write(json.dumps(c))
		

	with open("post_list.data", "r+") as f:
		try:
			c = json.loads(f.read())
		except: # file is empty
			c = {"posts": []}
		
		c["posts"].append(get_post_id_number())
		f.seek(0)
		f.write(json.dumps(c))

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
		return {"username": "null", "message": "null"}
	
def get_recommended_posts(username):
	return [random.randrange(0, get_post_id_number()+1) for _ in range(25)]

def format_post(post):
	return get_plaintext_file("template.html").replace('{message}', post["message"]).replace("{username}", post["username"])

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