l1=[12,-7,5,64,-14]
print("The positive number in the range of ",l1 ,"are:")
for num in l1:
        if num >= 0:
          a = [num for num in l1 if num >= 0]
          print (num, end=" ")
          
print("\n")

l2=[12,14,-95,3]
print("The positive number in the range of ",l2 ,"are:")
for num in l2:
        if num >= 0:
         b = [num for num in l2 if num >= 0]
         print (num, end=" ")
         
print("\n")

li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Positive numbers in the range of",li,"are:")
for i in li:   
    if i >= 0:
       print(i, end = " ")