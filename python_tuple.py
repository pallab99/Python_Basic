# Once a tuple is created, you cannot change its values. Tuples are unchangeable,
# or immutable as it also is called.

# add items to the tuple
thisTuple = ("apple", "banana", "cherry")
newList = list(thisTuple)
newList.append("mango")
thisTuple = tuple(newList)
print(thisTuple)

# add tuple to tuple
y = ("orange",)
thisTuple += y
print(thisTuple)


# as tuple are unchangeable but we can change it by converting them to list  and then converting
# them back into tuple

# update tuple
copyTupleToList = list(thisTuple)
copyTupleToList[2] = "updated fruit"
thisTuple = tuple(copyTupleToList)
print("updated tuple", thisTuple)

# delete items form tuple
copyTupleToList1 = list(thisTuple)
copyTupleToList1.pop(2)
thisTuple = tuple(copyTupleToList1)
print("updated tuple", thisTuple)


# unpacking the tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable
# name and the values will be assigned to the variable as a list:
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)

# looping tuple same as looping a list

# joining a tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1+tuple2
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
multiply = tuple3*3
print(tuple3)
print(multiply)
