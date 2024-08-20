#Словари
my_dict = {'mother' : 1973, 'father' : 1971, 'Oleg' : 2000, 'Katya' : 2003}
print(my_dict)
print('mother')
my_dict['Maya'] = 2005
print(my_dict['Maya'])
my_dict.update({'Grandmother' : 1953,
                'Grandfather' : 1950})
print(my_dict)
del my_dict['mother']
print(my_dict.get('mother'))
print(my_dict)

#Множества
my_set = {2.17,4,6,8, False, ('cat', 'dog')}
print(my_set)
my_set.update({'red', 'black'})
print(my_set)
my_set.remove(('cat', 'dog'))
print(my_set)