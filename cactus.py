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
	moving.to(0, 0)

	for i in range(size):
		measurements.append([])

	for x in range(size):
		for y in range(size):
			moving.to(x, y)
			plant_cactus()
			measurements[y].append(measure())
			sort_field(x, y, True)

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

def check_and_perform_swap(x, y, direction):
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

	return False


def sort_field(x, y, is_sort_after_planting = False):
	global measurements

	swapped = False

	if x > 0:
		if check_and_perform_swap(x, y, West):
			swapped = True
	if x < measurements[y].len() - 1 and not is_sort_after_planting:
		if check_and_perform_swap(x, y, East):
			swapped = True
	if y < measurements.len() - 1 and not is_sort_after_planting:
		if check_and_perform_swap(x, y, North):
			swapped = True
	if y > 0:
		if check_and_perform_swap(x, y, South):
			swapped = True

	return swapped

def sort_square(size):
	hasSwapped = True

	while hasSwapped:
		hasSwapped = False

		for y in range(size):
			for x in range(size):
				if sort_field(x, y):
					hasSwapped = True

def farm():
	plant_square()

	# Other plants might not be done either, which leads to lower yield harvests
	# It seems to be only an issue if the size to farm is small and the speed of the
	# drone is high.
	# It also seems to not break the next iteration since the measurements will be
	# cached again in the planting cycle
	# Good enough for me right now
	harvested = False

	while not harvested:
		if can_harvest():
			harvest()
			harvested = True
