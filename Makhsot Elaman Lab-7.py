def count_lines_not_starting_with_D(file_name):
    try:
        with open(file_name, 'r') as file:
            # Use a list comprehension to count lines that do not start with 'D'
            count = sum(1 for line in file if not line.startswith('D'))

        return count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'text1.txt' with the actual file path if it's in a different directory
result = count_lines_not_starting_with_D('text1.txt')

if result is not None:
    print(f"Output: {result}")
