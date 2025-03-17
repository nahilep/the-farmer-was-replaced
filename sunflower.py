import moving

min_petals = 7
max_petals = 15

def plant_sunflower():
	while get_water() < 0.9:
		use_item(Items.Water)

	plant(Entities.Sunflower)


def farm():
	petal_measures = []

	for i in range(9):
		petal_measures.append([])
		
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			
			plant_sunflower()
			petal_count = measure()
			coords = x, y
			measure_score = petal_count - min_petals
			petal_measures[measure_score].append(coords)
						
			move(North)
		move(East)
		
	while num_items(Items.Power) < 10000:
		score_to_harvest = None

		while score_to_harvest == None:
			for i in range(9):
				if petal_measures[8 - i].len() > 0:
					score_to_harvest = 8 - i
					break

		coords_to_check = petal_measures[score_to_harvest]
		x, y = coords_to_check.pop(0)
		moving.to(x, y)
		coords = x, y

		if can_harvest():
			harvest()

			plant_sunflower()

			petal_count = measure()
			measure_score = petal_count - min_petals
			petal_measures[measure_score].append(coords)
		
		else:
			coords_to_check.append(coords)


