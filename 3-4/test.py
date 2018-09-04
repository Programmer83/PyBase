i = int(input("input fact> "))

fact = 1
while i > 0:
    fact *= i
    i -= 1

print("fact is: ", fact)