# IPv6 subnets discovery

First of all, the program will unabbreviated the net address follow the ideas of IPv6 abbreviation:

- Use the two-colon (::) notation to represent contiguous 16-bit fields of zeros.
- Fields of zeros can be represented as a single 0.
- Omit any leading zeros in a field, such as changing 0db8 to db8.

Input example: ```2001:DB8::140B/33```. To find out the subnets of the range /32.

It will be divided into two parts, IPv6 number and the IPv6 range. After that, it will be validated and converted to binary matrix which is saparated in groups of 2 bytes to facility the calculator.


    2001:0DB8:0000:0000:130F:0000:0000:140B/33 to /32
        NET <-|-> HOST
              |
            | 33 | 34 35 36
            |----|---------
            | 0  | 0  0  0
            | -  | -  -  -
            | 8  | 4  2  1


On the example above, the division o will generate two new subnets range because just the bit ```33``` will be changed:

```2001:0DB8:0000:0000:130F:0000:0000:140B/32``` and ```2001:0DB8:8000:0000:130F:0000:0000:140B/33```
