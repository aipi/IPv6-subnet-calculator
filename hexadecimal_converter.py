def Hex_converter(ipv6_to_convert):
	result = []
	for byte in ipv6_to_convert:
		result.append(list(byte))
	line = 0
	row = 0
	while(line < 8):
		while(row < 4):
			result[line][row] = int(result[line][row], 16)
			row += 1
		row = 0	
		line += 1
	print(result)
	return ipv6_to_convert
	#ipv6_to_convert = ''.join(str(byte) for byte in ipv6_to_convert)
	