import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)



print()
print('*****  end section 1 ********')
print()


'''


print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}")
else:
    print(f"{name} is not found in the phonebook.")






print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

phonebook['Chris'] = '555-5454'  # Edit Chris
phonebook['Jake'] = '555-9999'   # Add entry for Jake
print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook['Chris']  # Remove Chris 
print(phonebook)



print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()






print()
print('*****  end section 5 ********')
print()

print("Keys:")
for key in phonebook:
    print(key)

print("Values:")
print()
for value in phonebook.values():
    print(value)

print("Items:")
print()
for key, value in phonebook.items():
    print(f"{key}: {value}")



print()
print('*****  start section 6 - using get and clear ********')
print()

print(phonebook.get('Katie', 'Not Found'))
print(phonebook.get('Chris', 'Not Found'))

phonebook.clear()  
print(phonebook)




print()
print('*****  end section 6 ********')
print()




print()
print('*****  start section 7 - using pop method ********')
print()

phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
removed_value = phonebook.pop('Joanne', 'Not Found')
print(f"Removed Joanne's number: {removed_value}")
print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
last_item = phonebook.popitem()
print(f"Item Removed : {last_item}")
print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
keys_list = list(phonebook.keys())
random_key = random.choice(keys_list)
print(f"Randomly selected key: {random_key} with value {phonebook[random_key]}")




print()
print('*****  end section 9 ********')
print()


'''





