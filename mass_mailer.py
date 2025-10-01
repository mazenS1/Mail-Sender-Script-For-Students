import pandas as pd
import smtplib
import ssl
from email.message import EmailMessage

# === CONFIG ===
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
SUBJECT_TEMPLATE = "Application for Cooperative Training - {company}"

# Path to resume
RESUME_PATH = "resume.pdf"

def parse_excel(file_path):
    # If your headers aren't on the first row, try header=1 (or 2, etc.)
    df = pd.read_excel(file_path, header=9)  # e.g., pd.read_excel(file_path, header=1)
    # Normalize column names (trim spaces/convert to str)
    df.columns = df.columns.map(lambda c: str(c).strip())
    print("Columns found:", df.columns.tolist())

    required = ['التقديم', 'المدينة', 'اسم الجهة']
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Clean emails
    emails = (
        df['التقديم']
        .dropna()
        .astype(str)
        .loc[lambda s: s.str.contains('@')]
        .tolist()
    )

    # Keep only allowed cities (fixes the logic bug in your current code)
    allowed = {'عدة مدن', 'الرياض', 'الوسطى', 'الرياض'}
    cities = (
        df['المدينة']
        .dropna()
        .astype(str)
        .loc[lambda s: s.isin(allowed)]
        .tolist()
    )

    companies = (
        df['اسم الجهة']
        .dropna()
        .astype(str)
        .tolist()
    )

    return emails, cities, companies

# Load Excel file
emailList, cityList, companyList = parse_excel("comp.xlsx")

for i, (email, city, company) in enumerate(zip(emailList, cityList, companyList), start=1):
    print(f"{i}. {email} | {city} | {companyList[i]}")

# Clean data: drop rows with no email
'''	
df = df.dropna(subset=['Email'])

# Email sending function
def send_email(to_email, company_name):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = SUBJECT_TEMPLATE.format(company=company_name)

    # Cover letter inside the email
    body = f"""
    Dear {company_name} Hiring Team,

    I am writing to express my strong interest in joining your organization as a cooperative trainee. 
    I am eager to contribute my skills, learn from experienced professionals, and support your team’s goals. 

    Please find my attached resume for your consideration. I would be grateful for the opportunity 
    to discuss how I can add value to your team. 

    Thank you for your time and consideration.  

    Best regards,  
    [Your Full Name]  
    [Your Phone Number]  
    """
    msg.set_content(body)

    # Attach resume only
    with open(RESUME_PATH, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="Resume.pdf")

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print(f"✅ Email sent to {to_email} ({company_name})")

# Loop through rows
for _, row in df.iterrows():
    email = row['Email']
    company = row['Company']
    try:
        send_email(email, company)
    except Exception as e:
        print(f"❌ Failed to send to {email} ({company}): {e}")
'''