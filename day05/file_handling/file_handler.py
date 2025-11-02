file_obj = open("myfile.txt", "a") # Open file in append mode
# print(dir(file_obj))
file_obj.write("This is the code line \n") # Write a line to the file
file_obj.close() # Close the file after writing

file_obj = open("myfile.txt", "r") # Open file in read mode
print(file_obj.readline()) # Print the line read
file_obj.close() # Close the file after reading

try:
    file_obj_new = open("non_existent_file.txt", "r") # Attempt to open a non-existent file
except FileNotFoundError:
    file_obj_new = open("non_existent_file.txt", "w") # Create the file if it doesn't exist
    file_obj_new.write("This file was created because it did not exist.\n")
finally:
    file_obj_new.close() # Ensure the file is closed
    
print("File handling operations completed.")