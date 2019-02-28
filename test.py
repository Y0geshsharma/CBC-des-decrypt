import decrypt
import binascii as bin
ct=[]
m = input('Enter the cipher text: ')
n=16
iv=0x0000000000000000
k = int(input('Enter the key: '),16)

c=[m[i:i+n] for i in range(0, len(m), n)]

i=0
pt=[]
print('---------------------------------')
for t in c:
    ct=int(t,16)
    cblock=decrypt.decryptDes(ct,k)
    print('Cipher block {} :{:x}'.format(i,cblock))
    pt.append('{:x}'.format(iv^cblock))   
    i+=1
    iv=cblock
print('---------------------------------')
print('Plain Text Blocks:')
for p in pt:
    print(p)
print('----------------------------------')

