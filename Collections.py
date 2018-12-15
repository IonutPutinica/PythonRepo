#tuples, arrays/lists, dictionaries
size=(100,200) #tuple
width=size[0] #width=100
height=size[1] #height=200
print(width)
print(height)
print(size)
new_size=size+(300,) #new_size=(100,200,300)
print(new_size)
#to delete a tuple , use the keyword del -> del new_size
len(size) #2
max(size) #200
min(size) #100
print(len(size))
print(max(size))
print(min(size))

does_contain= 100 in size #value should be true, because we do have the value 100 in the size tuple
print(does_contain) #returns true
