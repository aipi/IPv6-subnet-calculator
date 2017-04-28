from itertools import product

class IPv6:
	def __init__ (self, ipv6_to_convert):
		self.ipv6_to_convert = ipv6_to_convert
		self.divide_ip = self.divide_ip()
		self.initial_bit = self.capture_subnet()
		self.ip_to_divide_not_validated = self.capture_ip()
		self.ip_to_divide_validated = self.validate_ip()
		self.ip_binary = self.convert_binary()
		self.final_bit = self.range_to_convert()
		self.permutation = self.permutation()
		self.result = self.calculation()

	def print_data(self):
		print(len(self.ip_binary))

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
			return int(self.divide_ip[1])

	def capture_ip(self):
		if(type(self.divide_ip) is list):
			return self.divide_ip[0]
		else:
			return self.divide_ip

	def validate_ip(self):
		if(len(self.ip_to_divide_not_validated) < 39):
			self.ip_to_divide_not_validated = self.ip_to_divide_not_validated.split(':')

		#zero group abbreviation
		if('' in self.ip_to_divide_not_validated):
			index = self.ip_to_divide_not_validated.index('')
			self.ip_to_divide_not_validated = list(filter(None, self.ip_to_divide_not_validated))
			size = len(self.ip_to_divide_not_validated)
			while(size < 8):
				self.ip_to_divide_not_validated.insert(index, '0000')
				index += 1
				size += 1 
			
		#zero abbreviation
		index = 0
		for byte in self.ip_to_divide_not_validated:
			if(len(byte) < 4 and byte != ''):
				while(len(byte) < 4):
					byte = '0' + byte[0:]
				self.ip_to_divide_not_validated[index] = byte
			index += 1
		return self.ip_to_divide_not_validated

	def convert_binary(self):
		result = []
		for byte in self.ip_to_divide_validated:
			result.append(list(byte))
		line = 0
		row = 0
		while(line < 8):
			while(row < 4):
				result[line][row] = bin(int(result[line][row], 16))
				row += 1
			row = 0	
			line += 1

		binary = ''
		for j in result:
			for i in j:
				aux = ''
				aux = i[2:len(i)+1]
				index = len(aux)
				while(index < 4):
					aux = '0' + aux 
					index += 1
				binary += aux
		return binary

	def range_to_convert(self):
		range_to_convert = 0
		while(1 >= range_to_convert or range_to_convert >= 128 ):
			try:
				range_to_convert = int(input('Type it the net range which you want to convert: '))
				return int(range_to_convert)
			except ValueError:
				print('Please, enter a valid net range, between 1 and 128.')

	def permutation(self):
		permutation_range = int(self.final_bit) - self.initial_bit
		permutation = product(range(2), repeat=permutation_range)
		return list(permutation)

	def calculation(self):
		result = []
		final_result = []
		for i in self.permutation:
			index = 0
			counter = self.initial_bit+1
			list_ip_binary = list(self.ip_binary)
			for j in list_ip_binary[self.initial_bit+1:self.final_bit+1]:
				aux = i[index]
				teste = str(aux)
				list_ip_binary[counter] = teste
				index += 1 
				counter += 1
			result.append(list_ip_binary)
		
		for group in result:
			aux = ''
			for i in group:
				aux += ''.join(str(x) for x in i)
			final_result.append(aux)

		print(final_result)

# 2001:0DB8:D000:000B::/34
# 2001:0DB8:0000:0000:130F:0000:0000:140B/33 -> /32
#    REDE <-|-> HOST	
#           |
#	        33 34 35 36
#		    -----------
#           0  0  0  0
#           -  -  -  -
#		    8  4  2  1

# 2001:0DB8::140B