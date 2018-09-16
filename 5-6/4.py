dict_of_degrees = {}
enter_number = int(input('Enter number: '))

list_of_degree = [2, 3, 4]
list_of_numbers = list(range(1, enter_number + 1))

for numb in list_of_numbers:
    dict_of_degrees[numb] = {x: numb**x for x in list_of_degree}
print(dict_of_degrees)