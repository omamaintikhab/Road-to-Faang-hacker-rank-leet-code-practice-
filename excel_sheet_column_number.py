'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
a b c d e f g h i j  k   l  m  n  o  p  q  r  s  t  u  v  w  x  y  z aa ab ac

note:
* moving from right to left 26 power will increase for example
- zy
    26*26 +25= 701
    
- aac
(26^2 *1)+(26^1 * 1)+ (26^0 * c)
676+26+3= 705
c= 3
a=26^1
b = 26^26 
'''
from turtle import position


columnTitle= 'ZY'
column_number = 0
power_of_26 = 0
length_of_string = len(columnTitle) - 1
while length_of_string >= 0:
    asci_value_of_char = ord(columnTitle[length_of_string])
    #65 is the asci value of A
    position_in_alphabet =  asci_value_of_char - 65 + 1
    column_number += pow(26,power_of_26) * position_in_alphabet
    power_of_26 +=1
    length_of_string -=1
print(column_number)

