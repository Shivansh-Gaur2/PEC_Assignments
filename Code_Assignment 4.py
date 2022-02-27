#Question 1
disks = 3  
def tower_of_hanoi(disks, source, spare, target):  #created function 
    if(disks == 1):  
        print(f'Move disk 1 from rod {source} to rod {target}.')  
        return  
    tower_of_hanoi(disks - 1, source, target, spare)  #calling function again 
    print(f'Move disk {disks} from rod {source} to rod {target}')  
    tower_of_hanoi(disks - 1, spare, source, target)  
#source as A, spare as B, and target as C  
tower_of_hanoi(disks, 'A', 'B', 'C') 

#Question 2
from math import factorial
n = int(input("enter number of rows you want:- "))
#by recursive approach
def pascal_triangle(n,length=n):
    if n == 0:
        return
    pascal_triangle(n-1,length)
    # spacing
    print('  '*(length-n), end='')

    #fixing first number as 1
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i
    print()
pascal_triangle(n)

#by iterative approach
for i in range(n):
     for j in range(n-i+1):
         print(end=" ") 
     for j in range(i+1):
         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
     print()

#Question 3
num1 = int(input("Enter your first number:- "))
num2 = int(input("Enter your second number:- "))

Quotient , Remainder = divmod(num1,num2)
print("value of quotient is:- "Quotient)
print("value of remainder is:- "Remainder)
#PART A Check whether it(function/values) is callable or not.
print(callable(Quotient))
print(callable(Remainder))
#Part B Check whether all the values are non zeros or not.
if(Quotient!=0 and Remainder!=0):
    print("All the values are non zeros")
else:
    print("one or both of the value are 0")    
#Part C  Add values (4, 5, 6) to the result and filter out the values which
#are greater than 4.
listc = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]
result = []
for i in range(len(listc)):
    if listc[i] > 4:
        result.append(listc[i])
print("Filtered list:- ", result)      
#Part D Convert the above result into set datatype.
setd = set(result)
print("Converted set:- ",setd)
#Part E Make that set immutable.
sete = frozenset(setd)
print("Immutable Set:- ",sete)
##Part F Evaluate the maximum value from set and find out its hash
#value.
print("Hash value of max value from set is:- ", hash(max(sete)))

#Question 4
class Student:
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num
    def data(self):
        print("Student name is " + self.name + "having roll number " + self.roll_num)
    def __del__(self):
        print("deleting data of ", self.name)    
s1 = Student("shivansh", "21104049")   #creted object
s1.data()#calling method 
del s1

#Question 5
class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary   
#Creating objects
e1 = Employee("Mehak",40000)
e2 = Employee("Ashok",50000)
e3 = Employee("Viren",60000)

e1.salary = 70000
print(f"Updated value of Mehak is:- ",e1.salary)  
 
del e3   
print("Deleted record of Viren")

#Question 6
word_George = input("Enter a word George:- ")
word_Barbie = input("Enter meaningful word barbie:- ")

word_George, word_Barbie = word_George.lower(),word_Barbie.lower()
sorted_wordG,sorted_wordB = sorted(word_George),sorted(word_Barbie)

if(sorted_wordG==sorted_wordB):
    print("Your friendship is true")
else:
    print("Your friendship is fake")
