print("九九乘法表")
i=1
j=1

while i<=9:
    while j<=i:
        print("%d*%d=%d\t"%(j,i,i*j),end="")
        j+=1
    print()
    j=1
    i+=1
