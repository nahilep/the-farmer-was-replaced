def move_steps(direction, steps = 1):
	for i in range(steps):
		move(direction)

def to(x, y):
	half_world_size = get_world_size() / 2

	if x != get_pos_x():
		distance = abs(x - get_pos_x())
		
		if x < get_pos_x():
			if distance <= half_world_size:
				move_steps(West, distance)
			else:
				move_steps(East, get_world_size() - distance)
		else:
			if distance < half_world_size:
				move_steps(East, distance)
			else:
				move_steps(West, get_world_size() - distance)

	if y != get_pos_y():
		distance = abs(y - get_pos_y())
		
		if y < get_pos_y():
			if distance <= half_world_size:
				move_steps(South, distance)
			else:
				move_steps(North, get_world_size() - distance)
		else:
			if distance < half_world_size:
				move_steps(North, distance)
			else:
				move_steps(South, get_world_size() - distance)
