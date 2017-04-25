def Calculator(net, initial_range):
	range_to_convert = 0
	while(1 >= range_to_convert or range_to_convert >= 128 ):
		try:
			range_to_convert = int(input('Type it the net range which you want to convert: '))
		except ValueError:
			print('Please, enter a valid net range, between 1 and 128.')

	#This counter is one because make more sense start from one, since IP number start from there 
	bit_counter, final_bit, initial_bit, group, position, bit_group_counter = 0, 0, 0, 0, 0, 0

	#converter end to begin
	if(initial_range > range_to_convert):
		aux = range_to_convert
		range_to_convert = initial_range
		initial_range = aux
	
	while(bit_group_counter <= 32):	
		position_counter = 0
		
		while(position_counter < 4):
				if(bit_counter < range_to_convert):
					position_counter += 1
					bit_counter += 1
							
					if(bit_counter == initial_range):
						initial_bit = bit_counter + 1
				
				else:
					final_bit = bit_counter
					position = position_counter
					group = bit_group_counter
					break			
		
		#end while

		if(final_bit == range_to_convert):
			break

		bit_group_counter += 1
	#end while	
		

	print('The value to be changed are from the bit {} until bit {}\n'.format(initial_bit, final_bit))
	#print('This belongs to the group  and the group {} in the position {}'.format(group, position))

# 2001:0DB8::140B/33
# 2001:0DB8:0000:0000:130F:0000:0000:140B/33 -> /32
#    REDE <-|-> HOST	
#           |
#	        33 34 35 36
#		    -----------
#           0  0  0  0
#           -  -  -  -
#		    8  4  2  1

# 2001:0DB8::140B
