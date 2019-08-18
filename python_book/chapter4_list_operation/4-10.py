list_of_num = [i**3 for i in range(1, 11)]
print(list_of_num)

print("The first three items in the list are: %s" % str(list_of_num[:3]))
print("Three items form the middle of list are: %s" %
      str(list_of_num[int(len(list_of_num)/2)-1:int(len(list_of_num)/2)+2]))
print("The last three items in the list are: %s" % str(list_of_num[-3:]))
