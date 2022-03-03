
guess = 0

print("Gondolj egy számra!")

start = 1
end = 10

K_or_N =

while K_or_N_or_N != "E":
    guess = str((start + end) / 2)
    K_or_N = input("a szám amire gondoltál (K)isebb (N)agyobb (E)gyenlő, mint") + str(guess) + " ? - "
    if K_or_N == "K":
        interval_end = guess - 1
    if K_or_N == "N":
        interval_start = guess + 1
print("A gondolt szám a " + str(guess))