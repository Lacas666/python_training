
def calcilate_sum (a, b):  # formális paraméter
    return a + b


print(calcilate_sum(6,8))  # aktuális paraméter

# függvényhíváskor, az aktuális paraméterek értékeit - legyen ez csak literál, változó név stb.. - átmásolja a formális paraméterekbe

result = calcilate_sum(1,2)
print(result)

print(6 + calcilate_sum( 7,9))
print(calcilate_sum(1+2, 3+4))


print(calcilate_sum(len("alma"), calcilate_sum(10, 7+2)))