import random, string

messages = [
  {"message": "Just had the best coffee ever at the new café in town!", "likes": 0, "days": 0, "tags": ["coffee", "café"]},
  {"message": "Completed a 5-mile run this morning. Feeling great!", "likes": 0, "days": 0, "tags": ["fitness", "running"]},
  {"message": "Watched a fantastic movie last night. Highly recommend it!", "likes": 0, "days": 0, "tags": ["movies", "recommendation"]},
  {"message": "Started reading a new book. Loving it so far.", "likes": 0, "days": 0, "tags": ["books", "reading"]},
  {"message": "Cooked a delicious homemade pizza for dinner.", "likes": 0, "days": 0, "tags": ["cooking", "pizza"]},
  {"message": "Had a relaxing day at the beach.", "likes": 0, "days": 0, "tags": ["beach", "relaxation"]},
  {"message": "Visited the local farmer's market and bought fresh produce.", "likes": 0, "days": 0, "tags": ["farmersmarket", "freshproduce"]},
  {"message": "Spent the afternoon gardening. My plants are thriving!", "likes": 0, "days": 0, "tags": ["gardening", "plants"]},
  {"message": "Went hiking in the mountains. The view was breathtaking.", "likes": 0, "days": 0, "tags": ["hiking", "mountains"]},
  {"message": "Attended a live concert. The music was amazing!", "likes": 0, "days": 0, "tags": ["concert", "music"]},
  {"message": "Tried a new recipe today and it turned out great.", "likes": 0, "days": 0, "tags": ["cooking", "recipe"]},
  {"message": "Had a fun game night with friends.", "likes": 0, "days": 0, "tags": ["games", "friends"]},
  {"message": "Started a new workout routine. Feeling motivated!", "likes": 0, "days": 0, "tags": ["fitness", "workout"]},
  {"message": "Took a relaxing walk in the park.", "likes": 0, "days": 0, "tags": ["walk", "park"]},
  {"message": "Spent the day exploring the city. Found some hidden gems.", "likes": 0, "days": 0, "tags": ["cityexploration", "travel"]},
  {"message": "Had a productive day working on a new project.", "likes": 0, "days": 0, "tags": ["work", "productivity"]},
  {"message": "Went to a local art gallery. The exhibits were beautiful.", "likes": 0, "days": 0, "tags": ["art", "gallery"]},
  {"message": "Had a relaxing spa day. Feeling rejuvenated.", "likes": 0, "days": 0, "tags": ["spa", "relaxation"]},
  {"message": "Tried a new restaurant for dinner. The food was delicious.", "likes": 0, "days": 0, "tags": ["restaurant", "food"]},
  {"message": "Spent the day volunteering at a local charity.", "likes": 0, "days": 0, "tags": ["volunteering", "charity"]},
  {"message": "Enjoyed a quiet evening reading a book.", "likes": 0, "days": 0, "tags": ["reading", "relaxation"]},
  {"message": "Went to a fun amusement park. Had a blast!", "likes": 0, "days": 0, "tags": ["amusementpark", "fun"]},
  {"message": "Baked some delicious cookies today.", "likes": 0, "days": 0, "tags": ["baking", "cookies"]},
  {"message": "Had a lovely picnic in the park.", "likes": 0, "days": 0, "tags": ["picnic", "park"]},
  {"message": "Went to a sports event. The game was intense!", "likes": 0, "days": 0, "tags": ["sports", "game"]},
  {"message": "Enjoyed a cozy night in watching TV shows.", "likes": 0, "days": 0, "tags": ["tvshows", "cozy"]},
  {"message": "Tried a new workout class. It was challenging but fun.", "likes": 0, "days": 0, "tags": ["workout", "fitness"]},
  {"message": "Had a great time at a friend's birthday party.", "likes": 0, "days": 0, "tags": ["birthday", "party"]},
  {"message": "Spent the day doing some DIY projects around the house.", "likes": 0, "days": 0, "tags": ["DIY", "projects"]},
  {"message": "Went to a local farmers' market and bought fresh produce.", "likes": 0, "days": 0, "tags": ["farmersmarket", "freshproduce"]},
  {"message": "Had a relaxing day at home watching movies.", "likes": 0, "days": 0, "tags": ["movies", "relaxation"]},
  {"message": "Started a new painting. Loving the creative process.", "likes": 0, "days": 0, "tags": ["painting", "creativity"]},
  {"message": "Spent the afternoon at the beach. The weather was perfect.", "likes": 0, "days": 0, "tags": ["beach", "weather"]},
  {"message": "Went for a bike ride around the neighborhood.", "likes": 0, "days": 0, "tags": ["bikeride", "neighborhood"]},
  {"message": "Had a delicious brunch with friends.", "likes": 0, "days": 0, "tags": ["brunch", "friends"]},
  {"message": "Visited a new museum exhibit. Learned so much.", "likes": 0, "days": 0, "tags": ["museum", "exhibit"]},
  {"message": "Took a road trip to a nearby town. It was a great adventure.", "likes": 0, "days": 0, "tags": ["roadtrip", "adventure"]},
  {"message": "Attended a cooking class. Learned some new recipes.", "likes": 0, "days": 0, "tags": ["cookingclass", "recipes"]},
  {"message": "Had a fun day shopping with friends.", "likes": 0, "days": 0, "tags": ["shopping", "friends"]},
  {"message": "Went to a local festival. The atmosphere was lively.", "likes": 0, "days": 0, "tags": ["festival", "fun"]},
  {"message": "Spent the day at a theme park. Had so much fun on the rides.", "likes": 0, "days": 0, "tags": ["themepark", "rides"]},
  {"message": "Enjoyed a quiet evening at home with a good book.", "likes": 0, "days": 0, "tags": ["reading", "relaxation"]},
  {"message": "Tried a new hobby today. Really enjoyed it.", "likes": 0, "days": 0, "tags": ["hobby", "enjoyment"]},
  {"message": "Had a productive day working on my goals.", "likes": 0, "days": 0, "tags": ["goals", "productivity"]},
  {"message": "Went to a yoga class. Feeling so relaxed.", "likes": 0, "days": 0, "tags": ["yoga", "relaxation"]},
  {"message": "Spent the afternoon baking bread. The house smells amazing.", "likes": 0, "days": 0, "tags": ["baking", "bread"]},
  {"message": "Had a fun day at the zoo. Loved seeing all the animals.", "likes": 0, "days": 0, "tags": ["zoo", "animals"]},
  {"message": "Went for a swim at the local pool.", "likes": 0, "days": 0, "tags": ["swimming", "pool"]},
  {"message": "Spent the evening stargazing. The sky was so clear.", "likes": 0, "days": 0, "tags": ["stargazing", "sky"]}
]


def make_random_post(word = None):
	message = random.choice(messages)["message"]

	return f"{message}"