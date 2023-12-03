# Open the file (replace 'filename.txt' with your file's name)
file_name = r'C:\Users\subra\Desktop\Test-Project\Data-File.txt'

try:
    with open(file_name, 'r') as file:
        # Read the contents of the file
        file_content = file.read()
        
        # Print the content
        print(file_content)
        
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

