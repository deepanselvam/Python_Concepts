#Closure is a function having access to the scope
#of its parent function after the paren function has returned
def parent_function(person,coins):
    # coins=3

    def play_game():
        nonlocal coins
        coins=coins-1

        if coins>1:
            print('\n' + person +" has "+str(coins)+' coins left')
        elif coins==1:
            print("\n"+person+' has '+str(coins)+' coin left')
        else:
            print("\n"+person+' is out of coins.')  
    return play_game        

tommy = parent_function("tommy",5)
rose=parent_function('rose',3)

tommy()# 2 coins
tommy()#1 coin

rose()#2 coin
rose()#1 coin

# one function can access many op
# invisiblely store the value in coins
#it is known as closure
 

def make_multiplier_of(n):
    def mulitiplier(x):
        return n*x
    return mulitiplier

# multiple by 3
times3=make_multiplier_of(3)
# multiple by 5
times5=make_multiplier_of(5)

print(times3(5))# 3*5
print(times5(10))# 5*10

print(times5(times3(2))) # 3*2=6 6*5=30


