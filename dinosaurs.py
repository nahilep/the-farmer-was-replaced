import moving

change_hat(Hats.Straw_Hat)
moving.to(0, 0)
change_hat(Hats.Dinosaur_Hat)

move_successful = True

while move_successful:
	size = get_world_size()
	x = get_pos_x()
	y = get_pos_y()

	if x == 0:
		if y < size - 1:
			move(North)
		else:
			move(East)
	elif y == 0:
		move(West)
	elif x % 2:
		if y > 1:
			move(South)
		else:
			if x == size - 1:
				move(South)
			else:
				move(East)
	else:
		if y < size - 1:
			move(North)
		else:
			move(East)
