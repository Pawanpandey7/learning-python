# what does the calculator does is perform addition, subraction , multiplications and division
#now i need to create a program that can perform the operation
# first of all the calculator ask what operation why need to perform 


tem = input("what operation you want to perform: type a for addition, s for subraction, m for multiplication and d for division: ")
if tem=='a' or tem =='A':
    a= int(input("enter the first  number: "))
    b= int(input("enter the second number: "))
    c=a+b
    print("Sum: ",c )

if tem=='s' or tem=='S':
    a= int(input("enter the first number: "))
    b= int(input("enter the second number: "))
    print("difference: ",a-b)

if tem=='m' or tem=='M':
    a= int(input("enter the first number: "))
    b= int(input("enter the second number: "))
    print("Multiplication: ",a*b)

if tem=="d" or tem=="D":
    a= int(input("enter the first number: "))
    b= int(input("enter the second number: "))
    print("division: ",a/b)

