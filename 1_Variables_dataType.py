#______________variables__________________________

a=10      # a is known as valiable name
b=10       # b is known as valiable name
print(a+b)

f_name='deepan'   #f_name is known as variable
l_name='raja'     #l_name is known as variable
num=123           #num is known as variable


#_______________________DataType_____________________

#string
f_name='deepan'   
l_name='raja'


print(f_name)   # deepan
print(type(f_name))  #<class 'str'>
print(type(f_name)==str)  #true
print(isinstance(f_name,str)) #true

#integer
num=123
print(isinstance(num,str))  #false

#float
num1=1.076
print(type(num1))  # <class 'float'>

#boolean data type
myvalue=True
x=bool(False)

print(type(x))  #<class "boolian">
print(isinstance(myvalue,bool)) #true

#complex type      #real valu and imaginary value
comvalue=5+3j
print(type(comvalue))   
print(comvalue.real) #5
print(comvalue.imag) #3

#input from user

a=input("enter somethis")    # it will be string input
b=int(input("enter"))        # it will be integer input

print(isinstance(b,str))



#concatenation
full_name=f_name +" "+l_name+'!'
print(full_name)


