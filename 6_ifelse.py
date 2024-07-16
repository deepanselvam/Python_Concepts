"""
#comparision oprator

a=10
if(a==10): #comparision oprator 
    print("yes")       #true and false are boolean value
else:
    print("no")

    

rcb="win"
if(rcb=="win"):
    print("isala cup namde")
else:
    print("cup lose")

"""

megna=input("megna died or not:")
if(megna=="died"):
    print("suriya meet priya")
else:
    print("suriya wed megna")


#_______________ IF else, elif, nested if  questions______________

"""
get input for varible mark.if mark>35 print pass.else print fail
sample input
mark:35
sample output
fail


mark=int(input())
if(mark>35):
  print("you pass")
else:
    print("you fail")


#------------------------------------------------------------------------

 get input for variable income.if income is less than 7000
 scholarship is available.else not eligible for scholarship
 sample input
 income:7200
 sample output
 "not eligible for scholarship"

income=int(input("income:"))
if(income<=7000):
  print("eligible for scholership")
else:
    print("not eligible for scholership")

#-----------------------------------------------------------------------

get input for a number and check wether it is divisible by both 3 and 5 or not.
if yes the print the numbe is divisible by 3 and 5 else print not divisible


number=int(input())
if(number%3==0 and number%5==0):
    print("it is divisible by 3 and 5")
else:
     print("it is not divisible by 3 and 5")

#-----------------------------------------------------------------------
get input for a number find it is even or odd

a=int(input())
if(a%2==0):
    print (" it is an even number")
else:
    print("it is an odd number")

#-----------------------------------------------------------------------
get input for score out of 100
if score is 35but<than 70="average student"
if score is greater than 70="good student"


score=int(input())

if(score>35 and score<70):
    print("average student")
if(score>70):
    print("good student")
else:
    print ("poor student")


#simple methot
score=int(input())
if(score<35):
    print("average student")
elif(score<70):
    print("above average student")
elif(score>70 and score<100):
    print ("good student")
else:
    print("score invalide")
    
#-----------------------------------------------------------------------

                           mini calculator

get 2 input form the user
gri input from the user wether(add,sub,mul,div)
if the user select add and add the tow number and print ir

a=int(input("A:"))
b=int(input("B:"))
c=input("add/sub/mul/div:")
if(c=="add"):
    print("the add number is:",a+b)
elif(c=="sub"):
    print("the subract number is:",a-b)
elif(c=="mul"):
    print("the multiple number is:",a*b)
elif(c=="div"):
    print("the dived numbear is:",a/b)
else:
    print("invalid syntax")

________________________________________________________________________

get input for score percentage,only the persentage greater than 70,get
inptu for name,departmentand,location then print you eligible.if not
print not eligible

score=int(input("enter the percentage:"))
score=score/100*100
print(score)
if(score>70):
  name=input("enter your name")
  department=input("enter our department")
  location=input("enter your location")
  print("you are eligible")
else:
    print("you are not eligible")

________________________________________________________________________________

                                  salary


get input for salary and age

if salary greater than or equal to 20000 or age less than or equalto25,
get input for required loan amount.if not print you are not eligible for loan


salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
     loan=int(input("loan amount:"))
     if(loan<50000):
         print("your loan is eligible")
     else:
        print("your loan amount is reached maximum")
else:
     print("you are not eligible for loan")


________________________________________________________________________________

                          average
 get input for five subject mark add all of it,and find average.
 if average mark is less than 35,print"addition class is required"
 else print "you are good to go"

m1=int(input("tamil:"))
m2=int(input("english:"))
m3=int(input("maths:"))
m4=int(input("scince:"))
m5=int(input("social:"))
s=m1+m2+m3+m4+m5
avg=s/5
print("average mark is:",avg)
if(avg>35):
    print("good to go")
else:
    print("additional class is required")

"""
