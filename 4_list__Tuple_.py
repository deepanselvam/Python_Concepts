# __________________list[]______________________________  
# an store all type of datatype
g_list=['apple','milk','banana']
data=['deepan',True,27]
empty=[]

print('apple'in g_list)  #checking is ther or not in list
print(data[0]) #deepan
print(data[-1]) #27
print(g_list.index('milk')) #find the position in list
print(g_list[0:2]) #apple milk
print(len(data)) # length of the list 3


#adding in list
print('')
g_list.append('orange') 
print(g_list)
#or
g_list+=['grape']
print(g_list)


 #extend same as uppend
print('')
g_list.extend(['papaya'])  # need to put "[]" but not in uppend
print(g_list)


#combaining in tow list in same
print('')
g_list.extend(data)   #g_list and data added in same list
print(g_list)


#insert
print('')
g_list.insert(0,"mutton") #mutton will added in first element in list 
print(g_list)
 #or
g_list[2:2]=['onion','rice'] # add in that given position
print(g_list)

g_list[1:3]=['chilli','tomato']  # replace the previous data
print(g_list)

#remove
print('')
g_list.remove('banana') # remove banana in the list
print(g_list)

#pop
print('')
print(g_list.pop()) #it print what delete in last
                    #delete the last element in list
print(g_list)

#delete
print('')
del g_list[0]
print(g_list)# delete first element

# del data
# print(data) #delete hole list

# data.clear() #delete hole list
# print(data)


#sort     sort only work only have string in the list 
# print('')
# g_list[1:2]=['Salt']
# g_list.sort(key=str.lower)
# print(g_list)


#reverse

num=[1,2,13,4,5]
num.reverse() #reverse the number
print(num)

num.sort() #small to big 
print(num)

num.sort(reverse=True) #big to small number
print(num)

num=[1,24,56,23,5]
print(sorted(num,reverse=True)) #changes applied list

#copies   types
print(num)  #orginal list or orginal copi
numCpoys=num.copy() # orginal list
number=list(num)#same as orginal list
mycopy=num[:]


#__________________TUPLE ()_____________________________
# list can change delete inset the element in lis
#but tuble cannot change the values or elements

my_tuple=('deepan',27,True)
a_tuple=(1,2,2,4,5,6)
print(type(my_tuple)) #tuple

#change tuple

new_list=list(my_tuple)
new_list.append('hello')
newtuple=tuple(new_list)
print(newtuple )
(one,*two,hey)=a_tuple
print(one)
print(two)
print(hey)

print(a_tuple.count(2))#2 in this list 2 is present in 2 time
print(a_tuple.count(4))#1 4 is present one time

