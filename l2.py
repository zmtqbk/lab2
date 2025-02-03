#Python Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)
#True
#False
#False


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#b is not greater than a
  

print(bool("Hello"))
print(bool(15))
#True
#True


x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#True
#True


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#True
#True
#True


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
#False
#False
#False
#False
#False
#False
#False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#False


def myFunction() :
  return True

print(myFunction())
#True


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#YES!
  

x = 200
print(isinstance(x, int))
#True





#Python Operators

print(10 + 5)
#15

x = 5
y = 3

print(x + y)
#8

x = 5
y = 3

print(x - y)
#2

x = 5
y = 3

print(x * y)
#15

x = 12
y = 3

print(x / y)
#4


x = 5
y = 2

print(x % y)
#1

x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2
#32

x = 15
y = 2

print(x // y) #7

#the floor division // rounds the result down to the nearest whole number



x = 5

print(x)
#5

x = 5

x += 3

print(x)
#8

x = 5

x -= 3

print(x)
#2

x = 5

x *= 3

print(x)
#15

x = 5

x /= 3

print(x)
#1.6666666666666667


x = 5

x%=3

print(x)
#2


x = 5

x//=3

print(x)
#1


x = 5

x **= 3

print(x)
#125


x = 5

x &= 3

print(x)
#1

x = 5

x |= 3

print(x)
#7


x = 5

x ^= 3

print(x)
#6


x = 5

x >>= 3

print(x)
#0

x = 5

x <<= 3

print(x)
#40

print(x := 3)
#3


x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3


x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3


x = 5
y = 3

print(x > y)

# returns True because 5 is greater than 3


x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3


x = 5
y = 3

print(x >= y)

# returns True because five is greater, or equal, to 3



x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3


x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10


x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y



x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 3)



"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 ^ 3)



"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""

print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
print(100 - 3 ** 3)

"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""

print(100 + ~3)

"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""

print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

print(100 - 5 * 3)

"""
Subtraction has a lower precedence than multiplication, and we need to calculate the multiplication first.
The calculation above reads 100 - 15 = 85
"""


print(8 >> 4 - 2)

"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2

More explanation:
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


print(6 & 2 + 1)

"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2

More explanation:
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 ^ 2 + 1)

"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5

More explanation:
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

print(6 | 2 + 1)

"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7

More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(5 == 4 + 1)

"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""


print(not 5 == 5)

"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""


print(1 or 2 and 3)

"""
The and operator has a higher precedence than or, and we need to calculate the and expression first.
The calculation above reads: 1 or 3 = 1
"""


print(4 or 5 + 10 or 8)

"""
The or operator has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads: 4 or 15 or 8 = 4
"""


print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""






#Python Lists


thislist = ["apple", "banana", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)
#['apple', 'banana', 'cherry', 'apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
#['apple', 'banana', 'cherry']
#[1, 5, 7, 9, 3]
#[True, False, False]

mylist = ["apple", "banana", "cherry"]

print(type(mylist))
#<class 'list'>

thislist = list(("apple", "banana", "cherry"))
print(thislist)
#['apple', 'banana', 'cherry']





#Python - Access List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#banana


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Yes, 'apple' is in the fruits list
  


#Python - Change List Items
  
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)
#['apple', 'blackcurrant', 'cherry']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']



thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 
#['apple', 'banana', 'watermelon', 'cherry']



#Python - Add List Items

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)
#['apple', 'banana', 'cherry', 'orange']



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#['apple', 'orange', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']




thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) 
#['apple', 'banana', 'cherry', 'kiwi', 'orange']




#Python - Remove List Items


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry']


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry', 'banana', 'kiwi']


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']



thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]





#Python - Loop Lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#apple
#banana
#cherry
  

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#apple
#banana
#cherry
  

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#apple
#banana
#cherry
  


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#apple
#banana
#cherry





#Python - List Comprehension


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#['apple', 'banana', 'mango']



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)
#['apple', 'banana', 'mango']



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
#['banana', 'cherry', 'kiwi', 'mango']



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
#['banana', 'cherry', 'kiwi', 'mango']



newlist = [x for x in range(10)]

print(newlist)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
#['apple', 'orange', 'cherry', 'kiwi', 'mango']









#Python - Sort Lists


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)
#[23, 50, 65, 82, 100]


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']


thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)
#[100, 82, 65, 50, 23]



def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
#[50, 65, 23, 82, 100]



thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)
#['Kiwi', 'Orange', 'banana', 'cherry']


thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)
#['banana', 'cherry', 'Kiwi', 'Orange']


thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 
#['cherry', 'Kiwi', 'Orange', 'banana']




#Python - Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']



thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#['apple', 'banana', 'cherry']



thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#['apple', 'banana', 'cherry']








#Python - Join Lists


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#['a', 'b', 'c', 1, 2, 3]


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#['a', 'b', 'c', 1, 2, 3]






#Python - List Methods
#Python List append() Method
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)
#['apple', 'banana', 'cherry', 'orange']


