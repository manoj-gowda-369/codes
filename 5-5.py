def contains_substring(main_string, substring):
    return substring in main_string

# Example usage
text = "Hello, world!"
sub = "world"
print(f"'{sub}' in '{text}': {contains_substring(text, sub)}")