# File Creation and Writing
try:
    # Create and open the file in write mode
    with open('my_file.txt', 'w') as file:
        # Write three lines of text, including strings and numbers
        file.write("This is the first line of text.\n")
        file.write("The number is 42.\n")
        file.write("Python programming is fun.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file creation and writing: {e}")
finally:
    print("Finished file creation and writing.")

# File Reading and Display
try:
    # Open the file in read mode
    with open('my_file.txt', 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Display the contents on the console
        print("\nContents of 'my_file.txt':")
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file reading: {e}")
finally:
    print("Finished file reading.")

# File Appending
try:
    # Open the file in append mode
    with open('my_file.txt', 'a') as file:
        # Append three additional lines of text
        file.write("Appending a new line of text.\n")
        file.write("Another number: 123.\n")
        file.write("End of the additional lines.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error during file appending: {e}")
finally:
    print("Finished file appending.")

# Verify the final contents of the file
try:
    # Open the file in read mode again to verify appending
    with open('my_file.txt', 'r') as file:
        # Read the updated contents of the file
        updated_content = file.read()
        # Display the updated contents on the console
        print("\nUpdated contents of 'my_file.txt':")
        print(updated_content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error during final file reading: {e}")
finally:
    print("Finished verification of final file contents.")
