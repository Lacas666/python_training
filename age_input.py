number = int(input("születési éved"))
minimum_year = 1900
actual_year = 2022

if minimum_year <number< actual_year :
    print("életkorod: " str(actual_year - number))
else:
    print("helytelen szül év")
print("end")
