def farm():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Carrot)
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			move(North)					
		move(East)		