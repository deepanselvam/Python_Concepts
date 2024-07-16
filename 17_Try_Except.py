# try exception is known as catching error and print 
#or checking error

x=1

try:
    print(x/0) # it is name error
except NameError:
    print('NameError means something is probably undefine')

except ZeroDivisionError:
    print('pleace do not divide by Zero.')
except Exception as error:  # catching error
    print(error)    

else:
    print('no error!')

finally:
    print("I'm going to print the result with or without error" )        