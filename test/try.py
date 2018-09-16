# try:
#     num = input("number: ")
#     new = float(num)
# except ValueError as e:
#     print (e)
# else:
#     print ("number Pi : ", new)

a=input()
try:
    print (float(a))
except ValueError:
    print (bool(a))
