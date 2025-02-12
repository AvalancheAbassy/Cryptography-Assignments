import math
from math import gcd
# 3.4 - 1
##Find the square roots of 26055 mod the prime 34807.

def PowerModulo(a, z, n):
    """Computes the power of a number mod n using the formula:
        y = a^z mod n
        , Python3 has a power function that efficently computes modular exponentation using integers"""
    y = pow(a, z, n)
    return y
##To find
## (34807 + 1)/4 = 8702
print(PowerModulo(26055, 8702,  34807))

##
a= -33573 % 34807
print(a)


## 6.9 - 1
## We can RSA encrypt both of the messages 'one' and 'two' to see which one matches the received message
## Numberify then PowerModulo()

def Numberify(ciphertext): 
    """Converts plaintext letters to numbers by their alphabetical place"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Numbers=[]
    for i in ciphertext:
        letter = alphabet.find(i)
        Numbers.append(letter+1)
    return Numbers

print("plaintexts")
print(Numberify("one"))
print(Numberify("two"))
#one = 15, 14, 05 , two= 20, 23, 15, e = 6551, n = 712446816787, ciphertext to match: 273095689186
#we make 5, 05, to get fixed number length

print("ciphertexts")
print(PowerModulo(151405, 6551, 712446816787))
print(PowerModulo(202315, 6551, 712446816787))

##The message was 'one'

#6.9 - 8
#Since we know that 33335^2 == 670705093^2 (mod 670726081)
#We can use euclids lemma (p-n) to find the gcd between 33335 - 670705093 and 670726081 with gcd()

print("Factors")

print(gcd(33335 - 670705093, 670726081))

#we get 54323
factor=gcd(33335 - 670705093, 670726081)

print(670726081/factor)
#The factors are 54323 and 12347

# Suppose you know that 3^2 = 670726078^2 (mod 670726081). Why won't this information help you to factor 670726081?
# This is because -670726078 mod 670726081 == 3, the gcd below 3 will be 1 which is a given factor

print(gcd(3 - 670726078, 670726081))

#The result is 1