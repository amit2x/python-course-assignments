# read_data.py
# First, ensure greetings.txt exists with some content
# --- Reading the entire file ---
print("--- Reading entire file ---")
file_read_all = open("greetings.txt", "r")
content = file_read_all.read()
print(content)
file_read_all.close()


# --- Reading line by line using readline() ---
print("\n--- Reading line by line (readline()) ---")
file_read_line = open("greetings.txt", "r")
line1 = file_read_line.readline()
line2 = file_read_line.readline()
print(f"First line: {line1.strip()}")
# .strip() removes leading/trailing whitespace, including '\n'
print(f"Second line: {line2.strip()}")
file_read_line.close()

# --- Reading all lines into a list (readlines()) ---
print("\n--- Reading all lines into a list (readlines()) ---")
file_read_list = open("greetings.txt", "r")
all_lines = file_read_list.readlines()
for line in all_lines:
    print(f"List item: {line.strip()}")
file_read_list.close()

# --- Best Practice: Iterating over file object (most common and efficient)---
print("\n--- Reading efficiently (for loop) ---")
file_efficient_read = open("greetings.txt", "r")

for line in file_efficient_read:
    print(f"Processed: {line.strip()}")
file_efficient_read.close()