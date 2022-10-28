
from logging import exception

alphabets = "abcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" #characters used
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
      if pos > 66:
          pos = pos-67 # check you exceed the limit
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
          pos = pos + 67
      p += alphabets[pos]
      i +=1
    return p
try:
    print("Welcome to vigenere cipher.\n\n"
          "The text message should contain letter and numbers and special characters and the key should be one character word \n"
          " Press 1 to Enrypt a message \n press 2 to Decrypt a message\n press 3 to encrypt through a file \n press 4 to decrypt through a file")
    choose = input("Choice: ")
    if choose == '1':
       p = input("enter the plain text: ")
       p = p.replace(" ", "") #remouve the white spaces between the words if any
       k = input("enter the key:")
       if k.isalpha():
        c = encrypt(p,k)
        print("the cipher text is",c)
       else:
        print(k)
        print("enter valid key,key is only one character word")
       
    elif choose == '2':
        c = input("enter the cipher text: ")
        c = c.replace(" ","")
        k = input("enter the key:")
        if not k.isalpha():#isaplha check if the input is only letters
            print("enter valid key,key is only one word ")
        else:
            p = decrypt (c,k)
            print("the plain text is:",p)

    elif choose == "3":
       f = input("enter the file name:")# open the file using open() function
       f = f.replace(" ", "")
       o = input("enter the plain text: ")
       o = o.replace(" ", "")
       k = input("enter the key:")
       file = open(f,"w")# Overwrite the file
       file.write(encrypt(o,k))
       if k.isalpha():
        c = encrypt(o,k)
        print("the cipher text is",c)
       else:
        print(k)
        print("enter valid key,key is only one character word")
    elif choose == "4":
         f = input("enter the file name:")# open the file using open() function
         f = f.replace(" ", "")
         c = input("enter the encrypted text: ")
         c = c.replace(" ", "")
         k = input("enter the key:")
         file = open(f,"w")# Overwrite the file
         file.write(decrypt(c,k))
         if not k.isalpha():#isaplha check if the input is only letters
            print("enter valid key,key is only one word ")
         else:
            p = decrypt (c,k)
            print("the plain text is:",p)
    else:
        print("please enter a valid choice")
except exception as e:
    print(e)
    exit("enter a valid text please")

    