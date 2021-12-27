#0b to represent a binary number
a = 0b10
print("Binary A:",bin(a))
print("Decimal A:",a)

# "~" represents the binary negation, bitwise negation
print("decimal negation:",~a)
print("Bitwise negation:",bin(~a))

#Two binary numbers to be compared 
a = 0b1001
b = 0b1100

#Operator "|" represents bitwise OR
c = a | b
print("A OR B:",bin(c))

#Operator "^" represents bitwise XOR, XOR only when one value is 1, the result is 1. 1 XOR 1 = 0 and 0 XOR 0 = 0.
d = a ^ b
print("A XOR B:",bin(d))

#Operator "&" represents bitwise AND
e = a & b
print("A AND B:",bin(e))

#Add or remove "0" left or right
print("A AND B:",bin(e >> 4))
print("A AND B:",bin(e << 4))

print("a">"b")
print(ord("a"))
print(ord("b"))
print(id("a"))

print("This" and 0)
print("This" and "This")
print("This" or 0)
print("That" or "This")
print("David" or "Pamela")
print(1 or 0)
print(0 or 1)
print(not 2 or 3)
print(not "")