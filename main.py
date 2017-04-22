#IPv6 subnets finder
from IPv6_divider import IPv6_divider
from IPv6_checker import *
from IPv6_validation import *

if __name__ == '__main__': 

	ipv6_to_convert = input()

	divider_result = IPv6_divider(ipv6_to_convert)
	if(type(divider_result) is list):
		ipv6_to_convert = divider_result[0]
		range_of_subnets = divider_result[1]
		print(divider_result)		
	else:
		ipv6_to_convert = divider_result
		print(divider_result)
	
	IPv6_validation(ipv6_to_convert)

	#ipv6_to_convert = IPv6_validation(ipv6_to_convert)
	#2001:db8:1000/42