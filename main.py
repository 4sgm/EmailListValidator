import os
import sys
from helper import check, saveOutputs, saveResult


mxf = 100000
allEmails = []
inputs_path = "./inputs"
files = os.listdir(inputs_path)
files.sort()
start = int(sys.argv[1])
end = int(sys.argv[2])+1


i = 0

for file in files:
    i += 1
    filepath = inputs_path + '/' + file
    if i in range(start, end):
        filename, file_extension = os.path.splitext(filepath)
        file_extension = file_extension.lower()
        if file_extension == ".txt":
            try:
                f = open(filepath, "r")
                for email in f:
                    email = str(email).replace(' ', '').replace('\n', '')
                    isCorrect = False
                    result = ''
                    if email in allEmails:
                        isCorrect = False
                        result, count = saveResult(isCorrect)
                    else:
                        allEmails.append(email)
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
