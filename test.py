#square value of element in a list
from numpy import sqrt

a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i < 5:
        print(sqrt(i))
    else:
        print("0")
