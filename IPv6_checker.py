def IPv6_treatment(ipv6_to_convert):
	ipv6_to_convert = IPv6_validation(ipv6_to_convert)
	print(ipv6_to_convert)
	ipv6_to_convert = ''.join(str(byte) for byte in ipv6_to_convert)
	