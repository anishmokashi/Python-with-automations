
Set1 = {11,78.89,"Hello",True}
print(Set1)

# print(Set1[1])

for value in Set1:
    print(value)

Set2 = {11,78,89,11,78}
print(Set2)

Set2.add(101)
print(Set2)

Set2.remove(101)
print(Set2)

print("Enter the value that you want to search in Set")
No = int(input())

for value in Set2:
    if(No == value):
        print("Element is present")
        break

