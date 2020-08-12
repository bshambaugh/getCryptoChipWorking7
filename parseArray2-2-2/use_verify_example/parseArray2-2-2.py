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
0xB4, 0x07, 0x88, 0x28, 0x8C, 0xFA, 0x71, 0xBA, 0x08, 0xE3, 0x38, 0xE0, 0x4A, 0x17, 0X68, 0xCC,
0x3E, 0xCD, 0x48, 0xA8, 0x11, 0x52, 0xDD, 0x37, 0xA1, 0xC2, 0x55, 0x75, 0x81, 0xBE, 0X4E, 0x7E,
0x78, 0x98, 0x95, 0xF6, 0x6D, 0XE7, 0x1C, 0x9A, 0x36, 0xE6, 0xB0, 0x14, 0x5D, 0x50, 0x67, 0x91,
0x7C, 0X41, 0xB8, 0x99, 0x20, 0x75, 0x3A, 0x7D, 0xA1, 0xFB, 0xF5, 0x5E, 0X8A, 0x65, 0xF5, 0x8A
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

