import os
import sys
from helper import addEmail2List, check, isDuplicate, saveOutputs, saveResult
from natsort import natsorted


mxf = 100000
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


print(selectedFiles)

for file in selectedFiles:
    filepath = inputs_path + '/' + file
    filename, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.lower()
    if file_extension == ".txt":
        try:
            f = open(filepath, "r")
            for email in f:
                email = str(email).replace(' ', '').replace('\n', '')
                isCorrect = False
                result = ''
                if isDuplicate(email):
                    isCorrect = False
                    result, count = saveResult(isCorrect)
                else:
                    addEmail2List(email)
                    isCorrect = check(email)
                    result, count = saveResult(isCorrect)

                    if isCorrect:
                        if count % 100000 == 0:
                            # new file
                            name = str((int(count/mxf)-1) * mxf)
                            name += "-"
                            name += str((int(count/mxf)) * mxf)
                        else:
                            # append
                            name = str((int(count/mxf))*mxf)
                            name += "-"
                            name += str((int(count/mxf)+1)*mxf)

                        saveOutputs("[" + name + "]", email)

                #
                cond = str(isCorrect)
                if isCorrect:
                    cond = cond + " "
                print("#", cond, '(' + result + ')', email)

            f.close()

        except Exception as e:
            print("Error", e)
            # return False

    else:
        print("X", "Not TXT =>", filepath)
