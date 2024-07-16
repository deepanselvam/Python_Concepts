class Vehical:
    def __init__(self, company,model,diesel_or_petrol):
        self.company=company
        self.model=model
        self.diesel_or_petrol=diesel_or_petrol

    def move(self):
        print('move along...')

    def get_full_content(self):
        print(f'It\'s {self.company} Company And Model was {self.model} And It was an {self.diesel_or_petrol} Vehicle')   

my_car=Vehical('TATA','NEXON','ELECTRICAL')

my_car.get_full_content() #It's TATA Company And Model was NEXON And It was an ELECTRICAL Vehicle
print(my_car.company)#TATA
print(my_car.model)#nexon
my_car.move()#move along


#inheritance class
class Airplane(Vehical):
    def __init__(self, company, model, diesel_or_petrol,FA_ID):
        super().__init__(company,model,diesel_or_petrol) # super can use same value inside the Vehical
        self.FA_ID=FA_ID
    def move(self):
        print('Flies Along...')



class Truck(Vehical):
    def move(self):
        print('Rumble Along...')


class Glf(Vehical):
    pass      # pass is known as all element inside the Vehicle class come inside the class  



my_airplane=Airplane('kingFisher','skyhawk',"white petrol",'TN23J1233')
print(my_airplane.FA_ID)

my_truck=Truck("mahendra","v7",'Diesel')
my_golf_cart=Glf('yamaha','GC100','diesel')


my_airplane.get_full_content()
my_airplane.move()


my_golf_cart=Glf('yamaha','GC100','Petrol')
# polimarpisam


my_truck.get_full_content()
my_truck.move()

my_golf_cart.get_full_content()
my_golf_cart.move


for v in (my_car,my_airplane,my_truck,my_golf_cart):
    v.get_full_content()
    v.move()









class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoyment the beach")
ramesh = goa() # it is know as ramesh is able to acces party and beach in goa
suresh = goa() # it is know as suresh is able to acces party and beach in goa
ramesh.party()# rames can able to acces anyone but ramesh whant only party
suresh.beach()


class goa:
    name="ghdrrf" #ramesh is stored
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoyment the beach")
ramesh = goa() 
suresh = goa()
ramesh.name="ramesh" #ramesh is stored in the name variable in goa class
suresh.name="suresh"
ramesh.drink="yes"   #yes is tored in drink variable in goa class
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
ramesh.party() #function call

print(suresh.name)
print("drink:",suresh.drink)
suresh.beach() #function call

# create class called laptop
# create following variable and functions
# variable=> price,processor,ram
# creat object hp,dell,lenova

class laptop:
    price=""
    proc=""
    ram=""
hp=laptop()
dell=laptop()

hp.price="1000"
hp.proc="i5"
hp.ram="4GB"

dell.price="10000"
dell.proc="i5"
dell.ram="6GB"
print(hp.price)
print(dell.price)


#                      BIKE SPECIFICATION

class bike:
    price=""
    color=""
    model=""
re350=bike()
re500=bike()
re800=bike()

re350.price="1.5L,2.5L,4.5L"
re350.color="black,borun,blue"
re350.model="2020,2022,2023"
    
re500.price="3.5L,4.5L,5.5L"
re500.color="black,borun,blue"
re500.model="2020,2022,2023"
    
re800.price="4.5L,5.5L,6.5L"
re800.color="black,borun,blue"
re800.model="2020,2022,2023"

print(re350.price)

class bike:
    name=""
    def re350(self):
        print("price = 1.5L,2.5L,4.5L")
       

    def re500(self):
        print("price = 2.5L,3.5L,4.5L")

    def re800(self):
       print("price = 3.5L,4.5L,5.5L")

ramesh=bike()
ramesh.name="350" #assigen value 
print(ramesh.name) #350
ramesh.re350()   #price = 1.5L,2.5L,4.5L

#___________________________________________________________
class laptop:            # __INIT__ IS KNOWN AS CONTRUCTOR
    def __init__(self): #__init__ is python inbuild function
        print("deepan")  # if not call the functio but it take automaticaly
    def display(self):
         print("display")
         
hp=laptop()#object created named as hp

#____________________________________________________________

class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.proc=""
    def display(self):
         print("price:",self.price)
         print("proc:",self.proc)
         print("ram:",self.ram)

hp=laptop()
hp.price=20000
hp.ram="8gb"
hp.proc="i5"
print(hp.ram)
hp.display()
#______________________________________________________________

