# even - páros

i = 6
print(i % 2 == 0)

number = int(input("Adj meg egy számot: "))

if number % 2 == 0:
    print("páros")
else:
    print("páratlan")


number = int(input("születési éved"))
if 1900 <number< 2022 :
    print(2022 - number)
else:
    print("helytelen szül év")
print("end")
