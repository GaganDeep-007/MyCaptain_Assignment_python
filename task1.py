pi = 3.14
radius = float(input("Enter the radius of circle "))
area = pi*radius*radius
print("Area of circle is " + str(area))

print("--------------------------------------------------------------------------------------------")

filename = input("Input the Filename: ")
f_extns = filename.split(".")
d = {'py' : 'python', 'txt': 'Text', 'java': 'Java','js':'JavaScript'}
ext =  f_extns[-1];
value = None
if(ext in d):
    value = d.get(ext)

if(value != None):
    print ("The extension of the file is : " + value)
else: 
    print ("The extension of the file is : " + ext)