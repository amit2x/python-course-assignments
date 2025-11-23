# write_data.py
# Open in 'w' mode: creates file or overwrites if it exists
file_write = open("greetings.txt", "w")
file_write.write("Hello, Python!\n") # Add newline manually
file_write.write("This is a new line.\n")
file_write.write("We are learning file handling.\n")
lines_to_write = ["First item\n", "Second item\n", "Third item\n"]
file_write.writelines(lines_to_write) # writelines expects strings with newlines
file_write.close()
print("Data written to greetings.txt")