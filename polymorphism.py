"""def add(a,b,c):
    print(a+b+c)
add(2,4,10)

def add(c=10):
    print(c)
add(50) #=> it is a first preority c can print 50 not 10
"""
def add(a,b,c=0):
    print(a+b+c)
add(1,2)
add(1,2,3)#=> it is a first preority c can print 50 not 10
