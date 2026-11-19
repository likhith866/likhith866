# 1. Define the old string
old_string = "Hello, Python World!"

# 2. Extract a substring using slicing [start:end]
substring = old_string[7:13]  # Extracts "Python"

# 3. Create a new string by replacing a part of the old string
new_string = old_string.replace("World", "Developers")

# 4. Print strings and their lengths
print("Old String:", old_string, "| Length:", len(old_string))
print("Substring:", substring, "| Length:", len(substring))
print("New String:", new_string, "| Length:", len(new_string))

# 5. Print individual characters of the substring
print("\nCharacters in the substring:")
for index, char in enumerate(substring):
    print(f"Index {index}: {char}")