#Python List clear() Method
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
#[]


#Python List copy() Method
fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)
#['apple', 'banana', 'cherry']


#Python List count() Method
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)
#1


#Python List extend() Method
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
#['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']


#Python List index() Method

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
#2


#Python List insert() Method
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

#['apple', 'orange', 'banana', 'cherry']


#Python List pop() Method
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
#['apple', 'cherry']


#Python List remove() Method
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)
#['apple', 'cherry']


#Python List reverse() Method
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)
#['cherry', 'banana', 'apple']


#Python List sort() Method
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
#['BMW', 'Ford', 'Volvo']








#Python Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry', 'apple', 'cherry')


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#<class 'tuple'>
#<class 'str'>



mytuple = ("apple", "banana", "cherry")

print(type(mytuple))
#<class 'tuple'>





#Python - Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#banana


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#cherry


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])
#('apple', 'banana', 'cherry', 'orange')


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:])
#('cherry', 'orange', 'kiwi', 'melon', 'mango')



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#Yes, 'apple' is in the fruits tuple
  





#Python - Update Tuples
  
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#("apple", "kiwi", "cherry")



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
#('apple', 'banana', 'cherry', 'orange')



thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#('apple', 'banana', 'cherry', 'orange')



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)
#('banana', 'cherry')





#Python - Unpack Tuples


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#cherry


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']



fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#apple
#['mango', 'papaya', 'pineapple']
#cherry




#Python - Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple
#banana
#cherry
  



thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#apple
#banana
#cherry
  




#Python - Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#('a', 'b', 'c', 1, 2, 3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')



#Python - Tuple Methods

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
#2


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
#3





#Python Sets


thisset = {"apple", "banana", "cherry"}
print(thisset)
#{'cherry', 'banana', 'apple'}
# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.




thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#{'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#{'cherry', 'apple', 'banana'}
#{1, 3, 5, 7, 9}
#{False, True}



thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
#{'banana', 'apple', 'cherry'}




#Python - Access Set Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#banana
#cherry
#apple
  


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#True







#Python - Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#{'apple', 'cherry', 'banana', 'orange'}



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}



thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}





#Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#{'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal
#cherry
#{'apple', 'banana'}



thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#set()





#Python - Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#cherry
#apple
#banana
  


#Python - Join Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#{'b', 'c', 'a', 2, 1, 3}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#{2, 1, 'b', 'a', 'c', 3}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#{'b', 2, 'a', 3, 'c', 1}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#{'apple'}


set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#{'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)
#{'apple'}


set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)
#{'banana', 'cherry'}



set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#{'banana', 'cherry'}



set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)
#{'google', 'banana', 'microsoft', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)
#{'google', 'banana', 'microsoft', 'cherry'}


set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)
#{'google', 'banana', 'microsoft', 'cherry'}





#Python Dictionaries

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Ford


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
#3


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
#{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#<class 'dict'>


thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict) 
#{'name': 'John', 'age': 36, 'country': 'Norway'}

#Python - Access Dictionary Items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#Mustang




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#dict_keys(['brand', 'model', 'year'])



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
#dict_values(['Ford', 'Mustang', 1964])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Yes, 'model' is one of the keys in the thisdict dictionary
  


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}






#Python - Add Dictionary Items


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}





#Python - Remove Dictionary Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#{'brand': 'Ford', 'year': 1964}

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang'}



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#{}





#Python - Loop Dictionaries

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
#brand
#model
#year
  

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
#Ford
#Mustang
#1964
  

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#brand Ford
#model Mustang
#year 1964
  


#Python - Copy Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



#Python - Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
#Tobias


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

#child1
#name: Emil
#year: 2004
#child2
#name: Tobias
#year: 2007
#child3
#name: Linus
#year: 2011
        






#Python If ... Else
        


a = 33
b = 200

if b > a:
  print("b is greater than a")
#b is greater than a
  

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#a and b are equal


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#a is greater than b



a = 200
b = 33

if a > b: print("a is greater than b")
#"a is greater than b"


a = 2
b = 330

print("A") if a > b else print("B")
#B


a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
#=


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#Both conditions are True
  

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#At least one of the conditions is True
  


a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#a is NOT greater than b
  

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Above ten,
#and also above 20!
    

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement





#The while Loop


i = 1
while i < 6:
  print(i)
  i += 1
#1
#2
#3
#4
#5
  

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
#1
#2
#3


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result
#1
#2
#3
#4
#5
#6
  

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#1
#2
#3
#4
#5
#i is no longer less than 6
  






#Python For Loops
  


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
#apple
#banana
#cherry
  

for x in "banana":
  print(x) 
#b
#a
#n
#a
#n
#a
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#apple
#banana
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#apple
#cherry
  


for x in range(2, 30, 3):
  print(x) 
"""2
5
8
11
14
17
20
23
26
29"""


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.
#0
#1
#2
  


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
"""
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""


for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement
