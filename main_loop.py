import limits
import hay
import wood
import carrot
import pumpkin

clear()

while True:
	while num_items(Items.Hay) < limits.min_hay:
		hay.farm()

	limits.min_hay += limits.increment_hay
	clear()

	while num_items(Items.Wood) < limits.min_wood:
		wood.farm()

	limits.min_wood += limits.increment_wood
	clear()

	while num_items(Items.Carrot) < limits.min_carrot:
		carrot.farm()

	limits.min_carrot += limits.increment_carrot
	clear()

	while num_items(Items.Pumpkin) < limits.min_pumpkin:
		pumpkin.farm()

	limits.min_pumpkin += limits.increment_pumpkin
	clear()