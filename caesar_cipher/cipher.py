import re
from caesar_cipher.name_words_loader import words_list, names_list

def encrypt(plain,key):
  encrypted_string =''

  for char in plain:
    print(char)
    new_char = char
   
    if new_char.isalpha(): #The isalpha() method returns True if all the characters are alphabet letters (a-z).
     
      if char.isupper():#The isupper() method returns True if all the characters are in upper case, otherwise False.
        
        new_char = chr((ord(char)+ key- 65) % 26 + 65) #The ord() function returns an integer representing the Unicode character.
      else:
        new_char = chr ((ord(char)+ key- 97) % 26 + 97)
        
    encrypted_string += new_char

  return encrypted_string