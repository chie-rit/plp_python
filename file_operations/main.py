def modifier(content: str):
    """
    Converts contents to lowercase
    """
    return content.lower()

def file_modifier(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        modified_content = modifier(content)

        with open(output_file, 'w') as new_file:
            new_file.write(modified_content)

        print(f'File content written to {new_file}')
    except FileNotFoundError:
        print('File Not Found')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    try:
        input_file = input("Enter the name of the file to read from: ")
        output_file = input("Enter the name of the file to write to: ")

        file_modifier(input_file, output_file)
    except Exception as e:
        print(f'An error occurred: {e}')
