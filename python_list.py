from typing import List
thisList: List[str] = ["apple", "pineapple", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisTuple = ("kiwi", "orange")
thisList.insert(2, "mango")  # insert mango at position 2
thisList.append("orange")  # insert at the end of the list
# extent the list
thisList.extend(tropical)
thisList.extend(thisTuple)

print(thisList)

# remove items from the list
thisList1 = ["apple", "banana", "cherry", "banana", "kiwi"]
print("before", thisList1)

thisList1.remove("banana")
thisList1.pop(3)
print("after", thisList1)

# looping

# for in loop
for i in thisList1:
    print("for in loop", i)

# range loop
for index, value in enumerate(thisList1):
    print("enumerate loop", {value, index})


# sort list

newList = [3, 4, 56, 2, 10, 34]
print("Before sort", newList)
# newList.sort()
newList.sort(reverse=True)
print("After sort", newList)
