#dictionary
car={
    "brand":"tesla",
    "model":"1990",
    "year":2024
  }
car2=dict(brand='tesla',model="1990",year=2024)

print(car)
print(car2)
print(type(car))

# Access item inside the dict
print(car["model"])  #1990
print(car["brand"])  #tesla

#list all keys
print(car.keys()) #all keys

#list all values
print(car.values()) #all values

#list of keys/values conver as tipules
print(car.items())  #all keys and values 

#checking is it present or not 
print("model" in car) #true
print("price" in car)#False

#change the value using key
car["brand"]="mustang"
car.update({"price":10000})
print('')
print(car)

#remove 
print(car.pop("price")) #last value is deleted and return the value
# only value  is return ->(10000) but delete hole key and value in pop
print('')

car['eve']="yes" #adding element to dict
print(car)


#popitem  return tuple like ('eve','yes')
print('')
print(car.popitem())#delete the key and value in the {dict}

#delete and clear
print("")
car["deacl"]="yes" #addind element
del car["deacl"]   #deleting the same element before added
print(car)
print('')


#delete hole element
del car2
#or
# car.clear(car2) # car2 will be empty
# print(car2)

#copying dict
car2=car.copy()
car2['eve']='yes'
print('')
print(car2)

#or   use dict()
car3=dict(car)
print('')
print(car3)


#Nested dictionaries
print('')
member1={
    'name':'plant',
    'instrument':'brand',
}
member2={
    'name':'page',
    'instrument':'model'
}
band={
    'member1':member1,
    'member2':member2
}

print(band) 
print('')
print(band['member1'])#only member1 is display
print(band['member1']['name']) # member1 inside name only



#_______________________SET_____________________________
 #set does'n take duplicate value

number={1,2,3,4}
number2=set((1,2,3,4))

print(number)
print(number2)
print(type(number))
print(len(number2))

# No Duplicate Value
nums={1,2,2,3,4,4}   
print(nums)     #{1,2,3,4}

nums={1,True,2,False,0,3,4} #true=1 false=0
print(nums)  #{False,1,2,3,4}

#check value in set
print(2 in nums) #true  

#in set cannot access index value

# add a new element
nums.add(8)  
print(nums)    #{False,1,2,3,4,8}

# and element from one set to another
more_nums={5,6,7,9}
nums.update(more_nums)
print('')
print(nums)

#update with list tipule,dict.. 

#merge two set to create new 
one={1,2,3,4}
two={5.6,7,8,9}

mynewset=one.union(two)
print(mynewset)

#keep only the duplicate
one={1,2,3,4}
two={2,4,5,1}
one.intersection_update(two)
print(one)


#keep everithig without duplicate
one={1,2,3,4}
two={2,4,5,1}
one.symmetric_difference_update(two)
print(one)

