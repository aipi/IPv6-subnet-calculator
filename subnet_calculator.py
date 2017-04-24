def Calculator(net, range):
	range_to_convert = 0
	while(1 >= range_to_convert or range_to_convert >= 128 ):
		try:
			range_to_convert = int(input('Type it the net range which you want to convert: '))
		except ValueError:
			print('Please, enter a valid net range, between 1 and 128.')
	print(net)




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
