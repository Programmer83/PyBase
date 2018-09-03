var1 = input("Variable1 > ")
var2 = input("Variable2 > ")

print("Var1", var1, "Var2", var2)

mid = var1
var1 = var2
var2 = mid
del mid

print("Var1", var1, "Var2", var2)