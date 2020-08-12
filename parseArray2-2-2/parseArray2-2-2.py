brokenKey = []

def printarray(l,u,a,concat):
 while l < u:
    # with the hex method I do not always get two placeholders
    # see https://stackoverflow.com/questions/2269827/how-to-convert-an-int-to-a-hex-string
    # seeAlso: [200~https://docs.python.org/3.4/library/stdtypes.html?highlight=find%20method#float.hex
    # print("current:",l,hex(a[l]))
    #  print("current elem",l,a[l])
     print("current element:",l,"%0.2X" % a[l])
     concat = concat + ("%0.2X" % a[l])
    # concat = concat + hex(a[l]).lstrip("0x").rstrip("L")
     print concat
     l += 1
     if(l == u):
        brokenKey.append(concat)

publicKey = [
0xF9, 0xC3, 0x6F, 0x89, 0x64, 0x62, 0x33, 0x78, 0xBD, 0xC0, 0x68, 0xD4, 0xBC, 0xE0, 0x7E, 0xD1,
0x7C, 0x8F, 0xA4, 0x86, 0xF9, 0xAC, 0x0C, 0x26, 0x13, 0xCA, 0x3C, 0x8C, 0x30, 0x6D, 0x7B, 0xB6,
0x1C, 0xD3, 0x67, 0x17, 0xB8, 0xAC, 0x5E, 0x4F, 0xEA, 0x8A, 0xD2, 0x3D, 0xC8, 0xD0, 0x78, 0x3C,
0x23, 0x18, 0xEE, 0x4A, 0xD7, 0xA8, 0x0D, 0xB6, 0xE0, 0x02, 0x6A, 0xD0, 0xB0, 0x72, 0xA2, 0x4F
];

concat = ""
n = 2
count = 0

if ( len(publicKey) % n == 0):
   k = len(publicKey) / n
else:
   # dump the entire array if it is not divisible by n
   k = len(publicKey)

while (count < len(publicKey)):
   # print ('The count is:', count)
   u = count + k
   print ("The lower:",count,"The upper:",u)
   printarray(count,u,publicKey,concat)
   count = u

print brokenKey

print "----------------- the int x,y --------------"

print(int(brokenKey[0],16))

print(int(brokenKey[1],16))

