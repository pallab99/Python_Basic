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
