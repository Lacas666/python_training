
name = "john doe"

print(name.upper())
print(name.lower())

print(name)

# immutable - a string módosíthatatlan

for c in name:
    print(c)

print(len(name))

# szeletelés - slicing
print(name[2:5]) # substring
print(name[2:])
print(name[:6])
print(name[0:7:2])
print(name[::-1]) # visszafelé


print("alma" == "alma")
print("alma" == "korte")
print("alma" > "korte")

print("a" in "alma")
print("la" in "alma")




