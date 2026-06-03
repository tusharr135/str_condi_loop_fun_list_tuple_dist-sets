print("Hello, World!" + " This is a code execution example.")

#strings, conditional statements, loops, functions, lists, tuples, dictionaries, sets

#strings

str="tushar"
print(str.upper())
print(str.lower())
print(str.title())
print(str.find(str))
print(str.replace("tushar","raut"))
print(str.count(str))
print(str.endswith(str))

#escape sequences
print("hello \n world")
print("hello \t world")
print("hello \\ world")
print("hello \' world")
print("hello \" world")

#mini projec emoji converter

msg=input("enter the msg")
msg=msg.replace(":)", "😊")
msg=msg.replace(":(", "😒")
print(msg)

#conditional statements
age=18
age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
    
marks=int(input("enter your marks"))
if marks>=90:
    print("grade a")
elif marks>=80:
    print("grade b")
elif marks>=70:
    print("grade c")
elif marks>=60:
    print("grade d")        
else:    print("grade f")   


#Write a Python program that takes a number as input and prints:
#“Positive” if number > 0
#“Zero” if number == 0
#“Negative” if number < 0

#num=float(input("enter a number"))
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


#list in python
food=["apple","mongo","banana"]
print(len(food))
print(max(food))
print(min(food))
food[0]="tushar"
print(food)
print(food[1:2])  #slicing list


#tuple
tuple=("apple","orange","grapes","mango","kiwi")
print(tuple)
print(len(tuple))
print(tuple.index("apple"))

#3 favorite movies and store in list

movie1=input("enter movie1")
movie2=input("enter movie2")
movie3=input("enter movie3")

movielist=[movie1,movie2,movie3]
print(movielist)

#tuple of marks

marks=(87,44,33,22,66)
print(marks)
print(max(marks))
print(min(marks))

#dictionary in python

students={
    "name":"tushar",
    "age":22,
    "city":"mumbai"
}
print(students["name"])

students["rollno"] = 33
print(students)

#Create a dictionary named marks to store marks of 3 subjects. Add the subjects one by one and print the final dictionary. 

marks={
        "eng":44,
        "math":49,
        "sci":30
 }
print(marks)

#sets in python

languages={
    "c++","python","c++","react"
}
print(type(languages))

#You are given a list of programming languages:
#["Python", "Java", "C++", "Python", "Java", "C"]
#Convert it into a set and print how many unique languages Divya knows.

programming =["Python", "Java", "C++", "Python", "Java", "C"]
programmingset=set(programming)
print(programmingset)
print(len(programmingset))

#Mini Assignment
#Create a dictionary storing meanings of 3 English words.
dictionary={
  "bad":"waste",
  "device":"phone",
  "apple":"fruit"
 }
print(dictionary)

#Create a set of numbers and show union and intersection with another set.
set1={1,2,3,4,5,6}
set2={2,4,6,8,10,12}

print(set1.union(set2))
print(set1.intersection(set2))

#Try to add both integer 9 and float 9.0 to a set and observe what happens.
a=9
b=9.0
c=a+b
print(c)
print(set[c])

#LOOPS IN PYTHON

from doctest import Example



#Write a program that prints the sum of first n natural numbers.
#For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.
#(Hint: Keep a running total inside the loop.)


n=10
while (n>=1):
    sum=sum+n
    n=n-1
print(n)

#countdown for everythings
import time
count=int(input("enter the nummber"))
for i in range(count,0,-1):
    print( i)
    time.sleep(1)
print("heyyy done for the day")