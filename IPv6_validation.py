def IPv6_validation(ipv6_to_convert):
	if(len(ipv6_to_convert) < 39):
		ipv6_to_convert = ipv6_to_convert.split(':')

		#abreviação grupo de zero
		if('' in ipv6_to_convert):
			index = ipv6_to_convert.index('')
			ipv6_to_convert = list(filter(None, ipv6_to_convert))
			size = len(ipv6_to_convert)
			while(size < 8):
				ipv6_to_convert.insert(index, '0000')
				index += 1
				size += 1 
			
		#abreviação de zero
		index = 0
		for byte in ipv6_to_convert:
			if(len(byte) < 4 and byte != ''):
				while(len(byte) < 4):
					byte = '0' + byte[0:]
				ipv6_to_convert[index] = byte
			index += 1
		return ipv6_to_convert

	# 2001:DB8:0:0:130F:140B:11:22 ok

	# 2001:0DB8:0000:0000:130F:0000:0000:140B
		
	# 2001:DB8:0:0:130F::140B 
	
	# 2001:0DB8:0000:0000:130F:0000:0000:140B

	# 2001:DB8::130F:0:0:140B