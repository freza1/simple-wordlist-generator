import itertools

# Define the character set of numbers and symbols
character_set = '0123456789!@#$%^&*()_+'

# Prompt the user for the total password length
total_length = int(input("Enter the total password length: "))

# Prompt the user for the prefixes to use (split by '/')
prefixes = input("Enter the prefixes to use (split by '/'): ").split('/')

# Generate all possible combinations of passwords with the specified prefixes and LeetCode-style variations
passwords_with_prefix = []

for prefix in prefixes:
    remaining_length = total_length - len(prefix)
    
    # Generate variations for the remaining characters, but limit to the remaining length
    max_variation_length = remaining_length
    for length in range(max_variation_length + 1):
        variations = itertools.product(character_set, repeat=length)
        for variation in variations:
            variation_str = ''.join(variation)
            password = prefix + variation_str
            # Check if the password length is 6 characters
            if len(password) == total_length:
                passwords_with_prefix.append(password)

# Remove duplicates by converting the list to a set and back to a list
unique_passwords = list(set(passwords_with_prefix))

# Prompt the user for the file path to save the wordlist
file_path = input("Enter the file path to save the wordlist (e.g., wordlist.txt): ")

# Save the wordlist to the specified file
with open(file_path, "w") as file:
    for password in unique_passwords:
        file.write(password + '\n')

print(f"Wordlist with {len(unique_passwords)} unique passwords of {total_length} characters generated and saved to '{file_path}'.")
