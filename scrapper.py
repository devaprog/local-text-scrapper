import os

def scrape_directory_content(root_dir, output_file_path):
    """
    Traverses a directory tree, copies the content of all text files,
    and stores it in a single output file, preserving the tree structure.

    Args:
        root_dir (str): The absolute or relative path to the directory to be scraped.
        output_file_path (str): The path where the output .txt file will be saved.
    """
    # Check if the provided root directory exists.
    if not os.path.isdir(root_dir):
        print(f"Error: The directory '{root_dir}' does not exist.")
        return

    try:
        # Open the output file in write mode with UTF-8 encoding.
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Add a header to the output file.
            output_file.write(f"Content scraped from directory: {os.path.abspath(root_dir)}\n")
            output_file.write("=" * 80 + "\n\n")

            # os.walk() generates the file names in a directory tree
            # by walking the tree either top-down or bottom-up.
            for dirpath, _, filenames in os.walk(root_dir):
                # Check if the current directory is not empty.
                if filenames:
                    # Write the current directory path to the output file to show the structure.
                    relative_dir_path = os.path.relpath(dirpath, root_dir)
                    output_file.write(f"// Path: {relative_dir_path}\n")
                    output_file.write("-" * 80 + "\n")

                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)

                        try:
                            # Attempt to open and read the file as text.
                            # This will fail for binary files (images, executables, etc.).
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as current_file:
                                # Write the file name as a header for its content.
                                output_file.write(f"\n--- File: {filename} ---\n\n")

                                # Read the content and write it to the output file.
                                content = current_file.read()
                                output_file.write(content)
                                output_file.write("\n\n")

                        except Exception as e:
                            # If a file can't be read for any reason, print a notice
                            # and continue to the next file.
                            print(f"Could not read file: {file_path}. Reason: {e}")

        print(f"\nSuccessfully scraped all text content into '{output_file_path}'")

    except IOError as e:
        print(f"Error writing to output file '{output_file_path}'. Reason: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Get the directory path from the user.
    input_directory = input("Enter the path of the directory to scrape: ")

    # Define the name of the output file.
    output_filename = "directory_content_output.txt"

    # Call the main function to start the process.
    scrape_directory_content(input_directory, output_filename)
