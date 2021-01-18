import hashlib
import binascii
from string import ascii_lowercase
from itertools import combinations_with_replacement
import itertools
from itertools import chain, product
import multiprocessing as mp
import threading
import queue
import sys
import os
import glob
import timeit





#input = open('input.txt', 'r').read().split('\n')




## no need to run once all passwords have been saved to textfile. We saved into 301 textfiles with appox 1m words in each.
# def words():
#     f= open("Output.txt", "w")
#
#     for _set in product(list('abcdefghijklmnopqrstuvwxyz'), repeat=6):
#         word = ''.join(_set)
#         f.writelines(word+"\n")
#
#         print(word)
#
#     f.close()




def testpassword(textfile, drname):
        os.chdir('C:/Users/User/Desktop/cs165/' +drname)
        f=open(textfile)
        start=timeit.default_timer()
        for password in f:
            hash = 'wT1hIrT6VdrB80a/e8BeH0'
            password=password.strip()
            if hash == intialize(password):
                print(hash)
                print('password ' + password + ' matches')
                end=timeit.default_timer()
                print('this took  ', end-start )
                sys.exit()



def to64(v,n):
    base64=  "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ret=""

    for i in range(0,n):
        ret+= base64[v&0x3f]
        v>>=6
    return ret


def intialize(password):
    print(password)
    password_encode = password.encode()
    salt = '4fTgjp6q'
    salt_encode = salt.encode()
    res = password + "$1$" + salt
    h = password + salt + password

    test = b'\x3f\xfc\x86\xe7\xc7\x8f\x47\xa8\x16\x4f\xe2\x85\xc0\xfa\x22\x55'
    res=res.encode()
    h = hashlib.md5(h.encode()).digest()
   # print(h)

    l = len(password)
    lenght = len(password)
    while l > 0:
        res = res + h[0:min(16, l)]
        l = l - 16

    while lenght != 0:
        if lenght & 1:
            res += b'\x00'
        else:
            res += password[0].encode()
        lenght>>=1
    h=hashlib.md5(res)
    h_encoded= hashlib.md5(res).digest()

    for i in range(0,1000):
        tmp = b''
        if i %2==1:
            tmp += password_encode
        else: tmp += h_encoded

        if i % 3 !=0: tmp += salt_encode

        if i % 7 !=0: tmp += password_encode

        if i % 2==1:
            tmp += h_encoded
        else:
            tmp += password_encode

        h_encoded = hashlib.md5(tmp).digest()
   # print(h_encoded.hex())

    hex = b'\xff\x20\x2f\x2e\x9b\x6a\xc6\xe4\x95\x57\x55\x36\xfc\x89\xfd\x2a'
   # print(hex.hex())


    h_encodedfinal= (to64((h_encoded[0] << 16) | (h_encoded[6] << 8) | (h_encoded[12]), 4) +\
    to64((h_encoded[1] << 16) | (h_encoded[7] << 8) | (h_encoded[13]), 4) +\
    to64((h_encoded[2] << 16) | (h_encoded[8] << 8) | (h_encoded[14]), 4) +\
    to64((h_encoded[3] << 16) | (h_encoded[9] << 8) | (h_encoded[15]), 4) +\
    to64((h_encoded[4] << 16) | (h_encoded[10] << 8) | (h_encoded[5]), 4) +\
    to64(h_encoded[11], 2))

   # print(h_encodedfinal)

    return h_encodedfinal



def listfile(drname ):
    for textfile in os.listdir("C:/Users/User/Desktop/cs165" +"/" +drname):
        testpassword(textfile,drname)
        os.remove("C:/Users/User/Desktop/cs165" +"/"+drname +"/"+textfile)



#
if __name__ == "__main__":
    process1=mp.Process(target=listfile, args=("passwords",))
    process2=mp.Process(target=listfile,args=("passwords2",))
    process3 = mp.Process(target=listfile, args=("passwords3",))
    process4 = mp.Process(target=listfile, args=("passwords4",))
    process5 = mp.Process(target=listfile, args=("passwords5",))
    process6 = mp.Process(target=listfile, args=("passwords6",))
#process2=mp.Process(target=listfile, args="textfile")

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()








