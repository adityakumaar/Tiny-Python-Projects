import string

alphabets = "abcdefghijklmnopqrstuvwxyz"
#The sentence is required to be in lower case and without spaces
sentence = input("Enter the string to encrypt (lowercase): ")

#The shift value can be either negative or positive
val = int(input("Enter Shift Value: "))

def startEncryption(string, shift_val = val):
    encrypted_string = ""
    for i in string:
        index = alphabets.index(i)
        shifted_index = (index + shift_val) % len(alphabets)
        encrypted_string += alphabets[shifted_index]
    return encrypted_string

print(startEncryption(sentence))


