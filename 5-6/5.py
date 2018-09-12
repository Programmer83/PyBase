enter_length = input('Enter length: ')
if enter_length.isdigit() or (enter_length.startswith('-') and enter_length[1:].isdigit()):
    enter_length = int(enter_length)
    if enter_length >= 80:
        print("\033[1;31;48mError: Length must be less then 80!!! \n")
    elif enter_length < 0:
        print("\033[1;31;48mError: Length only positive number!!! \n")
    else:
        stars = enter_length * '*'
        enter_type = int(input('Enter type: '))
        for length in range(enter_length):
            if enter_type == 1:
                print(stars[:enter_length - length])
            if enter_type == 2:
                print(stars[:length + 1] + ' ' * ((enter_length - 1) - length))
            if enter_type == 3:
                print(' ' * ((enter_length - 1) - length) + stars[:length + 1])
            if enter_type == 4:
                print(' ' * length + stars[length:])
else:
    print("\033[1;31;48mError: Length must be integer!!! \n")