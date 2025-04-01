input_filename = input("Enter the filename to read from: ")
output_filename = input("Enter the filename to write to: ")

try:
    # Open the file for reading
    with open(input_filename, 'r') as file:
        content = file.read()  # Read content of the file
        
    # Modify the content (example: reverse the content)
    modified_content = content[::-1]  # Reverse the content
    
    # Open the output file for writing
    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)  # Write the modified content to the new file
    
    print(f"Content from {input_filename} has been successfully modified and saved to {output_filename}.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except IOError as e:
    print(f"Error: There was an issue reading or writing the file. Details: {e}")
