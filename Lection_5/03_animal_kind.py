animal_kind = input()

if animal_kind == 'dog':
    print('mammal')
elif animal_kind == 'crocodile' or animal_kind == 'tortoise' or animal_kind == 'snake':
    print('reptile')
else:
    print('unknown')