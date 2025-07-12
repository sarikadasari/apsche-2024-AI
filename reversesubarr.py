l = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
k = 3
 
def revSub(l):
    rev = []
    for i in range(0,len(l),k):
        rev += l[i:i+k][::-1]
    print(rev)
 
revSub(l)