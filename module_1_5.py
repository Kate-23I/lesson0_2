one_var = 23
two_var = 23.3
three_var = True
four_var = 'Four'
five_var = [1, 2, 3, 4]

immutable_var = (23, 23.3, True, 'Four', [1, 2, 3, 4])
print(immutable_var)

#immutable_var[0] = 7 # неизменяемый тип данных

mutable_list = (['с'], 'п', 'и', 'с', 'о', ['к'])
print(mutable_list)
mutable_list[0][0]= 's'
mutable_list[-1][0] = '!'
print(mutable_list)

immutable_var[4][1] = 8
print(immutable_var)
