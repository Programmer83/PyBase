# f1 = open("file.txt", "r")
# s = f1.readlines()[::-1]
# f1.close()
# f2 = open("file2.txt", "w")
# f2.writelines(s)
# f2.close()

#
# flist = list(range(0,101))
# print (flist)
# fw = open("file3.txt", "w")
# for item in flist:
#     fw.write(str(item)+',')
# fw.close()


flist = list(range(0,101))
print (flist)
fw = open("file3.txt", "w")
nlist = ','.join(str(item) for item in flist)
fw.write(nlist)
fw.close()