print(5*6)
print(5+6)
print(3/2)
print(3-2)
print(5*6+12)
print(1+2*3)
print((1+1)*3)

print("alma"+"korte")  # konkatenálás

# string + int
#print(fruit+5) # TypeError: can only concatenate str (not "int") to str
# int + string
#print(5+alma)
# string - string
#print("alma" - "korte") # nem támogatott
# string * string # nem támogatott

# string * int
print("alma" * 5)


result = 6*5+2
print(result)

number_of_apples_per_basket = 5
number_of_basket = 3
number_of_all_apples = number_of_apples_per_basket * number_of_basket
print(number_of_all_apples)


name = "John Doe"
message = " A name valtozo tipusa:" + str(type(name))
print(message) # TypeError: can only concatenate str (not "type") to str

# stringé knovertálás

print("Az almak szama:" + str(5))

# a kifejezések végrehajtása : kiértékelés


print(len("hello"))
length_of_hello = len("hello")
print(length_of_hello)


# változó - hours 3
# változó - minutes
# üzenet:


hours = 3
minutes = hours*60
print(str(hours) + " óra az " + str(minutes)+ " perc")


#hozzatok létre egy word nevu változót és adjatok neki értékül egy nagyon hossuú szót
# számoljátok ki ennek a hosszát
# kiírni : hosszu szó pontosan hány karakter


word = "nagyonhosszúszó"
print("A " +word+"pontosan " +str(len(word)) + " karakter hosszú")

print(5//2) # ötben a kettő
print(5%2) # maradék 1


