import moving

def plant_cactus():
    while get_water() < 0.5:
        use_item(Items.Water)

    if get_ground_type() != Grounds.Soil:
        till()

    plant(Entities.Cactus)

def plant_square(size = get_world_size()):
    for x in range(size):
        for y in range(size):
            moving.to(x, y)
            plant_cactus()
            sort_field_and_neighbours(x, y, size)

    sort_square(size)

def sort_field_and_neighbours(x, y, size = get_world_size()):
    hasSwapped = False
    if x > 0 and measure(West):
        if measure(West) > measure():
            swap(West)
            hasSwapped = True
    if x < size - 1 and measure(East):
        if measure(East) < measure():
            swap(East)
            hasSwapped = True
    if y > 0 and measure(South):
        if measure(South) > measure():
            swap(South)
            hasSwapped = True
    if y < size - 1 and measure(North):
        if measure(North) < measure():
            swap(North)
            hasSwapped = True

    return hasSwapped

def sort_square(size = get_world_size()):
    hasSwapped = True

    while hasSwapped:
        hasSwapped = False

        for x in range(size):
            for y in range(size):
                moving.to(x, y)
                result = sort_field_and_neighbours(x, y, size)
                if result:
                    hasSwapped = True

def farm():
    plant_square()
    harvest()
