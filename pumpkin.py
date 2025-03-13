import moving

growing_tiles = []

def farm():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()

			plant(Entities.Pumpkin)
			coords = x, y
			growing_tiles.append(coords)
			move(North)					
		move(East)
	

	while growing_tiles.len() > 0:
		coords = growing_tiles[0]
		x, y = coords
		moving.to(x, y)
		if can_harvest():
			growing_tiles.remove(coords)
		else:
			growing_tiles.append(growing_tiles.pop(0))
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)

	harvest()