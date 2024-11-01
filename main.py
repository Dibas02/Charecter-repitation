st1 = input("Enter a string: ")
ch = input("enter the charecter you want to search for: ")
counter = 0

for c in st1:
    if c == ch:
        counter = counter+1

print(counter)