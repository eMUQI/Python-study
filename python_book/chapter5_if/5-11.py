list_of_num = list(range(1, 10))

for num in list_of_num:
    if num == 1:
        print("%dst" % num)
    if num == 2:
        print("%dnd" % num)
    if num == 3:
        print("%drd" % num)
    else:
        print("%dth" % num)
