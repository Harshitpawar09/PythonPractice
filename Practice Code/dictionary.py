# dictionary = {
# "cat" : "chat",
# "dog" : "chien",
# "horse" : "cheval"
# }
# phone_number = {'boss': '123-456-7890', 'Suzy': '987-654-3210'}
# empty_dict = {}
# print(dictionary)
# print(type(dictionary))
# print(phone_number)
# print(type(phone_number))
# print(empty_dict)
# print(type(empty_dict))

# # print(dictionary['cat'])
# # print(phone_number['boss'])
# # print(phone_number['president']) # KeyError: 'president' not found in phone_number


# words = ['cat', 'lion', 'horse']
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, " is not in dictionary")


# print(dictionary.keys())
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])


# print(dictionary.items())
# for key, value in dictionary.items():
#     print(key, "->", value)


# print(dictionary.values())
# for value in dictionary.values():
#     print(value)



#Copying a dictionary

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# print("pol_eng_dictionary:", pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()
# print("copy_dictionary:", copy_dictionary)


# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary.pop("zamek")
# print(item)


# phonebook ={}
# print(phonebook)
# phonebook["boss"] = "123-456-7890"
# print(phonebook)
# del phonebook["boss"]
# print(phonebook)



#Pop Item

# pol_eng_dictionary = {"kwiat": "flower"}
# pol_eng_dictionary.update(
#     {"gleba": "soil"
#     })
# print(pol_eng_dictionary)
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)


# pol_eng_dictionary = {
#     "zamek" : "castle",
#     "woda" : "water",
#     "gleba" : "soil"
# }
# if "zamek" in pol_eng_dictionary: 
#     print("Yes! zamek is present in the Dictionary")
# else:
#     print("No! zamek is not present in the Dictionary")



# #Clear Method

# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear()
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary
# print(pol_eng_dictionary)


#Student Average Score
sd={}
while True:
    name = input("Enter student's name:")
    if name == "":
        break
    score = int(input(f"Enter ${name}'s score:"))

    if score not in range (1,11):
        break
    if name in sd:
        sd[name] +=(score,)
    else:
        sd[name] = (score,)
# for mark in sd:
#     print(mark)
print(sd)

for name, mark in sd.items():
    sum = 0
    # print(name,"->")
    for m in mark:
        # print(m)
        sum += m
    print(name, "->", sum/len(mark))        