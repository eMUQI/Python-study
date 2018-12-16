i=1
j=1
while i<=5:
    while j<=i:
        if i==3:
            break
        print(j,end="")
        j+=1
    print()
    j=1
    i+=1

print(10*"-")

i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i)

print(10*"-")
