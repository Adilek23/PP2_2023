fruits = ["orange", "apple", "banana"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)