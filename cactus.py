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
			# TODO: figure out why this crashes sometimes
			# sort_field(x, y, size)

	sort_square(size)

def swap_measurements(coords1, coords2):
	global measurements

	x1, y1 = coords1
	x2, y2 = coords2
	measurement_here = measurements[y1][x1]
	measurements[y1][x1] = measurements[y2][x2]
	measurements[y2][x2] = measurement_here


def move_to_and_swap(x, y, direction):
	moving.to(x, y)
	swap(direction)

def swap_with_measurement(x, y, direction):
	global measurements

	if direction == West and measurements[y][x - 1] > measurements[y][x]:
		move_to_and_swap(x, y, West)
		swap_measurements((x, y), (x - 1, y))
		return True

	if direction == East and measurements[y][x + 1] < measurements[y][x]:
		move_to_and_swap(x, y, East)
		swap_measurements((x, y), (x + 1, y))
		return True

	if direction == South and measurements[y - 1][x] > measurements[y][x]:
		move_to_and_swap(x, y, South)
		swap_measurements((x, y), (x, y - 1))
		return True

	if direction == North and measurements[y + 1][x] < measurements[y][x]:
		move_to_and_swap(x, y, North)
		swap_measurements((x, y), (x, y + 1))
		return True


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
				if sort_field(x, y, size):
					hasSwapped = True

def farm():
	global measurements

	plant_square()
	quick_print(measurements)
	harvest()
	