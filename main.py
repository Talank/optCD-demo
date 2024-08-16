import sys
import utils
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <yaml-file>")
        sys.exit(1)
    yaml_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    yaml_file_content = utils.get_file_content(yaml_file_path)
    modified_file = utils.modify_file_content(yaml_file_content)

    current_directory = os.getcwd()
    print("cwd is: "+str(current_directory))
    files_and_directories = os.listdir(current_directory)
    for item in files_and_directories:
        print(item)

    with open(output_file_path, 'w') as f:
        f.write(modified_file)
    
    print(modified_file)

    print("new list of files")
    files_and_directories = os.listdir(current_directory)
    for item in files_and_directories:
        print(item)


if __name__ == '__main__':
    main()
