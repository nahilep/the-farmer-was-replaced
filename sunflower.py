import moving

min_petals = 7
max_petals = 15

def farm():
	petal_measures = []

	for i in range(9):
		petal_measures.append([])
		
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			
			plant(Entities.Sunflower)		
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

		if can_harvest():
			debug = num_items(Items.Power)
			harvest()
			quick_print(num_items(Items.Power) - debug)

			plant(Entities.Sunflower)		
			petal_count = measure()
			coords = x, y
			measure_score = petal_count - min_petals
			petal_measures[measure_score].append(coords)
		
		else:
			coords = x, y
			coords_to_check.append(coords)


