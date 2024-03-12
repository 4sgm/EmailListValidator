# Import necessary libraries
import os
import sys
from helper import validation  # Import the validation function from the helper module
from natsort import natsorted  # For natural sorting of filenames
from threading import Thread  # For creating threads for concurrent processing

# Define the path to the directory containing input files
inputs_path = "./inputs"

# Get all files in the input directory
files = os.listdir(inputs_path)

# Sort the file list using natural sorting (e.g., "file10" after "file2")
files = natsorted(files)

# Get the starting and ending indexes for file selection from command-line arguments
start = int(sys.argv[1])
end = int(sys.argv[2]) + 1  # Note: end is non-inclusive

# Initialize a list to store selected files
selectedFiles = []

# Loop through each file in the sorted list
for i, file in enumerate(files, start=1):  # Use enumerate for index and filename
    # Check if the current file index is within the selected range
    if start <= i < end:
        selectedFiles.append(file)

# Only execute the following code if the script is run directly (not imported as a module)
if __name__ == '__main__':

    # Process each selected file
    for file in selectedFiles:
        # Create the full file path by combining the directory path and filename
        filepath = os.path.join(inputs_path, file)

        # Split the filename and extension
        filename, file_extension = os.path.splitext(filepath)

        # Convert the extension to lowercase for case-insensitive comparison
        file_extension = file_extension.lower()

        # Check if the file is a text file (.txt)
        if file_extension == ".txt":
            try:
                # Open the file for reading with the specified encoding
                f = open(filepath, "r", encoding="ISO-8859-1")

                # Read each line in the file (assuming each line contains an email address)
                for email in f:
                    # Clean up the email address by removing spaces and newlines
                    clean_email = email.strip()

                    # Create a new thread to call the validation function asynchronously
                    t = Thread(target=validation, args=(filename, clean_email, 1))

                    # Start the thread to perform validation concurrently
                    t.start()

                # Close the file after processing all lines
                f.close()

            # Catch any exceptions that might occur during file operations or validation
            except Exception as e:
                print("Error processing file:", filepath, ":", e)  # Provide more specific error message

        else:
            # Inform the user about non-TXT files
            print("X", "Not TXT =>", filepath)
