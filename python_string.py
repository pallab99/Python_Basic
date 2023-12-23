aaa="hello world"
# print(aaa[2:4])  #character from position 2 to 4
print(len(aaa))

multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

words = aaa.split(" ")
for word in words:
    print(word,end=" ")

if "Lorem" in multiline_string:
    print("lorem present")

if "World" not in multiline_string:
    print("world not present")

#Slicing string
print("Slicing string")
name="Pallab Majumdar"
print(name[2:5]) #Get the characters from position 2 to position 5 (not included)
print(name[:5])  #Get the characters from the start to position 5 (not included)
print(name[2:])  #Get the characters from position 2, and all the way to the end:
print(name[-5:-2])

#modify string
print(name.upper())
print(name.lower())
print(name.replace("a","e"))

#string Concatenation

first_name="Pallab"
last_name="Majumdar"
full_name=first_name+" "+last_name
print(full_name)

#string format

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

