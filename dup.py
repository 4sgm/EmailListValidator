import os
from natsort import natsorted

# Initialize an empty list to store all unique email addresses
allEmails = []

# Define a constant for the maximum number of emails per file (100,000)
mxf = 100000

# Variable to track the total number of processed emails (starts at 0)
count = 0

# Only execute the following code if the script is run directly (not imported as a module)
if __name__ == '__main__':

    # Get a list of all files in the "outputs/" directory
    files = os.listdir('outputs/')

    # Sort the file list using natural sorting (e.g., "file10" after "file2")
    files = natsorted(files)

    # Loop through each file in the sorted list
    for file in files:

        # Create the full path to the current file
        filepath = 'outputs/' + file

        # Open the file for reading
        f = open(filepath, "r")

        # Loop through each line in the file (assuming each line contains an email address)
        for email in f:
            # Clean up the email address by removing spaces and newlines
            clean_email = email.strip()

            # Check if the email address is already present in the list
            if clean_email in allEmails:
                # Print a message indicating a duplicate email
                print("> ", clean_email, "Duplicated")
            else:
                # Add the unique email address to the list
                allEmails.append(clean_email)

                # Increment the count of processed emails
                count += 1

                # Check if a new output file needs to be created
                if count % mxf == 0:
                    # Calculate the base filename based on the current count segment
                    base_name = str((int(count / mxf) - 1) * mxf)

                    # Create the filename with numbering for the new file segment
                    name = base_name + "-" + str(int(count / mxf) * mxf)
                else:
                    # Use the current file segment for appending to the existing file
                    name = str(int(count / mxf) * mxf) + "-" + str((int(count / mxf) + 1) * mxf)

                # Open a new file for appending unique emails (with numbering)
                frw = open("./removeDup/valid [" + name + "].csv", "a")

                # Write the unique email address to the output file
                frw.write(clean_email + "\n")

                # Close the output file
                frw.close()

                # Print a message indicating successful processing with details
                print("> ", clean_email, count, file)

        # Close the current file after processing all lines
        f.close()
