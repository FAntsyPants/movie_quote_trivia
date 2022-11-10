import random

import requests
import json
from random import randint,shuffle
import os
from dotenv import load_dotenv
load_dotenv()
API = os.environ.get('API_KEY')

url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"

querystring = {"count":"10","cat":"movies"}

headers = {
	"X-RapidAPI-Key": API,
	"X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

parsed = json.loads(response.text)

#getting quote answer from API
correct = random.choice(parsed)
#getting correct movie from API
correct_author = correct['author']

def provide_answers():
	#defining a list to put the answer selections in
	answers = []
	#making sure the correct movie is there
	answers.append(correct_author)
	#adding 3 more movies to the choices and adding them to the list
	random_author = random.sample(parsed, k=3)
	if correct in random_author:
		provide_answers()
	for i in random_author:
		answers.append(i['author'])
		# making an enumerated list then giving the option to choose
	#https://stackoverflow.com/questions/55754219/how-can-i-print-a-numbered-list-using-elements-from-another-list
	random.shuffle(answers)
	for i, item in enumerate(answers,1):
		print(i, item)
	#allowing user input in menu
	input_index = int(input('Which movie is this quote from?\n'.format(len(answers))))
	user_choice = answers[input_index - 1]
	#validating answer
	if user_choice == correct_author:
		print("Congratulations! You guessed the correct movie.")
		quit()
	else:
		print("wrong!")
	print(f"The correct answer is {correct_author}")




print(f"\"{correct['quote']}\"")
provide_answers()
