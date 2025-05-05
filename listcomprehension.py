#1. square all the numbers
#2. Filter even numbers
#3. convert to uppercase
#4. for a list of odd and even numbers, generate even for even numbers and odd for odd numbers
#5. generate a list from a scratch

list01 = [1,2,3,4,5]
print(list01)
list02 = [x**2 for x in list01]
print(list02)

list03 = [x for x in list01 if x%2==0]
print(list03)

list2 =["pawan","oli","bhandari"]
#converting to the uppercase
list04 = [x.upper() for x in list2 ]
print(list04)

list05 = ["even" if  x%2==0 else "odd" for x in list01]
print(list05)

# generating a list from a scratch 
list06= [x**2 for x in range(1,10)]
print(list06)
