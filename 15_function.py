#function
#fuction is a block of code which performs a specific task
def my_func():
    print("Hello from a function")
my_func()


def sum1(x):
    return x+10

print(sum1(2))


def sum1(x):
    return x+20

print(sum1(2))

def even(x) :
    if (x% 2 == 0 ):
        return True
    else:
       return False
print(even(7))

#lambda funtion 

g = lambda x : x * x* x
print(g(2))


list2 = [23,3,45,33,4,5,34,23,5,3,34]

newlist1 = list( filter(lambda x : (x>=30) , list2))
print('New List', newlist1 )

#lambda with map 
lst4 = [1 ,2,3,4,3,55,5,5,3]
newlst4 = list(map (lambda x : x*2,lst4))
print(newlst4)

# lambda with reduce 
from functools import reduce
sum = reduce(lambda x, y : x+y , lst4)
print(sum)

