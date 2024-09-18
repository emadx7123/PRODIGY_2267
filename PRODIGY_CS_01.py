# Task-01 Create a python program that can encrypt and decrypt text using the caesar cipher algorithm

def main():
    print("------------------------------------------------")
    print("------------CAESAR CIPHER ALGORITHM------------")
    print("------------------------------------------------")
    print("DO YOU WANT TO ENCRYPT(e) OR DECRYPT(d)")
    a = input("SELECT ANY ONE OPTION(e/d)")

    if a=="e":
        original = input("Enter the plain text ")
        new =encrypted(original,3)
        print(f"Your Encrypted text wil be: {new}")
    elif a=="d":
        original = input("Enter the encrypted text ")
        new =decrypted(original,3)
        print( print(f"Your Decrypted text wil be: {new}"))
    else:
        print("Try again!")

def encrypted(text,key):
   enc_text =""
   for char in text:
      if char.islower():
        enc_text+= chr((ord(char)+key-97)%26+97) 
      else:
        enc_text +=  char
   return enc_text


def decrypted(enc_text,key):
   dec_text =""
   for char in enc_text:
      if char.islower():
        dec_text+= chr((ord(char)-key-97)%26+97) 
      else:
        dec_text +=  char
   return dec_text

main()