#TUPLE
#Tuple is an ordered collection of elements enclosed within ()
tup1 = ( 2 , 'Ankit' , ' Naveen' , True)
print(tup1)
#NOTE 
#tuple are immutable, which means they cannot be changed.
#Tuples can have different data types in it but all the----
# ----datatypes should be same as that of tuple itself or else we get error.
t1 = tup1[0]
print(t1)

t2 = tup1[-1]
print(t2)

t3 = tup1[1:4]
print(t3)

t4 = len(tup1)
print(t4)

tup2 = (1,2,3)
tup3 = (4,5,6)
t5 = tup2 + tup3
print(t5)

t6 = tup3 + tup2
print(t6)

# repeating tuple Elements 

tup7 = ('Black panther' , 3000)
res = tup7*4
print(res)

#Repeating and Concatenating

tup8 =( "Hello" ,"World") *  2
print(tup8 )
tup9 = ( 3,4,54,45,4,5)
print(tup8 + tup9)

# find the min and max value 

tup10 = ( 34 , 3,43,34,3,3434,3,4,343)
print(min(tup10))
print(max(tup10))

