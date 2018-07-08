country_counter = {}

def addone(counry):
	if counry in country_counter:
		country_counter[counry] += 1
	else:
		country_counter[counry] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))
