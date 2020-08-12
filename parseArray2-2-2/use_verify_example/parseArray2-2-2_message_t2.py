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

message = [
0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F
];

concat = ""
n = 64
count = 0

if ( len(message) % n == 0):
   k = len(message) / n
else:
   # dump the entire array if it is not divisible by n
   k = len(message)

while (count < len(message)):
   # print ('The count is:', count)
   u = count + k
   print ("The lower:",count,"The upper:",u)
   printarray(count,u,message,concat)
   count = u

print brokenKey

print "----------------- the int x,y --------------"

print(int(brokenKey[0],31))

#print(int(brokenKey[1],16))

