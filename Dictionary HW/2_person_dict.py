person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

# print out the name of the second child
print(person["children"][1])

# print out the name of the cat
print(person["pets"]["cat"])


# use a loop to print out the names of each child
for kid in person["children"]:
    print(kid)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
for pet_type, pet_name in person["pets"].items():
    print(f"The type of pet is: {pet_type} and the name of the pet is: {pet_name}")