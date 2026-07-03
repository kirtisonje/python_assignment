file_name = "my_python_assignment.txt"
content = "Hello! This text was written using Python's file operations."

#write file
with open(file_name, 'w') as file:
    file.write(content)

print(f"Successfully written to '{file_name}'!")



#read file
with open(file_name, 'r') as file:
    # Use file.read() to get the entire content of the file
    file_content = file.read()

print("--- File Contents ---")
print(file_content)