list_of_person = ["Person A", "Person B", "Person C"]
for temp in list_of_person:
    print("Dear " + temp + ",可以和我一起共进午餐吗？")

print()
print(list_of_person[-1] + " won't come, so sad.")
print("list update\n")

list_of_person[-1] = "Person D"
for temp in list_of_person:
    print("Dear " + temp + ",可以和我一起共进午餐吗？")
