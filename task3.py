def most_frequent(string):
    d = dict()
    for key in string :
        if key not in d:
            d[key] = 1
        else:
            d[key] +=1
    return d
import operator
s = input("Enter a string ")
x = most_frequent(s)
z = dict(sorted(x.items(),key=operator.itemgetter(1), reverse=True))
print ("\n",z)