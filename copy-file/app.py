import os

def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
        
        print(f"Contents copied from {source_path} to {destination_path}")
    except:
        print(f"Error: The file {source_path} does not exist.")

def main():
    source_path = input("Enter the path to the source file: ")

    if not os.path.isfile(source_path) :
         print("File not found!")
         return
    
    destination_path = input("Enter the path to the destination file: ")
    copy_file(source_path, destination_path)

if __name__ == "__main__":
    main()
