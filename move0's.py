 
li = [12, 0, 45, 6, 0, 90, 89, 0, 67, 0, 45, 0]
sorted = sorted(li)
print(f"Output with sorted,reversed : {sorted[::-1]}")
 
def moveZeros(li):
    result = [d for d in li if d!=0]
    result += [0] * (len(li) - len(result))
    print(f"\nOutput without sorted : {result}")
 
moveZeros(li)
 