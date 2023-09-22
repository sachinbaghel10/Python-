#List
#list is an ordered collection of elements enclosed with []
#list is mutable 
#list can contain different data types like int, float and string
#list are used to store multiple values in a single variable
#list items are separated by commas.
#list indexing starts from zero (0) not one(1).
#list slicing [start:end] - start at index 'start' up until but NOT including the element indexed by end.
#negative indexes count backwards from the last item (-1 refers to the last list item)
#lists can be nested inside other lists
#you can use + operator on two or more lists to concatenate them into a new list
#use * operator on any iterable object such as strings, tuples etc., to repeat it n times
#the len() function returns length/size of a given sequence i.e number of items present in that sequence
#to add something to your list you have append(), insert() methods available for this purpose
#to remove some thing form your list you have pop() method which removes the first occurence of specified value if found else raises error
#append adds value to the end of existing list while inserting inserts value at specified position

l1 = [1 , 'a' , True] * 2
print(l1)
print(l1[1])
print(l1[-1])
print(len(l1))
print(l1[1:3])

l2 = [ 1,2,34,4,453]
l3 = [ 33,3,4,56,7,67,67]
print(l2 + l3)

#changing the element at 0th index
l2[0]=98
print(l2)

# Popping the last element 
l4 = l3.pop()
print(l4)

#Appending a new element
l6 = [2 , "a" , 4 ,5]
print(l6.append("kese ho"))

list1 = [1 , "a" , 2 , "b" , 3 , "c"]
list1.append("python")
print(list1)
list2 = list1
print(list2)

#Reversing element of a list 

rev = [1 , " a" , 3,3, 45,45,676,42 ]
rev.reverse()
print(rev)

# Sorting a list

srt = ["mango" , "banana" , "guava" , "apple"]
srt.sort()
print(srt)

# Inserting element at a specified index

insrt = [1 ,2,3,4,5]
insrt.insert(1,"AHIRWAR")
print(insrt)


