from models import *

ipv6_to_convert = input('Enter the IP that you would like to convert: ')

ipv6 = IPv6(ipv6_to_convert)

ipv6.print_data()


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