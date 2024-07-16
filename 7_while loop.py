i=0
while(i<=5):
    print(i)
    i=i+1


# while(True):
#     print("true")  # op is infinete true
print('break')
#break
i=1
while i<6:
    print(i) 
    if i==3:
        break    #123
    i+=1

 #continue   
print('continue')
# i=1
# while i<6:
#     print(i) 
#     if i==3:
#         continue    #33333333......
#     i=+1   

i=0
while i<6:
  i+=1  
  if i==3:
    continue    #1245  when i=3 it will coninue 
  print(i) 

#while inside if and else

i=0
while i<6:
  i+=1  
  if i==3:
    continue    #1245  when i=3 it will coninue 
  print(i) 
else:
   print('i is no longer than 6')


# # ________________________question's__________________________

# # -------print the number from 1 to 5 using while loop                                  
 
# i=1

# while(i<=5):
#     print(i)
#     i=i+1


# #------print following series 10,20,30,40,50,60,....200

# i=10
# while(i<=200):
#     print(i,end=",")
#     i=i+10


# # ---------write a program to print first 10 natural numbers in reverse order
# # 10,9,8,7,6,5,4,3,2,1

# i=10
# while(i>=1):
#     print(i,end=",")
#     i=i-1


# # -------to find the factorial of a number

# i=int(input("num:"))
# fact=1
# while(i>0):
#   fact=fact*i
#   i=i-1
# print(fact)
