# Regular expression IPv4: \d{1,3}[.]?\d{3}[.]?\d{1}[.]?\d{1}\\\d{1,2}

from itertools import product


class IPv6:
    def __init__(self, ipv6_to_convert):
        self.ipv6_to_convert = ipv6_to_convert
        self.aux_initial_bit = 0
        self.divide_ip()
        self.capture_subnet()
        self.capture_ip()
        self.validate_ip()
        self.convert_binary()
        self.get_final_bit()
        self.get_initial_bit()
        self.permutation()
        self.calculation()
        self.convert_hexadecimal()

    def print_data(self):
        print(self.ip_binary)
        print('-------------------------------------')
        print('\nThe subnets of {} in range /{} are: \n'.format(
            self.ipv6_to_convert, self.final_bit))
        for i in self.result:
            print('{}'.format(i))
        print('-------------------------------------\n')

    def divide_ip(self):
        self.divide_ip = []
        if('/' in self.ipv6_to_convert):
            self.divide_ip.append(
                self.ipv6_to_convert[:self.ipv6_to_convert.index('/')])
            self.divide_ip.append(
                self.ipv6_to_convert[self.ipv6_to_convert.index('/') + 1:])
        else:
            self.divide_ip = self.ipv6_to_convert

    def capture_subnet(self):
        if(type(self.divide_ip) is list):
            self.aux_initial_bit = int(self.divide_ip[1])

    def capture_ip(self):
        if(type(self.divide_ip) is list):
            self.ip_to_divide_not_validated = self.divide_ip[0]
        else:
            self.ip_to_divide_not_validated = self.divide_ip

    def validate_ip(self):
        if(len(self.ip_to_divide_not_validated) <= 39):
            self.ip_to_divide_not_validated = self.\
                ip_to_divide_not_validated.split(':')
        # zero group abbreviation
        if('' in self.ip_to_divide_not_validated):
            index = self.ip_to_divide_not_validated.index('')
            self.ip_to_divide_not_validated = list(
                filter(None, self.ip_to_divide_not_validated))
            size = len(self.ip_to_divide_not_validated)
            while(size < 8):
                self.ip_to_divide_not_validated.insert(index, '0000')
                index += 1
                size += 1
        # zero abbreviation
        index = 0
        for byte in self.ip_to_divide_not_validated:
            if(len(byte) < 4 and byte != ''):
                while(len(byte) < 4):
                    byte = '0' + byte[0:]
                self.ip_to_divide_not_validated[index] = byte
            index += 1
        self.ip_to_divide_validated = self.ip_to_divide_not_validated

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

        self.ip_binary = ''
        for j in result:
            for i in j:
                aux = ''
                aux = i[2:len(i) + 1]
                index = len(aux)
                while(index < 4):
                    aux = '0' + aux
                    index += 1
                self.ip_binary += aux

    def get_final_bit(self):
        range_to_convert = 0
        while(1 >= range_to_convert or range_to_convert >= 128):
            try:
                range_to_convert = int(
                    input('Type it the net range which you want to convert: '))
                if(self.aux_initial_bit > range_to_convert):
                    aux = range_to_convert
                    range_to_convert = self.aux_initial_bit
                    self.aux_initial_bit = aux
                self.final_bit = int(range_to_convert)
            except ValueError:
                print('Please, enter a valid net range, between 1 and 128.')

    def get_initial_bit(self):
        if(self.aux_initial_bit > self.final_bit):
            aux = self.final_bit
            self.final_bit = self.aux_initial_bit
            self.aux_initial_bit = aux
            self.initial_bit = self.aux_initial_bit
        else:
            self.initial_bit = self.aux_initial_bit

    def permutation(self):
        permutation_range = int(self.final_bit) - self.initial_bit
        permutation = product(range(2), repeat=permutation_range)
        self.permutation = list(permutation)

    def calculation(self):
        result = []
        final_result = []
        for i in self.permutation:
            index = 0
            counter = self.initial_bit
            list_ip_binary = list(self.ip_binary)
            # print(self.initial_bit-1)
            for j in list_ip_binary[self.initial_bit:self.final_bit]:
                aux = i[index]
                test = str(aux)
                list_ip_binary[counter] = test
                index += 1
                counter += 1
            result.append(list_ip_binary)
        index = 0
        while(index < len(result)):
            counter = self.final_bit + 1
            while(counter < 128):
                result[index][counter] = '0'
                counter += 1
            index += 1

        for group in result:
            aux = ''
            for i in group:
                aux += ''.join(str(x) for x in i)
            final_result.append(aux)
        self.ipv6_converted = final_result

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
        self.result = final_result
