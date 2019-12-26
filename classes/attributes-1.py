class Plant:
	plant = 'tree'

	def get_plant(self):
		return self.plant

plant_1 = Plant()
plant_2 = Plant()

print(plant_1.get_plant())  # tree
print(plant_2.get_plant())  # tree

plant_1.plant = 'bush'
plant_1.little_plant = 'flower' # new argument for object plant_1

print(plant_1.get_plant())  # bush
print(plant_2.get_plant())  # tree
print(plant_1.little_plant)  # flower
