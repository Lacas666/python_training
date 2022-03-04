
# hozz létre egy is_even nevű függvényt
# amely Trut-t ad vissza ha a paraméterként megadott érték páros, egyéb esetlben False

def is_even (value):
    if value % 2 == 0:
        return True
    else:
        return False


# vagy
def is_even (value):
    return value % 2 == 0

print(is_even(5))
print(is_even(4))

# Hozz létre egy is_even nevű függvényt,
# amely True-t ad vissza, ha a paraméterként megadott
# érték páros, egyéb esetben False-t adjon vissza
# Szorgalmi
# Hozz létre egy sum_negatives függvényt, mely paraméterül kap egy listát,
# és összegzi a benne szereplő negatív számokat, és azzal tér vissza


def sum_negatives(numbers):
    result = 0
    for number in numbers:
        if number < 0:
            result += number
    return result

print(sum_negatives([-1, 3, 5, -6, 1]))


# Szorgalmi
# Hozz létre egy to_minutes függvényt, mely paraméterül megkapja
# az órák számát, és visszatér a percek számával

def to_minutes(hours)
    return hours * 60


print(to_minutes(1))
print(to_minutes(3))

# Szorgalmi
# Hozz létre egy input_number függvényt, melynek legyen egy
# paramétere. A függvény bekér a felhasználótól egy szöveget
# a paraméterrel megadott szöveggel, számmá konvertálja és azt adja vissza

def input_numbers(message):
    return int(input(message))

value = input_number("adj meg egy számot")
print(type(value))


# Szorgalmi
# Írjatok egy annotate_every_even_number függvényt, mely kap egy
# számok listáját, és kiírja őket egymás alá, de minden másodikat
# egy karakterrel beljebb ír ki


def annotate_every_even_number(numbers):
    counter = 1
    for number in numbers:
        print(number)

annotate_every_even_number([4,7,6,3,6,9])

# Írj egy concatenate_shorts függvényt, mely paraméterül kap szavak listáját
# és csak a 3 karakternél rövidebb szavakat fűzze össze egy stringbe,
# és ezt adja vissza

def concatenate_shorts(words)
    result = ""
    for word in words:
        if len(word) <= 2:
            result += word + ","
    return result

print(concatenate_shorts("alma" , "korte", "cseresznye" , "egy", "az", "xy"))