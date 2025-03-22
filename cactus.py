import moving

measurements = []

def plant_cactus():
	while get_water() < 0.5:
		use_item(Items.Water)

	if get_ground_type() != Grounds.Soil:
		till()

	plant(Entities.Cactus)

def plant_square(size = get_world_size()):
	global measurements

	measurements = []

	for i in range(size):
		measurements.append([])

	for x in range(size):
		for y in range(size):
			moving.to(x, y)
			plant_cactus()
			measurements[y].append(measure())
			sort_field(x, y, size)

	sort_square(size)

def move_to_and_swap(x, y, direction):
	swap(direction)

def swap_with_measurement(x, y, direction):
	global measurements

	moving.to(x, y)

	if direction == West and measure(West) and measure(West) > measure():
		move_to_and_swap(x, y, West)
		measurement_here = measurements[y][x]
		measurements[y][x] = measurements[y][x - 1]
		measurements[y][x - 1] = measurement_here

	if direction == East and measure(East) and measure(East) < measure():
		move_to_and_swap(x, y, East)
		measurement_here = measurements[y][x]
		measurements[y][x] = measurements[y][x + 1]
		measurements[y][x + 1] = measurement_here

	if direction == South and measure(South) and measure(South) > measure():
		move_to_and_swap(x, y, South)
		measurement_here = measurements[y][x]
		measurements[y][x] = measurements[y - 1][x]
		measurements[y - 1][x] = measurement_here

	if direction == North and measure(North) and measure(North) < measure():
		move_to_and_swap(x, y, North)
		measurement_here = measurements[y][x]
		measurements[y][x] = measurements[y + 1][x]
		measurements[y + 1][x] = measurement_here


def sort_field(x, y, size = get_world_size()):
	global measurements

	hasSwapped = False
	if x > 0 and measure(West):
		if swap_with_measurement(x, y, West):
			hasSwapped = True
	if x < size - 1 and measure(East):
		if swap_with_measurement(x, y, East):
			hasSwapped = True
	if y > 0 and measure(South):
		if swap_with_measurement(x, y, South):
			hasSwapped = True
	if y < size - 1 and measure(North):
		if swap_with_measurement(x, y, North):
			hasSwapped = True

	return hasSwapped

def sort_square(size = get_world_size()):
	hasSwapped = True

	while hasSwapped:
		hasSwapped = False

		for x in range(size):
			for y in range(size):
				moving.to(x, y)
				result = sort_field(x, y, size)
				if result:
					hasSwapped = True

def farm():
	global measurements

	plant_square()
	quick_print(measurements)
	harvest()
	