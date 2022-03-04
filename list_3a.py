
# írj egy függ. paraméterül kap egy listát amiben nevek vannnak
# és visszaadegy másik listát amiben a nevek Johnnal kezd
# szűrés - filter

# ["John Smith" , "Jane Smith" , "Jack Smith", "John Doe"]
#

def pick_johns(names_list):
    johns_list = []
    for name in names_list:
        if "John" in name:
            johns_list.append(name)
    return johns_list


def filter_johns(names: list) -> list:
    result = []
    for name in names:
        if "John" in name and name.index("John") == 0:
            result.append(name)
    return result

print(filter_johns(["John Smith" , "Jane Smith" , "Jack Smith", "John Doe"]