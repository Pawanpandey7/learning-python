str = "pawan"

#string manipulation

#access the first element of the string
print(str)

print("first element of the string")
print(str[0])

print("print upto first 3 element of the string")
print(str[:3])

print("last two element of the string")
print(str[2:])

print("count the number of words in the string")
num = len(str)
print(num)

str2="my name is pawan pandey"
word_count=len(str2.split())
print(f"the number of words in {str2} is {word_count}")
