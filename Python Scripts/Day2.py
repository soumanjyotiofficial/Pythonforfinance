
## String Manipulation


name = "Charter Finance Institute"

"""
1. Remember index start from 0  so to get the C from the variable name we use name[0].
2. If we want to print t from the varable name we will use name[4].
3. If we want to print last 10th character we will use name[-10] it is the best practice.
I know you are thinking something that is might be possible
4. Let say you want to print all character beyond the 4th caracter including 4th one we use will use name[4:]
5. Let say you want to print all the character beyond the last 10 th character we will use name[-10:]  
6. Let say you want to print character from h to e we will use i to i+1 (i=index) analogy name[1:6] 
you will get the out put "harter" >>> if you get confuse we get the out put upto 5th index(i) that way we 
used the analogy of upto i+1 index.

"""
#1
print(name[0])
#2
print(name[4])
#3
print(name[-10])
#4
print(name[4:])
#5
print(name[-10:])

#6
print(name[1:6])


"""
let say we want to perfrom sentance casing 
1. upper  case every character >>> name.upper()
2. lower case every character >> name.lower()
3. capitalize each character >> name.capitalize()
4. To First Character of every workd we use name2.title()
"""

print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())
name2 = name.capitalize()
print(name2.title())


# Other topics
"""
Few other method of string
Getting the position any character
1. name.index('a') here >> 'a' is the character whose index we are  finding
  

"""
#1
print(name.index("a"))



