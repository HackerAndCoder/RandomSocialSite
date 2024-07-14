import random, string

def make_random_post(word):
	gib = ''
	for i in range(100):
		gib += random.choice(string.ascii_letters)
	return f"{word} :{gib}"