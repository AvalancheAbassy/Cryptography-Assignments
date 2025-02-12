import numpy as np
import math
from numpy import matrix
from numpy import linalg



#We will use numpy to create a matrix and the linear algebra functions to manipulate it and implement modular inverse matrices

M = np.array([[1, 2, 3, 4],[4, 3, 2, 1],[11, 2, 4, 6],[2, 9, 6, 4]])

ciphertext = 'zirkzwopjjoptfapuhfhadrq'

def Numberify(ciphertext): 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Numbers=[]
    for i in ciphertext:
        letter = alphabet.find(i)
        Numbers.append(letter)
    return Numbers

print(Numberify(ciphertext))#returns numberified ciphertext


def modInv(a,p):# Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

print (modInv(3, 26)) #should be 9, if so our modular inverse function is working properly

def minor(A,i,j):# Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def modMatInv(A,p):# Finds the inverse of matrix A mod p
  n=len(A)
  A=matrix(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

def hilldecrypt(M, ciphertext):# Inverses the cipher matrix and finds the dot product of the numberified ciphertext pairs to find the plaintext, then returns it
  M_inverse = modMatInv(M, 26)
  ciphernumbers = Numberify(ciphertext)
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  plaintext = ''
  for i in range(len(ciphernumbers)//4):
    pair = np.dot(ciphernumbers[i*4 :(i+1)*4], M_inverse)
    for element in pair:
      index = int(element)%26
      plaintext = plaintext + alphabet[index]
  return plaintext

#runs the function
print(hilldecrypt(M, ciphertext)) #returns "jackandjillwentupthehill"