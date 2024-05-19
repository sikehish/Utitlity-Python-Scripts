def count_words(file_path):
    """
    Count the total number of words in a text file.
    
    Parameters:
    file_path (str): The path to the text file.
    
    Returns:
    int or None: The total word count if the file exists, otherwise None.
    """
    try:
        # Open the file in read mode and read its contents
        with open(file_path, 'r') as file:
            text = file.read()
            
        # Split the text into words based on whitespace
        words = text.split()
        
        # Count the number of words
        word_count = len(words)
        
        # Return the word count
        return word_count
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file {file_path} does not exist.")
        return None

def main():
    """
    Main function to input file path, count words, and print the word count.
    """
    # Prompt the user to enter the path to the file
    file_path = input("Enter the path to the file: ")
    
    # Count the words in the file
    word_count = count_words(file_path)
    
    # Print the word count if it's not None
    if word_count is not None:
        print(f"Total word count: {word_count}")

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
