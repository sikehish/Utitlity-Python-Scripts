import os

def copy_file(source_path, destination_path):
    """
    Copies the content of the source file to the destination file.
    
    Parameters:
    source_path (str): The path to the source file.
    destination_path (str): The path to the destination file.
    """
    try:
        # Open the source file in read mode
        with open(source_path, 'r') as source_file:
            content = source_file.read()  # Read the entire content of the source file

        # Open the destination file in write mode (creates the file if it doesn't exist)
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)  # Write the content to the destination file
        
        print(f"Contents copied from {source_path} to {destination_path}")  # Success message
    except:
        # If there's an error (e.g., the source file does not exist), print an error message
        print(f"Error: The file {source_path} does not exist.")

def main():
    """
    Main function to prompt the user for file paths and initiate the file copy process.
    """
    source_path = input("Enter the path to the source file: ")  # Prompt user for the source file path

    # Check if the source file exists
    if not os.path.isfile(source_path):
        print("File not found!")  # Print error message if the source file does not exist
        return  # Exit the function

    destination_path = input("Enter the path to the destination file: ")  # Prompt user for the destination file path
    copy_file(source_path, destination_path)  # Call the function to copy the file

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
