

import os


if __name__ == '__main__':
    files = os.listdir('outputs/')
    for file in files:
        filepath = 'outputs/' + file
        f = open(filepath, "r")
        for email in f:
            email = str(email).replace(' ', '').replace('\n', '')
            print("*", email, "+")

        f.close()
