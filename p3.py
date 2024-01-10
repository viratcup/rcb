def BinToDec(b):
 return int(b,2)
def OctToHex(o):
 return hex(int(o,8))
bnum = input("enter the binary number: ")
dnum = BinToDec(bnum)
print("\nEquivalent Decimal value = ",dnum)
onum = input("enter the octal number: ")
hnum = OctToHex(onum)
print("\nEquivalent Hexadecimal value = ",hnum[2:].upper())
