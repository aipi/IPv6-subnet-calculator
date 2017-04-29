# IPv6 subnets discovery

First of all, the program will unabbreviated the net address follow the ideas of IPv6 abbreviation:

- Use the two-colon (```::```) notation to represent contiguous 16-bit fields of zeros.
- Fields of zeros can be represented as a single ```0```.
- Omit any leading zeros in a field, such as changing ```0db8``` to ```db8```.

Input example: ```2001:DB8::140B/33```. To find out the subnets of the range ```/32.```

It will be divided into two parts, IPv6 number and the IPv6 range. After that, it will be validated and converted to binary which is separate to execute the calculator logic.


     2001:0DB8:D000:0000:0000:0000:0000:140B/34 to /36
                NET <-|-> HOST
                      |
            31  33 34 | 35 36 | 37  38
            ----------|-------|-------
             0  0  0  | 0  0  |  0   0
             -  -  -  | -  -  |  -   -
             1  8  4  | 2  1  |  8   4


On the example above, the division o will generate four new subnets range because just the bit ```35``` until bit ```36``` will be variated, this is 2^n bits, where "n" is the number of variations :

    2001:0DB8:C000:0000:0000:0000:0000:0000
    2001:0DB8:D000:0000:0000:0000:0000:0000
    2001:0DB8:E000:0000:0000:0000:0000:0000
    2001:0DB8:F000:0000:0000:0000:0000:0000

![alt text](https://raw.githubusercontent.com/aipi/IPv6/master/Images/Captura%20de%20Tela%202017-04-29%20%C3%A0s%2001.41.50.png)

