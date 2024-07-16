#_______________________small commends_________________
sentence='I\'am Deepan raja \t welcome \n to my webpage'
# (\)  is taking (') also   \t -> tab spacing  \n-> new line


#________________________methods_________________________
sentence_2="i\'am deepan raja im front-end developer"
print(sentence_2.lower())   # all letter get lowe case

print(sentence_2.upper())   # all letter get upper case

print(sentence_2.capitalize()) # first letter is capital

print(sentence_2.title())   # all words first letter be caps

print(sentence_2.replace("front-end","python"))  #repalce "front-end" to "python"

print(len(sentence_2))  #39
sentence_2+='                '
sentence_2="   "+sentence_2
print(len(sentence_2)) #58     # in this  '   ' gap will applay in front and back

print(len(sentence_2.strip())) #39 it will remove all unwanted gaps
print(len(sentence_2.lstrip())) #55
print(len(sentence_2.rstrip())) #42

#______________________________string Index Value_____________________________
str='hello'
print(str[0]) #h
print(str[4]) #0
print(str[:]) #hello  ":" is take all value

#bunch element
print(str[:0]) #hello
print(str[:3]) #hel
print(str[:5])#hello
print(str[0:4])#hell or [0:-1]
print(str[1:3])#el
print(str[-1])#o  last letter

#some methods return boolean data
print(str.startswith('h')) #checking "h" is a starting letter or not
print(str.endswith('o'))#checking ending letter is "o" or not


#__________________________number methods__________________________
floatvalue=3.28
print(abs(floatvalue)) # absaloute value of floatvalue

print(abs(floatvalue * -1)) # it will became "-3.28" but the op is absaloute so "3.28" is op

print(round(floatvalue)) # 3

print(round(floatvalue,1)) #3.3

import math
print(math.pi) #3.1415.......
print(math.sqrt(64)) # 8.0  8*8=64
print(math.ceil(floatvalue)) #4 beacuse 3.28 aftre the round number is 4
print(math.floor(floatvalue)) #3 because 3.28 base low value is 3



#______________________________small proj_______________________
 #build menu

title="menu".upper()
print(title.center(20,'='))
print("coffee".ljust(16,'.')+"$2".rjust(4))
print("tea".ljust(16,'.')+"$3".rjust(4))
