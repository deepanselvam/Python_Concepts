#scope

#global

name="deepan"     #Global variable

def greeting():
    print(name)

greeting()    
print(name) #name will call inside the function and also outside


#local scope

def local(f_name):
    age=20
    print('')
    print(age)
    print(f_name)

local("deepan")
#print(age)  # it become error because it local onlu use inside the function
#print(f_name) #it also local scope function parameter
   
#global function
def another():
    print("")
    local("raja")
another()    

#local function
age=20  #it cannot be use when age is present inside function
def l_another():
    print("")
    age=20            # age is outside the function but it can be use because function inside function
    def local(f_name):
        print('')
        print(age)
        print(f_name)
    local("deepan") 

l_another() 
#local()# cannot use this function inside the l_another function

# global
def a_no():
    color="blue"
    def Global():
        nonlocal color   # avoind red and take blue as a color
        color='red'   
        print(color)#blue
    Global()
a_no()        
