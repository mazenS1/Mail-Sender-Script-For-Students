# Mail Outreach Helpers

Automation scripts for sending batches of personalized outreach emails with your resume attached.

The project currently contains:

- `mass_mailer_txt.py`: sends emails to a list of addresses stored in a plain-text file. This is the primary script most users will run.
- `mass_mailer.py`: parses addresses from an Excel sheet that matches the author's internal layout (optional; requires tweaking for your own spreadsheet).

The sections below focus on getting `mass_mailer_txt.py` ready to use.

## Prerequisites

- Python 3.10 or newer.
- A Gmail account with [2-Step Verification](https://myaccount.google.com/security) enabled and an App Password generated for "Mail".
- A PDF resume (or any document you plan to attach).
- A text file containing one recipient email address per line (duplicates and malformed addresses are filtered automatically).

## Configure `mass_mailer_txt.py`

Open `mass_mailer_txt.py` and adjust the configuration block at the top of the file.

- `EMAIL_ADDRESS`: your Gmail address.
- `EMAIL_PASSWORD`: the 16-character app password you generated.
- `SUBJECT`: subject line to appear in every outgoing message.
- `RESUME_PATH`: absolute or relative path to the attachment you want to send.
- `EMAILS_PATH`: path to the `.txt` file that contains your recipient list.
- `DRY_RUN`: keep `True` while testing—emails go only to `Test_Email` / `Test_Email2`.
- `Test_Email` / `Test_Email2`: dummy addresses you control for dry runs.
- `CONTACT_*` / `GITHUB_URL` / `LINKEDIN_URL` / `PORTFOLIO_URL`: optional links used in the email signature.
- Replace the placeholder text `WRITE YOUR MESSAGE HERE` (both plain-text and HTML sections) with the body of your email. Keep the formatting if you want the signature to render nicely.

## Prepare Your Recipient List

Create a UTF-8 encoded text file—`mails.txt` for example—with one email address per line. Blank lines and duplicates are ignored automatically. You can maintain multiple lists (e.g., `mails2.txt`) and point `EMAILS_PATH` to whichever list you want.

## Test Mode (Highly Recommended)

1. Set `DRY_RUN = True`.
2. Ensure `Test_Email` (and optionally `Test_Email2`) are addresses you control.
3. Run the script:

   ```powershell
   python mass_mailer_txt.py
   ```

4. Confirm the message looks correct in your inbox. Adjust the wording and signature until satisfied.

## Send the Campaign

1. Flip `DRY_RUN` to `False`.
2. Double-check `RESUME_PATH`, `EMAILS_PATH`, and the message body.
3. Run the script:

   ```powershell
   python mass_mailer_txt.py
   ```

4. The script prints each recipient and reports success (`✅`) or failure (`❌`). A five-second pause between messages helps avoid Gmail rate limits.

If a send fails, the script continues with the next address. Review the console output to identify any invalid addresses or authentication issues.

## Troubleshooting Tips

- Authentication errors usually mean the Gmail app password is incorrect or 2-Step Verification is disabled.
- `FileNotFoundError` indicates `RESUME_PATH` or `EMAILS_PATH` is pointing to a non-existent file. Check spelling and use absolute paths if necessary.
- If Gmail flags the activity, wait and try again—heavy sending in a short window may trigger rate limits.

## Optional: Excel-Based Workflow

`mass_mailer.py` demonstrates how to extract emails from a structured Excel file (`comp.xlsx`). It requires `pandas` and is tailored to the author's column names. Install dependencies with `pip install pandas` and adapt the parsing logic before use.

## Good Practice Checklist

- Proofread your email copy and signature.
- Send yourself a final test message with `DRY_RUN = False` but a single known-good address.
- Respect privacy laws and company policies when sending mass outreach emails.
