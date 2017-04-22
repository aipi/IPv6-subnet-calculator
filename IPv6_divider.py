#Function to divide the IP and address range
def IPv6_divider(ipv6_to_convert):
	result = []
	range_of_subnets = ''
	if('/' in ipv6_to_convert):
		result.append(ipv6_to_convert[:ipv6_to_convert.index('/')]) 
		result.append(ipv6_to_convert[ipv6_to_convert.index('/')+1:]) 
	else:
		result = ipv6_to_convert
	return result