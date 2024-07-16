#lambda is a mini function or one line function
add_to=lambda num:num+num
print(add_to(2))  #2+2 =4


sum_total=lambda a,b:a+b

print(sum_total(2,3)) # 2 inputs #2+3=5

def funcBuilder(x):
    return lambda num:num*x

add_ten=funcBuilder(10) 
add_twenty=funcBuilder(20)

print(add_ten(2)) #2*10=20
print(add_twenty(2)) # 2*20=40


#higher order function

#map function
numbers=[3,5,7,10,12,20]
square_num=map(lambda num:num*num,numbers)
print(list(square_num))


#filter     taking odd number
odd_num=filter(lambda num:num%2 !=0,numbers)
print(list(odd_num))


from functools import reduce

numbers=[1,2,3,4,5,1]     #acc is 1+2=3 curr=3  acc 3+3=6  curr=4  acc=6  curr=5.....

total=reduce(lambda acc,curr:acc+curr , numbers)
print(total)  #16

#simple to sum
print(sum(numbers)) #16

names=["deepan",'raja','selvam','sumathi']

char_count=reduce(lambda acc,curr:acc+len(curr),names,0) # 0 is for startimg because all arestring now it start in 0
print(char_count)
