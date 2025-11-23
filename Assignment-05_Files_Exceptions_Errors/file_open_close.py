# file_open_close.py
# Open a file in write mode ('w')
# If 'my_file.txt' exists, its content will be deleted!
# If it doesn't exist, it will be created.
file_object = open("my_file.txt", "w")
print("File 'my_file.txt' opened in write mode.")
# Perform some operations (writing will come later)
# ...
# Close the file
file_object.close()
print("File 'my_file.txt' closed.")
# Now try opening in read mode ('r')
# This will raise an error if 'my_file.txt' doesn't exist (e.g., if you run this alone)
try:
    file_object_read = open("my_file.txt", "r")
    print("File 'my_file.txt' opened in read mode.")
    file_object_read.close()
    print("File 'my_file.txt' closed.")
except FileNotFoundError:
    print("Error: 'my_file.txt' not found for reading (might not have been created yet).")