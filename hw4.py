"""Requires SYMPY library for factorint() method"""
import sympy
from sympy import factorint 


def modInv(a,p):
  """Finds the inverse of a mod p, if it exists"""
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

##We use a modular exponent function to compute the last five digits of 3^1234567, we can do this by calculating it mod 100000, the number place of the exponent
def PowerModulo(a, z, n):
    """Computes the power of a number mod n using the formula:
        y = a^z mod n
        , Python3 has a power function that efficently computes modular exponentation using integers"""
    y = pow(a, z, n)
    return y

def ChineseRemainder(div, rem, k):
    """Demonstrates the chinese remainder theorm with inverse modulo by finding the minimum divisor using number set 'div' remainders 'rem' of size 'k' 
    assuming the numbers in set n are coprime"""
    prod = 1
    for i in range(0, k) :  
        prod = prod * div[i]  
  
    # Initialize result  
    result = 0
  
    # Apply above formula  
    for i in range(0,k):  
        pp = prod // div[i]  
        result = result + rem[i] * modInv(pp, div[i]) * pp  
      
      
    return result % prod  

def FactorInteger(n):
    """Finds the factors of an integer using the sympy factorint() method"""
    x=factorint(n)
    return x  




#########Drivers##########

#3
print(PowerModulo(3, 1234567, 100000))
#returns 40587

r=[17,18,19]
n=[101, 201, 301]
k=len(n)

#6
print("CRT result is: ", ChineseRemainder(n, r, k))
#Returns 61122


#9 
#Factorize P-1 then raise 3 (The primitive root of 65537) to P-1/2 power with P=65537
print("Factors of P-1 with P=65537 are:",FactorInteger(65537 - 1))
#returns 2, 16, 2 is the only prime factor of p-1
#Raise primitive root 3 by (65537 - 1)/(2)
print("Using the primitive root p-1 method, we check to see the result of raising 3 by P-1/2: ", pow(3, 32768, 65537))
#Returns 65536
#Because this is not equal to 1, we now know that 3 is a primitive root of 65537