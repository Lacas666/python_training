# Írjatok egy get_max nevű függvényt,
# aminek paraméterül át lehet adni két
# lebegőpontos számot, és adja vissza a
# kettő közül a nagyobbat!

def get_max(a: float,b: float) -> float:
    if a > b:
        return a
    else:
        return b


print("A nagyobb szám:", get_max(3.4, 5.6))
print("A nagyobb szám:", get_max(12.5, 7.2))
print("A nagyobb szám:", get_max(10, 10))

# Írjatok egy beszédes print_square függvényt,
# ami paraméterül kap két egész számot.
# Rajzoljon ki egy ekkora téglalapot, csillagokból.
# 7, 5
#
# *******
# *     *
# *     *
# *     *
# *******

def print_square(width: int, height: int) -> None:
    full_row = width * "*"
    print(full_row)
    center_row = "*" + (width - 2) * " " + "x"
    for i in range (0, height - 2):
        print(center_row)
    print(full_row)

print_square(10,6)

# Írjatok egy függvényt, ami paraméterül megkapja
# a szavak listáját, és visszaadja ezeket összefűzve,
# de mindegyiket gondolatjel között.
# ["alma", "korte", "meggy"]
# "-alma--korte--meggy-"

def star(words):
    sum_word = ""
    for word in words:
        sum_word += "-" + word + "-"
    return sum_word

print(star(["alma", "korte", "malna"]))