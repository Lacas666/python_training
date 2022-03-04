
# függvény paraméter három egész szám,
# true ad vissza ha számok szigoruan novekvő sorrendben vannak
# ellenkező esetben false

def is_ascending(a: int,b: int,c: int):
    if a < b < c:
        return True
    else:
        return False
print("end")

print(is_ascending(2,3,4))

# Írj egy word_concat függvényt, mely két szót kap
# paraméterként, és visszaadja őket összefűzve úgy,
# hogy a rövidebb legyen elől
# "alma", "korte" -> "almakorte"
# "cseresznye", "meggy" -> "meggycseresznye"

def word_concat(a: str,b: str):
    if len(a) < len(b):
        return a+b
    else:
        return b+a

print(word_concat("alma", "korte"))


