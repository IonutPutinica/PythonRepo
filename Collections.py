#tuples, arrays/lists, dictionaries
size=(100,200) #tuple
width=size[0] #width=100
height=size[1] #height=200
print("Tuples:")
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
print() #spacing for readability
print("Lists:")

movement=[5,-2,-3,4,-1]
print(movement) #prints [5,-2,-3,4,-1]
first_movement=movement[0] #first_movement=5, because 5 is the value stored in the first position of the "movement" list
print(first_movement)
movement[0]=7 #sets the value of the first position in the list to 7
first_movement_secondary=movement[0] #the value is 7, because the value stored in the first position of the list is now 7
print(first_movement_secondary) 
movement.append(-5) # adds a -5 at the end of the list
print(movement) #[5,-2,-3,4,-1, -5]
movement.remove(-3) #removes the value -3 from the list || CAREFUL it's not index-based, but value based!, so now, the list will be [5,-2,4,-1, -5]
print(movement)