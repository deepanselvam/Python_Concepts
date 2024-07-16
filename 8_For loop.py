#for loop
fruits=['apple','orange','mango']
for x in fruits:
  print(x)   #all element in fruits
print('')


#adding element 
for x in "deepan":
  print(x)  # all fruits list and 'd','e','e','p','a','n'
print('')

 #break
fruits=['apple','orange','mango']
for x in fruits:
  if x =='orange':    #apple 
    break
  print(x)
print('')

#continue
fruits=['apple','orange','mango']
for x in fruits:
  if x =='orange':
    continue         #apple mango
  print(x)

# for loop -->range<--  
# range will alway 0 when start not given

for i in range(5):
 print(i)                 #01234 

#starting point given
 for i in range(1,4):
     print (i)           #1234 it will be print in new and new line


#three range with else
for x in range(0,101,5):
    print(x)
else:
  print("that's over")


#2 table    
for a in range(1,11):
    print("2x",a,"=",2*a)


n=int(input("n value:"))
for a in range(1,n):
  print(a*"*")
  
  #nested
  names=['deepan','raja','selvam']
  actions=['sleep','eat','study']

for name in names:
 for action in actions:         #deepan sleep deepan eat deepan study 
   print(name+' '+action+'.')    #raja sleep raja eat raja study

for action in actions:
 for name in names:         # sleep deepan sleep raja sleep selvam
   print(name+' '+action+'.')    #eat deepan eat raja   eat selvam


n=int(input())
for n in range(0,n):
    a=n*n
    print(a)
    
#________________________Questions_______________________
"""
get input for number a nd b
print the number between a and b
sample input
8
15
sample output
9
10
11
12
13
14
15

a=int(input("a:"))
b=int(input("b:"))
for i in range(a+1,b):
    print(i)

______________________________________________________________________
print even number between 1to10
sample input:
1,2,3,4,5,6,7,8,9,10
sample output:
2,4,6,8,10

for i in range(1,11):
    print(i)
    if(i%2==0):
       print (i)
___________________________________________________________________________
          counting the even number present in given number between
          
count the number even number between 1to 10 and print it
sample output
5

count=0
for i in range(1,11):
    if(i%2==0):   #wen it is pass count will add itself
        count=count+1 #when if condition is true the
                      #,count become 0+1=1,1+1=2.....5
print(count)

______________________________________________________________________________
         counting the even number present in given number between

count the number of odd and even number between 1 to 10
sample input
1
2
3
4
5
6
7
8
9
10
sample output
even 5
odd 5

 
e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):   
        e_count=e_count+1 
    else:
        o_count=o_count+1
print(e_count)
print(o_count)

___________________________________________________________________________
  count the number which are divisible by 3 and 5 range 1-100


count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):   
        count=count+1 
print(count)

___________________________________________________________________________


write a program to campute the sum of the first 5 natural numbers

sum=0
for i in range (1,6):
       sum=sum+i
print(sum)

__________________________________________________________________________
                    for loop with list
                    
 read 10 number from the keyboard and find  sum and average 


a=[]
print("enter the 10 number's:")
for i in range(5):
    num=int(input("num:"+str(i+1)))
    a.append(num)
    print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)
_________________________________________________________________

to display n terms of natural numbers
sample input
7
sample output is
1234567


num=int(input("data:"))

for i in range(num+1):
  if(i<=num):
      num=num-1
      print(num)
else:
       print("")

 _______________________________________________________________________
                                CUBE VALUE
bye the input as a number and displa the number and its cube value
  
i=int(input("give som number"))
for i in range(i+1):
    
   print("number is :",i,"the cube value is",i*i*i)


 """















   