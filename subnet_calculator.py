def Calculator(net, range):
	range_to_convert = 0
	while(1 >= range_to_convert or range_to_convert >= 128 ):
		try:
			range_to_convert = int(input('Type it the net range which you want to convert: '))
		except ValueError:
			print('Please, enter a valid net range, between 1 and 128.')
	
	i, bit_total, group, bit_group, bit = 1, 0, 0, 0, 0
	while(i <= 32):
		j = 0
		while(j < 4):
			if(bit != range_to_convert):
				j += 1
				bit += 1
			else:
				bit_total = bit 
				bit_group = j
				group = i
				break
		if(bit_total == range_to_convert):
			break
		i += 1

	print('The calue to be changed is int the bit {}, in the group {} and in the position {}'.format(bit_total + 1, group, bit_group))

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
