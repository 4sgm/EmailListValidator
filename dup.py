

from itertools import count
import os

allEmails = []
mxf = 100000
count = 0
if __name__ == '__main__':
    files = os.listdir('outputs/')
    for file in files:
        filepath = 'outputs/' + file
        f = open(filepath, "r")
        for email in f:
            email = str(email).replace(' ', '').replace('\n', '')
            if email in allEmails:
                print("Duplicated", email)
            else:
                allEmails.append(email)

                if count % 100000 == 0:
                    # new file
                    name = str((int(count / mxf) - 1) * mxf)
                    name += "-"
                    name += str((int(count / mxf)) * mxf)
                else:
                    # append
                    name = str((int(count / mxf)) * mxf)
                    name += "-"
                    name += str((int(count / mxf) + 1) * mxf)

                frw = open("./removeDup/valid [" + name + "].csv", "a")
                frw.write(email + "\n")
                frw.close()
                count += 1

        f.close()
