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
0x7D, 0x88, 0xC5, 0x5A, 0x89, 0x04, 0xB4, 0x7C, 0x67, 0xAD, 0x76, 0xBD, 0xE9, 0x17, 0xE1, 0x4F,
0x33, 0xD4, 0x82, 0xD0, 0xD9, 0x3D, 0xF5, 0xC5, 0x31, 0x84, 0xA4, 0xAD, 0x8E, 0xFD, 0x6E, 0x97,
0xCA, 0x67, 0x52, 0xCA, 0xDC, 0xA7, 0x82, 0xD4, 0x8D, 0x8C, 0x8C, 0x83, 0xE1, 0xEA, 0x07, 0x35,
0xFE, 0XEE, 0x5A, 0x04, 0x6E, 0x3F, 0x3D, 0x47, 0x06, 0x63, 0x34, 0x82, 0x58, 0x8D, 0x41, 0x8D
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

