
# kérd be a felhasz, hány számot szeretnél megadni
# kérj be tőle pont annyi számot mint amit megadott
# összegezzük a felhasz általá megadott csak pozitiv számokat


sum = 0
count = int(input("hany szamot szeretnel megadni? "))
for i in range(0, count):
    number = int(input("Adj meg egy szamot: "))
    if number > 0:
        sum += number
print("A szamok osszege", sum)


# MEGOLDÁS 2

count = int(input("hany szamot szeretnel megadni? "))
for i in range(count):
    number = int(input("Add meg a " + str(i + 1) szamot: "))
    print("A megadott szam:, ")




