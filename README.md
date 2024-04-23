<p><a target="_blank" href="https://app.eraser.io/workspace/dDqA5e0i04YGKv2rLypf" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

## Description
EmailListValidator is an Open Source tool that uses Python to validate email addresses from a file line by line, using threads for concurrent processing. It performs basic syntax checks, MX record lookups, and temporary SMTP connections for verification. It checks for duplicates before validation to avoid redundant processing.

EmailListValidator performs the following checks:

- **Syntax Check:** Uses the defined regex to validate the email format.
- **MX Record Lookup:** Extracts the domain from the email address. Uses dns.resolver to query for the Mail Exchanger (MX) record of the domain. This helps identify if a valid mail server exists for the domain.
- **SMTP Conversation:** Establishes a temporary SMTP connection to the MX server. Sends commands to check if the email address is accepted by the server. (Note: This doesn't guarantee deliverability, but indicates a valid mailbox might exist.)
## Screenshot
![Commandline](https://github.com/ronknight/EmailListValidator/blob/v1/assets/images/screenshots/screenshot.png "")

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
## Result Sample
**1. all.txt** - List of tested emails

![all](https://github.com/ronknight/EmailListValidator/blob/v1/assets/images/screenshots/all_txt.png "")

**2. result.txt** - Progress

![result](https://github.com/ronknight/EmailListValidator/blob/v1/assets/images/screenshots/result_txt.png "")

**3. valid [0-100000].csv** - Validated emails

![valid](https://github.com/ronknight/EmailListValidator/blob/v1/assets/images/screenshots/valid_%5B0-100000%5D_csv.png "")




<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-EmailListValidator Process Flow-1.eraserdiagram" data-element-id="s1JQV6q24DSbooOVP3TKJ"><img src="/.eraser/dDqA5e0i04YGKv2rLypf___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----fa1819b8a1c1666ce3ff040e8990c867-EmailListValidator-Process-Flow.png" alt="" data-element-id="s1JQV6q24DSbooOVP3TKJ" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/dDqA5e0i04YGKv2rLypf --->