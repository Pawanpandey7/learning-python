# here i will show the difference between the list and the tuple

list = [1,2,3,4,5] # it is the list. we can modify it

tup = (1,2,3,4,5) # this is tuple we cannot make changes to it

# one of the feature of the tuple is that we can insert tuple within a tuple
tup2 =(1,2,(3,4),5)

# also we can define tuple like this:

tup3 = 1, 2, 3

#let me see if i can access the elements of the tuple

print(tup[0])
print(tup2[2][0])

#dictionary

dict = {
    "name": "Pawan pandey",
    "age": 23,
    "hobby": "coding"
}
# we can add data to the dictionary by 
dict["course"] = "BIT" 

# we can modify the dictionary by 
dict["hobby"]="singing"

#we can delete the data from the dictionary by 
del dict["age"]

# set

#it is the unordered data structure
# we cannot index it like list and tuple
# there should be no repetition
#it can be modified

set1 = {1,2,2,3,4,5}
print(set) #output {1,2,3,4,5}

# we cannot access a element of the set by using set1[0] like the list and tuple



