def invite(templist):
    for temp in templist:
        print("Dear " + temp + ",可以和我一起共进午餐吗？")


list_of_person = ["Person A", "Person B", "Person C"]
invite(list_of_person)

print()
print(list_of_person[-1] + " won't come, so sad.")
print("list update\n")

list_of_person[-1] = "Person D"
invite(list_of_person)
print()

print("I found a bigger table!")
print("list update\n")

list_of_person.insert(0, "Person E")
list_of_person.insert(int(len(list_of_person)/2), "Person F")
list_of_person.append("Person G")
invite(list_of_person)
