# This program can convert a word to an encrypted string and can also decode the same string.
# It take the last letter of the word and attaches it to the start of the word.
# Then it add random 3 letters on the start and end of the word making it encrypted.
# when decoding the same, it reverses the process and prints the decrypted word.

import random
import string

def codingString():
    v = ''.join(random.sample(string.ascii_letters, 3))
    x = ''.join(random.sample(string.ascii_letters, 3))
    code = input("Enter the string you want to code: ")
    print(f"{v}{code[-1] + code[:-1]}{x}")

def decodingString():
    decode = input("Enter the string you want to decode?")
    start = 3
    end = -3
    c = decode[start:end]
    print(f"The decode string is: {c[1:] + c[0]}")

user_input = input("Do you want to code or decode?")

if(user_input == 'decode' or user_input == 'Decode' or user_input == 'DECODE'):
    decodingString();
elif(user_input == 'code' or user_input == 'Code' or user_input == 'CODE'):
    codingString();
else:
    print("please enter the following field with attention to the prompt!")
