logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text,shift_space):
    cipher_text=""
    for i in plain_text:
        if i in alphabet:
            new_position = alphabet.index(i)+shift_space
            if new_position>25:
                new_position = new_position-25
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=i
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_space):
    plain_text=""
    for i in cipher_text:
        if i in alphabet:
            new_position = alphabet.index(i)-shift_space
            if new_position<0:
                new_position = new_position+25
            plain_text+=alphabet[new_position]
        else:
            plain_text+=i
    print(f"The decoded text is {plain_text}")

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  if direction=="encode":
    encrypt(text,shift)
  else:
    decrypt(text,shift)  

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")