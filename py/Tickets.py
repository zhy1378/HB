import math

Population = {
	'Ming': 22060,
	'Japan': 2900,
	'Korea': 1900,
	'Vietnam': 1700,
	'Myanmar': 900,
	'Northeast': 900,
	'Mongolei': 200,
	'WesternRegions': 270,
	'Tibet': 60,
	'Australia': 70,
	'America': 40
}

Total = 0
for country in Population:
	Total += Population[country]

NumTickets = 499

tickets = {}
stats = 0
for country in Population:
	ticket = round(Population[country] / Total * NumTickets)
	if ticket == 0:
		ticket = 1
	tickets[country] = ticket
	print(country + ' = ' + str(ticket))
	stats += ticket

print('Stats: ' + str(stats))