def hello():  # no parameter there
    print('hello')

hello() 


def sum(num1,num2):   #num1 and num2 are parameters
    return num1+num2

total=sum(2,5)    # 2,5 are arguments
print(total)

totalname=sum('deepan',"raja") #deepanraja
print(totalname)


#only intejer
def sum(num1,num2):   #(num1=1,num2) is default value
    if(type(num1) is not int or type(num2) is not int):
       return('somthing is given as string')
    return num1+num2

total=sum(2,6)    # 2,5 are arguments
print(total)

#multiple argument inside function  stringss..
def multi_item(*args):    # print as a tuple
    print(args)
    print(type(args))

multi_item('deepan','selvam','sumathi')


#multiple interger inside function   numbers...
def num(*num):            # print as a tuple
    sum=0
    for n in num:
        sum=sum + n  # 0+3=3 and 3+8=11
    print('sum:',sum)    
num(3,8)    # 11


#key and value in function
def mul_name(**kwargs):     # op wil be dictionary
    print(kwargs)
    print(type(kwargs)) 
mul_name(first='deepan',last='raja')    


def func(a,b,*args,option=True,**kwargs):
    print(' ')
    print(a,b)     #op integer 
    print(args)    # op tipule
    print(option)  #op boolen
    print(kwargs)  #op dictionary
func(1,2,10,20,name='deepan',city='salem')   



#recursion
def add_one(num):
    if num>=9:
        return num+1
    
    total=num+1
    print(total)

    return add_one(total)

mynewtotal=add_one(0)
print(mynewtotal)




#recrution factorial
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

num=6

if num<0:
    print('invalid input ')
elif num==1:
    print('factorial of number 0 is 1')
else:
    print('factorial number ',num,'=',factorial(num))        