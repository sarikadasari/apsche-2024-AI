expr=input()

open=0
close=0

for char in expr:
    if char=='(':
        open+=1
    elif char==')':
        close+=1
        if close>open:
            print("Not")
            break
else:
    if open==close:
        print("Balanced")
    else:
        print("Not Balanced")