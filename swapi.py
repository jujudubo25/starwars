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