import encrypt
import binascii as bin
ct=[]
m = input('Enter the Plain text: ')
n=16
iv=0x0000000000000000
k = int(input('Enter the key: '),16)

p=[m[i:i+n] for i in range(0, len(m), n)]

i=0
ct=[]
print('---------------------------------')
for t in p:
    pt=int(t,16)
    pt=pt^iv    
    pblock=encrypt.encryptDes(pt,k)
    ct.append('{:x}'.format(pblock))  
    print('Plain Text block {} :{}'.format(i,t))
    i+=1
    print('IV {:x} cblock {:x}'.format(iv,pblock))
    iv=pblock

print('---------------------------------')
print('Cipher Blocks:')
for l in ct:
    print(l)
print('----------------------------------')

