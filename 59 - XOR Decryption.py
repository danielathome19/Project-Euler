from csv import *

def decrypt(cipher, key):
    decrypted = ""
    l = len(cipher)
    for i in range(l):
        decrypted += chr(int(cipher[i])^key[i%len(key)]) 
    return decrypted

def main():
    with open("cipher.txt", "rt") as inputfile:
        myreader = reader(inputfile, delimiter=',')
        filelist = list(myreader)     
    cipherlist = filelist[0]          

    for a in range(ord('a'), ord('z')+1):
        for b in range(ord('a'), ord('z')+1):
            for c in range(ord('a'), ord('z')+1):
                password = [a, b, c]     
                message = decrypt(cipherlist, password)
                if "the" in message and "be" in message and "to" in message and "of" in message and "and" in message:
                    print(message)
                    charsum = 0
                    for char in message:
                        charsum += ord(char)
                    print(charsum)

    print("done.")  # result: 107359

if __name__ == '__main__':
    main()
raw_input('Press Enter to exit')