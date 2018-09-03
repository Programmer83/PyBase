fname = input("FName ? > ")
lname = input("LName ? > ")
age = int(input("Age ? > "))
que = input("Are you a man (y/n) > ")
print(que)
if que == "y":
    ack = "man"
else:
    ack = "women"
print(" Hello, " + lname, fname, ", age",age, "(",ack, ")")
