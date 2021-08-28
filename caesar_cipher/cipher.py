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
 
def decrypt(ciper_text,key):
  return encrypt(ciper_text,-key)


def crack(text):
  max=50
  be_able = ''
  
  for shift in range(0,26):
    encrypted_words =decrypt(text,shift)
    split_word_list =encrypted_words.split() 
  
    count = 0 
    
    for word in split_word_list:
      clean_word = re.sub(r"[^a-zA-Z]+", "", word).lower()
    
      if (clean_word in words_list) or (clean_word in names_list): 
        count += 1
    percent=int(count / len(split_word_list) * 100)
    
    if percent > max:
      max=percent
      be_able=encrypted_words
  return be_able 