
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from os.path import basename
import re
import smtplib
import dns.resolver


# Address used for sending emails (replace with your address)
fromAddress = 'r.ahmadifar.1377@gmail.com'

# Simple Regex for email syntax validation
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'


def check(emailAddress):

    try:
        # Check syntax using the defined regular expression
        match = re.match(regex, emailAddress)
        if match == None:
            return False

        # Extract domain name from the email address for DNS lookup 

        splitAddress = emailAddress.split('@')
        domain = str(splitAddress[1])

        # Perform MX record lookup to find the mail exchange server for the domain

        records = dns.resolver.resolve(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # Connect to the mail exchange server using smtplib. SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP(timeout=2)
        server.set_debuglevel(1) # Change to 1 for detailed debug output

        # SMTP Conversation handshake with the server
        server.connect(mxRecord)

        # server.local_hostname(Get local server hostname)  # Commented out, purpose unclear
        # server.helo(server.local_hostname)
        server.mail(fromAddress)
        code, message = server.rcpt(emailAddress)
        server.quit()

        # Assuming a successful response code (250) indicates a valid email address

        if code == 250:
            return True
        else:
            return False
    except KeyError:
        return False # Likely DNS lookup error
    except Exception as e:
        return False # Catch any other exceptions


def saveResult(correct):
    # Open "result.txt" for reading and writing
    frw = open("result.txt", "r+")
    # Read current total and correct counts
    nums = frw.read().split("/")
    tot = int(nums[1])
    cur = int(nums[0])
    # Update total count
    tot += 1
    # Update correct count if the email is valid
    if correct:
        cur += 1
      # Write updated counts back to the file
    dw = str(cur) + "/" + str(tot)
    frw.seek(0)
    frw.write(dw)
    frw.close()
    # Return the updated result string and current correct count
    return dw, cur


def saveOutputs(fc, email):  
    # Open a CSV file for appending valid emails
    frw = open("./outputs/valid " + fc + ".csv", "a")
    # Write the email
    frw.write(email + "\n")
    frw.close()


def addEmail2List(email):
    frw = open("all.txt", "a")
    frw.write(email + "\n")
    frw.close()


def isDuplicate(email):
    frw = open("all.txt", "r")
    mm = email in frw.read()
    frw.close()
    return mm


mxf = 100000


def validation(file, email, arg):
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
                name = str((int(count / mxf) - 1) * mxf)
                name += "-"
                name += str((int(count / mxf)) * mxf)
            else:
                # append
                name = str((int(count / mxf)) * mxf)
                name += "-"
                name += str((int(count / mxf) + 1) * mxf)

            saveOutputs("[" + name + "]", email)

    #
    cond = str(isCorrect)
    if isCorrect:
        cond = cond + " "
    print("#", cond, '(' + result + ')', email, file)