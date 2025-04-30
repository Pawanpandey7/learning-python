#in this program i am going to ask the user to enter the number and i will create a function
#that will decide whether the given number is palindrome or not 
# palindrome is the number that is same when read from the start or the end eg 121 


def is_palindrome(num):
    str_num = str(num)
    rev_num = str_num[::-1]
    return int(rev_num) 

num = int(input("enter the number"))
rev = is_palindrome(num)
if rev==num:
    print("it is palindrome")

else:
    print("it is not palindrome")    


