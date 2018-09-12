num_list = input("enter list of numbers:> ")
num_list = num_list.split()

res = 0

res = sum(int(i) for i in num_list)

print("list : ", num_list)
print("sum :", res)