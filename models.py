from itertools import product
import binascii

class IPv6:
	def __init__ (self, ipv6_to_convert):
		self.ipv6_to_convert = ipv6_to_convert
		self.divide_ip = self.divide_ip()
		self.aux_initial_bit = self.capture_subnet()
		self.ip_to_divide_not_validated = self.capture_ip()
		self.ip_to_divide_validated = self.validate_ip()
		self.ip_binary = self.convert_binary()
		self.final_bit = self.get_final_bit()
		self.initial_bit = self.get_initial_bit()
		self.permutation = self.permutation()
		self.ipv6_converted = self.calculation()
		self.result = self.convert_hexadecimal()

	def print_data(self):
		print('-------------------------------------')
		print('\nThe subnets of {} in range /{} are: \n'.format(self.ipv6_to_convert, self.final_bit))
		for i in self.result:
			print('{}'.format(i))
		print('\n-------------------------------------\n')

	def divide_ip(self):	
		result = []
		range_of_subnets = ''
		if('/' in self.ipv6_to_convert):
			result.append(self.ipv6_to_convert[:self.ipv6_to_convert.index('/')]) 
			result.append(self.ipv6_to_convert[self.ipv6_to_convert.index('/')+1:]) 
		else:
			result = self.ipv6_to_convert
		print(result)
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
		if(len(self.ip_to_divide_not_validated) <= 39):
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
		#print(self.ip_to_divide_not_validated)
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

	def get_final_bit(self):
		range_to_convert = 0
		while(1 >= range_to_convert or range_to_convert >= 128 ):
			try:
				range_to_convert = int(input('Type it the net range which you want to convert: '))
				if(self.aux_initial_bit > range_to_convert):
					aux = range_to_convert
					range_to_convert = self.aux_initial_bit
					self.aux_initial_bit = aux
				return int(range_to_convert)
			except ValueError:
				print('Please, enter a valid net range, between 1 and 128.')

	def get_initial_bit(self):
		if(self.aux_initial_bit > self.final_bit):
			aux = self.final_bit
			self.final_bit = self.aux_initial_bit
			self.aux_initial_bit = aux
			return self.aux_initial_bit
		else: 
			return self.aux_initial_bit

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
		
		index = 0 
		while(index < len(result)):
			counter = self.final_bit+1
			while(counter < 128):
				result[index][counter] = '0'
				counter += 1
			index += 1
		
		for group in result:
			aux = ''
			for i in group:
				aux += ''.join(str(x) for x in i)
			final_result.append(aux)

		return final_result

	def convert_hexadecimal(self):
		final_result = []
		for i in self.ipv6_converted:
			hexadecimal = '%0*X' % (len(i) // 4, int(i, 2))
			index = 0
			hex_list = []
			aux = ''
			for j in hexadecimal:
				aux += j
				index += 1
				if(index % 4 == 0 and index != 0):
					hex_list.append(aux)
					aux = ''
				
			result = ':'.join(hex_list)
			final_result.append(result)
		return final_result
