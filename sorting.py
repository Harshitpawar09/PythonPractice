#Bubble sort
list1 = [1,2,3,4,5]  #[8, 10, 6, 2, 4]
swapped = True
count = 0
while swapped:
    swapped = False
    for i in range(len(list1)-1):
        count += 1
        if list1[i] > list1[i+1]:
            swapped = True
            list1[i], list1[i+1] = list1[i+1], list1[i]
print(list1)
print(count)


#Sort Method
list = [8,3,2,9]
list.sort()
print(list)
list.reverse() #reverse the list
print(list)
