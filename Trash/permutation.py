from itertools import product

def Permutation(group_to_change):
	amount_to_change = 0 
	for i in group_to_change:
		index = 0
		while(index < len(group_to_change[i])):
			amount_to_change += 1
			index += 1

	combination = product(range(2), repeat=amount_to_change)

	return combination
