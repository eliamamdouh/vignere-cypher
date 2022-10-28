
from logging import exception
import re
import string

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
def encrypt(p, k):
    c = ""
    kpos = [] # return the index of characters ex: if k='d' then kpos= 3
    for x in k:
       # kpos += alphabets.find(x) #change the int value to string
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i] #find the number or index of the character and perform the shift with the key
      print(pos)
      if pos > 62:
          pos = pos-63               # check you exceed the limit
      c += alphabets[pos] 
      i +=1
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) - kpos[i]
      if pos < 0:
          pos = pos + 63
      p += alphabets[pos]
      i +=1
    return p
try:
    print("Welcome to vigenere cipher.\n\n"
          "The text message should contain CHARACTERS AND NUMBERS and the key should be one character word \n"
          "Press 1 to Enrypt a message \npress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       p = input("enter the plain text: ")
       k = input("enter the key:")
       if k.isalpha():
        c = encrypt(p,k)
        print("the cipher text is",c)
       else:
        print(k)
        print("enter valid key,key is only one character word")
       
    elif choose == '2':
        c = input("enter the cipher text: ")
        k = input("enter the key:")
        if not k.isalpha():
            print("enter valid key,key is only one word ")
        else:
            p = decrypt (c,k)
            print("the plain text is:",p)
    else:
        print("please enter a valid choise")
except exception as e:
    print(e)
    exit("enter a valid text please")