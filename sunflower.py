import moving

min_petals = 7
max_petals = 15
different_petal_count = max_petals - min_petals + 1

def plant_sunflower():
	while get_water() < 0.5:
		use_item(Items.Water)

	plant(Entities.Sunflower)


def farm():
	while num_items(Items.Power) < 100000:
		petal_measures = []

		for i in range(different_petal_count):
			petal_measures.append([])
			
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				moving.to(x, y)
				if get_ground_type() != Grounds.Soil:
					till()
				
				plant_sunflower()
				petal_count = measure()
				coords = x, y
				measure_score = petal_count - min_petals
				petal_measures[measure_score].append(coords)
			
		for i in range(different_petal_count):
			while petal_measures[8 - i].len() > 0:
				coords_to_check = petal_measures[8 - i]
				x, y = coords_to_check.pop(0)
				moving.to(x, y)
				coords = x, y

				if can_harvest():
					power = num_items(Items.Power)
					harvest()
					quick_print(num_items(Items.Power) - power)

				else:
					coords_to_check.append(coords)


