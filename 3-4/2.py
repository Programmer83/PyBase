var = input("input fac number> ")

if var >= 0:
    fact = 1
    while var > 0:
        fact = fact * var
        var = var - 1

    print("fact is: ", fact)
else:
    print("Cannot count")