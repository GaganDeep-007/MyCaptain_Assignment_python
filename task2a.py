n=int(input("Enter the number of elements to be printed :"))
n1 = 0
n2 = 1
count = 0
if n <=0:
    print("Enter a number grater positive number the 0")
elif n == 1:
    print("The Fibonacci number of ",n,":")
    print(n)
else:
    print("The Fibonacci number of the given elements is ")
    while count < n:
        print(n1)
        temp=n1+n2
        n1 = n2
        n2 = temp
        count += 1 