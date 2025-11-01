user_input = input("Enter the list of numbers: ")
list_of_nums = list(map(int,user_input.split())) 

choice = input("1.Print a List \n 2.Add element at the end \n Enter your choice: ")

if choice == '1':
    print("List:", list_of_nums)
    
elif choice == '2':
    element = input("Enter the element to add at the end: ")
    list_of_nums.append(element)
    print("List after adding element:", list_of_nums)
    
else:
    print("Invalid choice")
    
#Finding the Smallest and Second smallest number in the list
print("Finding the Smallest and Second smallest number in the list")

#Smallest number
smallest = min(list_of_nums)
print("Smallest number is:", smallest)

#Second Smallest number
list_of_nums.remove(smallest)
second_smallest = min(list_of_nums)
print("Second Smallest number is:", second_smallest)

        

