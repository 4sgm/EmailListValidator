import os
import sys
from helper import validation
from natsort import natsorted
from threading import Thread
import time


inputs_path = "./inputs"
files = os.listdir(inputs_path)
files = natsorted(files)

start = int(sys.argv[1])
end = int(sys.argv[2])+1

i = 0
selectedFiles = []

for file in files:
    i += 1
    if i in range(start, end):
        selectedFiles.append(file)


if __name__ == '__main__':
    for file in selectedFiles:
        filepath = inputs_path + '/' + file
        filename, file_extension = os.path.splitext(filepath)
        file_extension = file_extension.lower()
        if file_extension == ".txt":
            try:
                f = open(filepath, "r")
                for email in f:
                    email = str(email).replace(' ', '').replace('\n', '')
                    t = Thread(target=validation, args=(filename, email, 1))
                    t.start()
                f.close()

            except Exception as e:
                print("Error", e)

        else:
            print("X", "Not TXT =>", filepath)
