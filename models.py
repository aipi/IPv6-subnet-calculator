class IPv6:
	def __init__ (self, ipv6_to_convert):
		self.ipv6_to_convert = ipv6_to_convert
		self.divide_ip = self.divide_ip()
		self.subnet_to_divide = self.capture_subnet()
		self.ip_to_divide_not_validated = self.capture_ip()
		self.ip_to_divide_validated = self.validate_ip()
		self.ip_binary = self.convert_binary()

	def print_data(self):
		print(self.ip_binary)

	def divide_ip(self):	
		result = []
		range_of_subnets = ''
		if('/' in self.ipv6_to_convert):
			result.append(self.ipv6_to_convert[:self.ipv6_to_convert.index('/')]) 
			result.append(self.ipv6_to_convert[self.ipv6_to_convert.index('/')+1:]) 
		else:
			result = self.ipv6_to_convert
		return result
	
	def capture_subnet(self):	
		if(type(self.divide_ip) is list):
			return self.divide_ip[1]

	def capture_ip(self):
		if(type(self.divide_ip) is list):
			return self.divide_ip[0]
		else:
			return self.divide_ip

	def validate_ip(self):
		if(len(self.ip_to_divide_not_validated) < 39):
			self.ip_to_divide_not_validated = self.ip_to_divide_not_validated.split(':')

		#abreviação grupo de zero
		if('' in self.ip_to_divide_not_validated):
			index = self.ip_to_divide_not_validated.index('')
			self.ip_to_divide_not_validated = list(filter(None, self.ip_to_divide_not_validated))
			size = len(self.ip_to_divide_not_validated)
			while(size < 8):
				self.ip_to_divide_not_validated.insert(index, '0000')
				index += 1
				size += 1 
			
		#abreviação de zero
		index = 0
		for byte in self.ip_to_divide_not_validated:
			if(len(byte) < 4 and byte != ''):
				while(len(byte) < 4):
					byte = '0' + byte[0:]
				self.ip_to_divide_not_validated[index] = byte
			index += 1
		return self.ip_to_divide_not_validated

	def convert_binary(self):
		string = ''
		for i in self.ip_to_divide_validated:
			string += i
		index = 0
		result = ''
		while(index < len(string)):
			result += bin(int(string[index], 16))
			index += 1
		return result
		


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