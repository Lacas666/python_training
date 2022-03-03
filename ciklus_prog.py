# program bekérdezi a nvedet
# bekérdezi háynszor írja kia
# írja ki
# írja a neve elé a sorszámot



name = input("Add meg a neved:")
number = input ("Hányszor írjam ki?")
for i in range(0,int(number)):
    print(i + 1, name)


for i in range(1, number + 1):
    print(i, name)