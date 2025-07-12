def rotateLeft(a,d):
    return a[d:] + a[:d]
 
def rotateRight(b,d):
    return b[-d:] + b[:-d]
 
a = [1,2,3,4,5,6,7,8]
b = [1,2,3,4,5,6,7,8]
d = 3
 
print(f"\nrotate Left : {rotateLeft(a,d)}")
print(f"\nrotate Right : {rotateRight(b,d)}")