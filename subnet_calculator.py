def Calculator(net, initial_range):
	range_to_convert = 0
	while(1 >= range_to_convert or range_to_convert >= 128 ):
		try:
			range_to_convert = int(input('Type it the net range which you want to convert: '))
		except ValueError:
			print('Please, enter a valid net range, between 1 and 128.')

	#This counter is one because make more sense start from one, since IP number start from there 
	bit_counter, final_bit, initial_bit, hex_position, position, hex_position_counter = 0, 0, 0, 0, 0, 0

	#converter end to begin
	if(initial_range > range_to_convert):
		aux = range_to_convert
		range_to_convert = initial_range
		initial_range = aux
	
	while(hex_position_counter <= 32):	
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
					hex_position = hex_position_counter
					break			
		#end while

		if(final_bit == range_to_convert):
			break

		hex_position_counter += 1
	#end while	

	bit_counter, hex_group_counter, hex_position_counter = 1, 0, 1
	list_values = []
	for hex_group in net:
		for value in hex_group:
			index = 0
			
			while(index < 4):
				if(bit_counter == initial_bit):
					initial_hex_group = hex_group_counter
					hex_position_initial = hex_position_counter 
				
				if(bit_counter == final_bit):
					final_hex_group = hex_group_counter
					hex_position_final = hex_position_counter 
				
				if(bit_counter >= initial_bit and bit_counter <= final_bit):
					list_values.append(index)


				bit_counter += 1
				index+=1
			#end while

			hex_position_counter += 1
			
		
		hex_group_counter += 1
		#end for
	#end for

	print('The value to be changed are from the bit {} until bit {}'.format(initial_bit, final_bit))
	print('This value are between hexadecimal group {} and  {}'.format(initial_hex_group, final_hex_group))
	print('The values to be change are {}'.format(list_values))
	print('The position is between {} and {}'.format(hex_position_initial, hex_position_final))

	i = 0 
	while(i < 8):
		print(net[i])
		j = 0
		
		while(j < 4):
			print(net[i][j])
			j += 1
		#end while

		i += 1
	#end while	


# 2001:0DB8::140B/34
# 2001:0DB8:0000:0000:130F:0000:0000:140B/33 -> /32
#    REDE <-|-> HOST	
#           |
#	        33 34 35 36
#		    -----------
#           0  0  0  0
#           -  -  -  -
#		    8  4  2  1

# 2001:0DB8::140B
