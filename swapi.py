import json
import requests

def get_vehicle(index):
	"""
	A function that gives the name of a vehicle specific to a certain person.
	"""
	data = requests.get('https://www.swapi.co/api/people/%d' % (index))
	data = json.loads(data.text)
	try:
		for x in range(len(data['vehicles'])):
			data['vehicles'][x] = info(data['vehicles'][x])
		return data['vehicles']
	except  IndexError:
		return None

def get_films(index):
	data = requests.get('https://www.swapi.co/api/people/%d' % (index))
	data = json.loads(data.text)
	try:
		for x in range(len(data['films'])):
			data['films'][x] = info(data['films'][x])
		return data['films']
	except  IndexError:
		return None

def get_species(index):
	data = requests.get('https://www.swapi.co/api/people/%d' % (index))
	data = json.loads(data.text)
	try:
		for x in range(len(data['species'])):
			data['species'][x] = info(data['species'][x])
		return data['species']
	except  IndexError:
		return None



















def main():
	"""
	Responsible for running the entire program,
	all functions are implemented into this function in a way that
	makes everything run easily. 
	"""
	exit = False
	while exit == False:
		print('1. View Characters')
		print('2. View Planets')
		print('3. View Species')
		print('4. View Films')
		print('5. View Starships')
		print('6. View vehicles')
		print('7. Quit')
		print()
		bigmood = input('Make a selection ')
		if bigmood == '1':
			callCharacter()	
		elif bigmood == '2':
			callPlanet()
		elif bigmood == '3':
			callSpecies()
		elif bigmood == '4':
			callFilms()
		elif bigmood == '5':
			callStarships()
		elif bigmood == '6':
			callVehicles()
		elif bigmood == '7':
			exit = True
		else:
			print('Unrecognized Input')

main()
