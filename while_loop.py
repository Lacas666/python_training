# logikai = boolean
# 2 érték lehet: True, False

are_you_a_boy = True
print(are_you_a_boy)
print(type(are_you_a_boy))

is_17_lower_than_15 = False
print(is_17_lower_than_15)

# összehasonlító operator

result = 10 < 20
print(result)

result = 10 > 20
print(result)


result = 10 >= 20
print(result)

result = 10 == 10
print(result)

print("alma" == "korte")




while False:
    print("Hallo Ciklus")  # nem igaz

# végtelen ciklus
#while True:
#    print("hello végtelen")


count = 0
while count < 10:
    print("Hello " + str(count))
    count = count + 1


