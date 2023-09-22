#Dictionary 
#Dictionary is an unordered collection of key-value pairs enclosed with {}
#Dictionary is mutable
#Dictionary can be nested inside another dictionary.
#Key value pair are separated by a colon (:) and values in the same line as keys or on new lines.
#Keys must be unique, but duplicate values will overwrite previous ones.

Fruit = {"Apple": 10 , "Orange":20}
print(Fruit)
#Adding a new element

Fruit["Mango"]=22
print(Fruit)
Fruit['sugar']=20
print(Fruit)

#Changing an existing element

Fruit["Apple"]=100
print (Fruit)
#Deleting elements from Dictionary using del keyword
del Fruit["Mango"] #deleting Mango
print ("After deleting mango")  
print (Fruit)

#update one dictionary's elements with another 
fruit_dict={"apple" :5,"orange":6 }
vegetable_dict={ 'potato':7,'tomato' :8 ,'cabbage':9}
fruit_dict.update(vegetable_dict)
#updating fruit dict with vegetables dict
print("after updating the dictionary the result is : ")
print(fruit_dict)

#Popping an element 
popped=fruit_dict.pop('apple')    
#(key,default) poping apple out of fruits list
print("\nThe poped item was : ",popped,"\nNow our updated dictionary looks like this :")
print(fruit_dict)

