#Few Operations on operators to get some idea on them
print(10&4+3)
print(7+2&4+3&9)
print(10^3&4)
#print(10&4~2)-->SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(6|3&9+6)
#print(2~4^3*2)-->SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(~9+4&6)
print(~6)#-->~num=-(num+1) So, result is -7 check reason in book
print(7>>1)
print(7<<1)
print(5^5^5)#-->Number XOR itself by odd times gives number itself
print(5^5)#-->Number XOR itself by even times gives 0
print(1^2^3)#-->Even 1's will give 0 i.e., XOR all 3 at a time
print(4^6^5)#-->Odd 1's will give 1 i.e., XOR all 3 at a time
print(4^5)
#a>>b ==> a/(2^b)
print(5>>1)#5/2^1
print(5>>2)#5/2^2
print(5>>3)#5/2^3
print(14>>4)#14/2^4
print(6>>3)#6/2^3
#a<<b ==> a*(2^b)
print(5<<2)#5*2^2
print(10<<3)#10*2^3
print(9<<4)#9*2^4
print(2**31)