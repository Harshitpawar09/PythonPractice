# city = 'Bhopal'
# print(city[0])
# print(city[2])
# print(city[-1])
# print(city[5])
# print(city[-3])
# print(city[3])

# #Slicing
# name = 'Priya Sharma'
# print(name[0:5])  # Prints 'Priya'
# print(name[6:])  # Prints 'Sharma'
# print(name[:5])  # Prints 'Priya'
# print(name[::2])  # Prints 'PryShrm'
# print(name[::-1])  # Prints 'amrahS ayirP'

# #Length of string
# print(len(name))  # Prints the length of the string
# print(len(city))  # Prints the length of the string




#Case

# text = ' Hello Python World! '
# #case
# print(text.upper())  # Converts to uppercase
# print(text.lower())  # Converts to lowercase
# print(text.title())  # Converts to title case
# print(text.capitalize())  # Capitalizes the first letter of the string

# #strip whitespace
# print(text.strip())  # Removes leading and trailing whitespace

# #search
# print('Python' in text)  # Checks if 'Python' is in the text
# print(text.find('Python'))  # Finds the index of 'Python' in the text
# print(text.count('l'))




# #  Replace 
# print(text.replace('Python', 'AI'))  # Replaces 'Python' with 'AI'
# #Split and Join
# csv = 'rahul,22,bhopal,engineer'
# parts = csv.split(',')
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

# #check content
# print('hello123'. isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print('   '.isspace())

# #start/end check
# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu')) 




# name, marks, rank = 'Anita', 92.5278, 3
# #basic
# print(f'Hello, {name}!)')
# #format numbers
# print(f'marks: {marks:.2f}')  # Prints marks with 2 decimal places
# print(f'marks: {marks:.0f}') 
# print(f'count: {100000}')

# #padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|{rank}')
# print(f'hello {name:>10}')
# print(f'hello {name:<10}')
# print(f'hello {name:^10}')
# print(f'hello {name:*^11}')



# price, +gst = 500, 0.18
# print(f'price:rs{price} | gst:rs. {price*gst:.2f} | total:rs. {price*(1+gst):.2f}')





string = "Hello, How are you doing today?"
#count the vowels in the string
vowels = 'aeiouAEIOU'
count = sum(1 for char in string if char in vowels)
print(f'The number of vowels in the string is: {count}')






#print you from the string
you_index = string.find('you')
if you_index != -1:
    print(f'Found "you" at index: {you_index}')
else:
    print('"you" not found in the string.')





#reverse the string
reversed_string = string[::-1]
print(f'Reversed string: {reversed_string}')





non_palin, palin = "abcdef", "axttxa"
#check if the string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
print(f'Is "{non_palin}" a palindrome? {is_palindrome(non_palin)}')
print(f'Is "{palin}" a palindrome? {is_palindrome(palin)}')








