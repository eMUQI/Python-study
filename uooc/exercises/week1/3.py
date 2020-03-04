s = input()
temp = float(s[1:])
if s[0].upper() == "C":
    result = temp*1.8+32
    # print(str(round(result,2))+"F")
    print("F%.2f"%float(round(result,2)))
elif s[0].upper() == "F":
    result = (temp-32)/1.8
    # print(str(round(result,2))+"C")
    print("C%.2f"%float(round(result,2)))
