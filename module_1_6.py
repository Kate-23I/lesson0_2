my_dict = {'Sofa': 2001, 'Rada': 1998, 'Peter': 2003}
print('Dict:', my_dict)

print('Existing value:', my_dict['Rada'])
print('Not existing value:', my_dict.get('Alice'))

my_dict['Alice'] = 2007
print('Non-existent added value:', my_dict['Alice'])

my_dict.update({'Tom': 1998, 'Gloria': 2002})
a = my_dict.pop('Sofa')

print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set_ = {1, 2, 2, 3, 4, 4, 5, True, 'word', 1.5}
print('Set:', my_set_)

my_set_.add(6)
my_set_.add(7)
my_set_.remove(2)

print('Modified dictionary: ', my_set_)

