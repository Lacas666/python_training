
print("gondolj egy számra")

min_guess = 1
max_guess = 10
answer = "x"
guess = 5
while answer != "e":
    guess = (min_guess + max_guess) // 2
    print("A tippem", guess)
    answer = input("k/e/n?")
    if answer == "k":
        max_guess = guess - 1
    elif answer == "n":
        min_guess = guess + 1
print("a gondolt szám", guess)


