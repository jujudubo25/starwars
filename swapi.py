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


def get_starships(index):
	data = requests.get('https://www.swapi.co/api/people/%d' % (index))
	data = json.loads(data.text)
	try:
		for x in range(len(data['starships'])):
			data['starships'][x] = info(data['starships'][x])
		return data['starships']
	except  IndexError:
		return None

def get_homeworld(index):
	data = requests.get('https://www.swapi.co/api/people/%d' % (index))
	data = json.loads(data.text)
	try:
		data['homeworld'] = info(data['homeworld'])
		return data['homeworld']
	except  IndexError:
		return None

def info(url):
    data = requests.get(url)
    data = json.loads(data.text)
    if 'name' in data:
    	return data['name']
    elif 'title' in data:
    	return data['title'] 


def films(title):
    """
    Take the name of a movie as a parameter and return it's index in the
    Star Wars JSON API (SWAPI). Return `None` if there is no match.
    """
    itername = ''
    index = 1
    while itername != title and index < 15:
        film = requests.get('https://www.swapi.co/api/films/%d' % (index))
        data = json.loads(film.text)
        if data.get('title') == title:
            return index
        else:
            index += 1
    return

def character(name):
	"""
    Take the name of a person as a parameter and return it's index in the
    Star Wars JSON API (SWAPI). Return `None` if there is no match.
    """
	itername = ''
	index = 1
	while itername != name and index < 100:
		person = requests.get('https://www.swapi.co/api/people/%d' % (index))
		data = json.loads(person.text)
		if data.get('name') == name:
			return index
		else:
			index += 1
	return

def planets(name):
	"""
    Take the name of a planet as a parameter and return it's index in the
    Star Wars JSON API (SWAPI). Return `None` if there is no match.
    """
	itername = ''
	index = 1
	while itername != name and index < 100:
		planet = requests.get('https://www.swapi.co/api/planets/%d' % (index))
		data = json.loads(planet.text)
		if data.get('name') == name:
			return index
		else:
			index += 1
	return index - 1

def species(name):
    """
    Take the name of a species as a parameter and return it's index in the
    Star Wars JSON API (SWAPI). Return `None` if there is no match.
    """
    itername = ''
    index = 1
    while itername != name and index < 100:
        species = requests.get('https://www.swapi.co/api/species/%d' % (index))
        data = json.loads(species.text)

        if data.get('name') == name:
            return index
        else:
            index += 1
    return index - 1

def vehicles(name):
	"""
    Take the name of a vehicle as a parameter and return it's index in the
    Star Wars JSON API (SWAPI). Return `None` if there is no match.
    """
	itername = ''
	index = 1
	while itername != name and index < 100:
		vehicle = requests.get('https://www.swapi.co/api/vehicles/%d' % (index))
		data = json.loads(vehicle.text)
		if data.get('name') == name:
			return index
		else:
			index += 1
	return index - 1

def starships(name):
    """
    Take the name of a starship as a parameter and return it's index in the
    Star Wars JSON API (SWAPI). Return `None` if there is no match.
    """
    itername = ''
    index = 2
    while itername != name and index < 100:
        starship = requests.get('https://www.swapi.co/api/starships/%d' % (index))
        data = json.loads(starship.text)

        if data.get('name') == name:
            return index
        else:
            index += 1
    return index - 1






def callPlanet():
	name = input('Which Star Wars planet would you like to learn about? ')
	print()
	index = planet(name)
	myReq = requests.get('https://www.swapi.co/api/planets/%d' % (index))
	data = json.loads(myReq.text)
	for key in data.keys():
		print(key, ":", data[key])
		print('-'* 50)	
	print()
	print()
	print('-'* 50)

def callSpecies():
	name = input('Which Star Wars species would you like to learn about? ')
	print()
	index = species(name)
	myReq = requests.get('https://www.swapi.co/api/species/%d' % (index))
	data = json.loads(myReq.text)
	for key in data.keys():
		print(key, ":", data[key])
		print('-'* 50)	
	print()
	print()
	print('-'* 50)


def callFilms():
	name = input('Which Star Wars film would you like to learn about? ')
	print()
	index = films(name)
	myReq = requests.get('https://www.swapi.co/api/films/%d' % (index))
	data = json.loads(myReq.text)
	for key in data.keys():
		print(key, ":", data[key])
		print('-'* 50)	
	print()
	print()
	print('-'* 50)


def callStarships():
	name = input('Which Star Wars starship would you like to learn about? ')
	print()
	index = starships(name)
	myReq = requests.get('https://www.swapi.co/api/starships/%d' % (index))
	data = json.loads(myReq.text)
	for key in data.keys():
		print(key, ":", data[key])
		print('-'* 50)	
	print()
	print()
	print('-'* 50)


def callVehicles():
	name = input('Which Star Wars vehicle would you like to learn about? ')
	print()
	index = vehicles(name)
	myReq = requests.get('https://www.swapi.co/api/vehicles/%d' % (index))
	data = json.loads(myReq.text)
	for key in data.keys():
		print(key, ":", data[key])
		print('-'* 50)	
	print()
	print()
	print('-'* 50)













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
