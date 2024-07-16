name="Deepan"
coins=3

#normal print
print('\n'+name+' has '+ str(coins) +'coins left')


#previous %s formatting
message='\n%s has %s coins left.'%(name,coins)
print(message)
#previous string.format()

message="\n {} has {} coins left.".format(name,coins)
print(message)

message="\n {1} has {0} coins left.".format(coins,name)
print(message)


message="\n {name} has {coins} coins left.".format(coins=coins,name=name)
print(message)



#dictionary format
player={'person': 'Raja','coins':3}
message="\n {person} has {coins} coins left.".format(**player)
print(message)




#______________________________________________

#f-string! this is the way
message=f'\n{name} has {coins} coins left.' #no need to denote the value of name and coins
print(message)

#mat opratin
message=f'\n{name} has {2*3} coins left.' 
print(message)    # 6 coins in op


#method calling
message=f'\n{name.lower()} has {2*3} coins left.' 
print(message)   

# calling dictionary in f string
message=f'\n{player['person']} has {2*3} coins left.' 
print(message) 

# decimal value
num=10
print(f'\n2.25 times {num} has {2.25*num:.2f}')


#for loop 
for num in range(1,11):
   print(f'2.25 times {num} has {2.25*num:.2f}')

for num in range(1,11):
   print(f'0.5 times {num} has {0.5*num:.2%}')









#  unique module to use
# import math
# print(math.pi)
# print('')
# from math import pi   # taking only pi in math function
# print(pi)

# import random as rdm  # random function named as rdm
# print(dir(rdm)) # all random directory 
# for item in dir(rdm):
#    print(item)
