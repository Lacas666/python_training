
# függvény definiciója
def print_employee_data(name, age):  # paraméterek megadása, változók
    """az a függvény kiírja az alkalmazott nevét és életkorát"""
    # DRY - dont repeat yourself
    print("az alkalmazott neve", name)
    print("az alkalmazott eletkora", age)
    # a függvény végén a paraméterek törlődnek, nincs többé name és age

print_employee_data("John", 10)  # függvény hívás, paraméter értékek megadása kötelező
# az átműsolás sorrenben történik - sorrendi kötés
print_employee_data("Jack", 30)
print_employee_data("Jane", 40)

def a_ket_szam_osszege (number1, number2):
    print(number1+number2)

a_ket_szam_osszege(5,5)


# sum list függvény, paraméterül kap egy listát
# kiírja a konzolra a listában szereplő összeget
numbers = [1,2,5,8]

def sum_list(data):
    sum = 0
    for numbers in data:
        sum += numbers
    print("Lista összege:", sum)


sum_list(numbers)

print("end")

