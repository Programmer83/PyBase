word = input("Please input string:> ")

step = int(input("what is the step:> "))

start = 0
for letter in word:
    print(word[start::step])
    start = start + 1
