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

signature = [
0xD1, 0x84, 0x7E, 0x48, 0xD1, 0x40, 0x52, 0x87, 0xFF, 0x97, 0x49, 0x65, 0x66, 0x7D, 0x57, 0xE7,
0xF4, 0x38, 0xF2, 0x02, 0xA9, 0x8C, 0x9D, 0x17, 0x27, 0x5C, 0x59, 0x92, 0x2D, 0x12, 0x2B, 0xE7,
0xF9, 0x0D, 0x7A, 0x68, 0xB1, 0x6A, 0xB0, 0x5D, 0x47, 0x2C, 0x59, 0x1A, 0xDF, 0xC3, 0xCA, 0x77,
0x20, 0x4E, 0xC6, 0xAB, 0x8A, 0xC7, 0x99, 0x53, 0xE5, 0x14, 0xD2, 0x82, 0x04, 0x4F, 0x50, 0xB9
];

concat = ""
n = 2
count = 0

if ( len(signature) % n == 0):
   k = len(signature) / n
else:
   # dump the entire array if it is not divisible by n
   k = len(signature)

while (count < len(signature)):
   # print ('The count is:', count)
   u = count + k
   print ("The lower:",count,"The upper:",u)
   printarray(count,u,signature,concat)
   count = u

print brokenKey

print "----------------- the int x,y --------------"

print(int(brokenKey[0],16))

print(int(brokenKey[1],16))

