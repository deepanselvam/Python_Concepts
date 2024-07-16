class a():                 #parant class
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class a")
class b():                #child class
    def __init__(self):
        super().__init__() # super is used to call the parant class directly
        print("B")
    def display(self):
         print("you are in class b")
class c(a,b): #in multiple in heritance left is calling first c(a) is consider
     def __init__(self):    #
         super().__init__()
         print("c")
     def display(self):
        print("you are in class c")

boj=c()











    
# obj=a()  => a  
# obj=b()  => b

#obj=b()  #it gives a when b constructor is remove
          #it gives a and b with using super() 


