fname = input("FName ? > ")
lname = input("LName ? > ")
age = int(input("Age ? > "))
que = input("Are you a man (y/n) > ")
print(que)
choise = { 'y': 'man' , 'n': 'woman'}
print(" Hello, " + lname, fname, ", age",age, "(",choise[que], ")")
