# with open("data.txt", "r") as file:
#     data = file.read()
# print(data)



# with open("students.txt", "w") as file:
#     file.write("Alice, 85\n")
#     file.write("Bob, 90\n")
#     file.write("Charlie, 78\n")

# with open("students.txt", "r") as file:
#     content = file.read()
# print(content)


# with open("students.txt", "r") as file:
#     for line in file:
#         name, score = line.strip().split(", ")
#         print(f"{name:<15} |{score:>5}")
#         print("----------")




#CSV 



# import csv
# #writing csv
# records = [
#     ['Name', 'Marks', 'City', 'Grade'],
#     ['Alice', 85, 'New York', 'A'],
#     ['Bob', 90, 'Los Angeles', 'A+'],
#     ['Charlie', 78, 'Chicago', 'B']
# ]
# with open('students.csv', 'w', newline='') as file:
#     csv.writer(file).writerows(records)


# #reading csv
# with open('students.csv', 'r') as file:
#     for row in csv.DictReader(file):
#         print(f'{row["Name"]}: {row["Marks"]} marks ({row["City"]})')


import csv
records = [
    ['Name', 'Age', 'Marks1', 'Marks2', 'Marks3'],
    ['Harshit', 22, 88, 89, 93],
    ['Divya', 22, 88, 89, 93],
    ['Abhishek', 22, 88, 89, 93],
    ['Harsh', 22, 88, 89, 93]
]
with open('CLI.csv', 'w', newline='') as file:
    csv.writer(file).writerows(records)

student = input("Enter Student Name:")
found = False
with open('CLI.csv', 'r', newline='') as file:
    for row in csv.DictReader(file):
        if row['Name'] == student:
            print(f"{row['Name']}: age {row['Age']} marks1 {row['Marks1']} marks2 {row['Marks2']} marks3 {row['Marks3']}")
            found = True
            break
if not found:
        print("No Student Record Found")