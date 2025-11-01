list_of_nums = [64, 34, 25, 12, 22, 11, 90]

# Bubble sort algorithm
for i in range(len(list_of_nums)):
   for j in range(len(list_of_nums)):
        if list_of_nums[i] > list_of_nums[j]:
            #swap
            temp = list_of_nums[i]
            list_of_nums[i] = list_of_nums[j]
            list_of_nums[j] = temp
            
print("Sorted list is:", list_of_nums)