list1 = ["A", "B", "C", "D", "E", "F"]

print(list1)
print(type(list1))

list2 = ["Hello", 15, 1.77, False, ["Celiber", "Fish"], ("Tuples"), [], list()]

print(list2)
print(type(list2))
print(list1[0]) # Index
print(list1[-1]) # Index from last
print(list2[4][0]) # index nasted list
print(list2[4][-1]) # index nested list from last





# changing a value

list1[0] = "X"
print(list1) # here we see list1[0] has been changed

# Deleting a value (using del function)

del list1[0]
print(list1) # here we see list1[0] has been deleted





# insert a value in a list

list1.insert(0, "A")
print(list1) 

del list1[0]
print(list1) # deleting again

# combained a list + list

list1 = ["A"] + list1
print(list1)




# append a value

print("=======")

list1.append("G")
print(list1) # append do, add value in end of the list

# using built-in function (max,min)

print(max(list1)) # printing the maximum value in the list
print(min(list1)) # printing the minimum value in the list





# index number

print(list1.index("E")) # printing the index number of a value
print(list1[list1.index("E")]) # This line prints the element "E" from the list list1 by finding its index and accessing it directly.






# reverse the list

list1.reverse()
print(list1) # we can print also the reverse version of a list





# slice notation

list1 = list1[::-1]
print(list1)





# counting

print(list1.count("A"))
list1.append("A")
list1.append("A")
	# addnig more "A" for verifying that it is counting or not
print(list1.count("A"))






# pop method

list1.pop()
list1.pop()
list1.pop()
list1.pop()
	# it pop out / delete the end index of the list
print(list1)








# extend method

list3 = ["H", "I", "J"]
print(list3) 

list1.extend(list3)
print(list1) # extended the list3 in list1





# clear 

list1.clear() 
print(list1) # we can also clear all values of a list







# sort a list

list4 = [4, 8, 67, 17, 2, 9]

list4.sort()
print(list4) # print small to large number

# reverse the sort
# we want to print list4 in large to small in technical way
list4.sort(reverse=True)
print(list4) # print large to small number
	# Also worked in string
	# list1.sort(reverse=True)
	# print(list1)

print("=====") # printing this for better output








# aliasing
list5 = list4 
	# list5 doesn't create a new copy of list4
	# it only creates another reference to the same list.
	# means if we changes on list5 then it auto change in list4
print(list4)
print(list5)

list5[2] = "77"
	# it also affects list4 because both 
	# list4 and list5 point to the same list in memory.
print(list4)
print(list5)

print("=====") # printing this for better output








# copy
list6 = list4.copy() 
	# This way, modifying list6 won't affect list4.
print(list6)
print(list4)

list6[2] = "ABCD"
print(list6)
print(list4)







# shallow copy

x = ["A", "B", "C"]
y = x[:]
	# creates a shallow copy of x. 
	# This means that y becomes a new list with the same elements as x, 
	# but it's a different object in memory.

y[1] = "E"
print(x)
print(y)






# slicing

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

down = areas[:6] # takes the first 6 elements from the areas list.
up = areas[6:] # takes all elements from index 6 to the end of the list.

print(down)
print(up)
