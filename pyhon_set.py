# A set is a collection which is unordered, unchangeable*, and unindexed.
# set items are unchangeable, but you can remove items and add new items.
# Sets cannot have two items with the same value.

thisSet = set(("apple", "banana", "cherry", "cherry"))

for item in thisSet:
    print(item)


# add set items

# add items
thisSet.add("mango")
print(thisSet)

# add set

tropical = {"pineapple", "mango", "papaya"}

thisSet.update(tropical)

print(thisSet)

# Add Any Iterable
myList = ["kiwi", "orange"]

thisSet.update(myList)

print(thisSet)

# remove items from set

thisSet.discard("mango")
print(thisSet)


# looping set same as looping a list

# set join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x.symmetric_difference_update(y)

print("symmetric_difference_update", x)
