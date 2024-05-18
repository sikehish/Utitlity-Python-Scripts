def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            
        words = text.split()
        word_count = len(words)
        
        return word_count
    except:
        print(f"Error: The file {file_path} does not exist.")
        return None

def main():
    file_path = input("Enter the path to the file: ")
    word_count = count_words(file_path)
    
    if word_count is not None:
        print(f"Total word count: {word_count}")

if __name__ == "__main__":
    main()
