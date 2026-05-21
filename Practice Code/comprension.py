# row = []
# for i in range(8):
#     row.append("White_Pawn")
#or
# row = ["White_Pawn" for i in range(8)]
# print(row)

# square = [x ** 2 for x in range(1,11)]
# print(square)

# twos = [2 ** index for index in range(8)]
# print(twos)


square = [x ** 2 for x in range(1,11)]
odds = [x for x in square if x % 2 != 0]
print(odds)


