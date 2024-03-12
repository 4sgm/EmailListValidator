## Description

EmailListValidator is an Open Source tool that uses Python to validate email addresses from a file line by line, using threads for concurrent processing. It performs basic syntax checks, MX record lookups, and temporary SMTP connections for verification. It checks for duplicates before validation to avoid redundant processing.

EmailListValidator performs the following checks:
- **Syntax Check:** Uses the defined regex to validate the email format.
- **MX Record Lookup:** Extracts the domain from the email address. Uses dns.resolver to query for the Mail Exchanger (MX) record of the domain. This helps identify if a valid mail server exists for the domain.
- **SMTP Conversation:** Establishes a temporary SMTP connection to the MX server. Sends commands to check if the email address is accepted by the server. (Note: This doesn't guarantee deliverability, but indicates a valid mailbox might exist.)

## Screenshot
![Commandline](https://github.com/ronknight/EmailListValidator/blob/master/assets/images/screenshots/screenshot.png)

## Installation

```bash
pip install -r requirements.txt
```

## Instruction
1. Replace email on helper.py Line 13 to your email address before running the program.
2. Set debug level to 0 if you want a clean output, change it to 1 if you want to see detailed error messages.
3. Replace test emails on input folder.

## Usage

```bash
python main.py 1 1
```
