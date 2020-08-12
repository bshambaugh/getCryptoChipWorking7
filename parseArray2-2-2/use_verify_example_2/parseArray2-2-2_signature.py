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
0xD4, 0x4D, 0x37, 0x08, 0x27, 0x73, 0x29, 0x49, 0x9A, 0xB8, 0x33, 0xA3, 0x15, 0x56, 0x7D, 0xC9,
0x7B, 0x20, 0x1C, 0x94, 0x8E, 0xC9, 0x20, 0xBD, 0x1F, 0x9D, 0x71, 0x06, 0xD3, 0x16, 0xAA, 0x85,
0xA8, 0x34, 0x7A, 0x7E, 0xD7, 0x4B, 0x7F, 0x17, 0xC1, 0xF1, 0x23, 0xD3, 0xDC, 0x36, 0xC4, 0xE8,
0x3C, 0x4A, 0x00, 0x6D, 0x42, 0x67, 0x59, 0x94, 0x86, 0x1D, 0xCD, 0xCD, 0xEC, 0x5A, 0xED, 0xE9
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

