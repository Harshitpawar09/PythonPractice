# with open("data.txt", "r") as file:
#     data = file.read()
# print(data)



with open("students.txt", "w") as file:
    file.write("Alice, 85\n")
    file.write("Bob, 90\n")
    file.write("Charlie, 78\n")

with open("students.txt", "r") as file:
    content = file.read()
print(content)


with open("students.txt", "r") as file:
    for line in file:
        name, score = line.strip().split(", ")
        print(f"{name:<15} |{score:>5}")
        print("----------")