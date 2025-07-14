import pandas as pd
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

try:
    # 📥 Load the email queue
    df = pd.read_csv("email_queue.csv")

    invalid_emails = []  # ✅ Track skipped emails

    # 📤 Loop through each email entry
    for index, row in df.iterrows():
        email = row['email']
        subject = row['subject']
        message = row['message']

        # ✅ Validate email format
        if not is_valid_email(email):
            print(f"⚠️ Invalid email format: {email}")
            invalid_emails.append(email)
            continue  # Skip this entry

        # ✉️ Simulate sending
        print(f"\n📬 Sending to: {email}")
        print(f"📌 Subject: {subject}")
        print(f"📝 Message: {message}")
        print("✅ Email 'sent' successfully!")

    # 🚫 Show skipped emails
    if invalid_emails:
        print(f"\n🚫 {len(invalid_emails)} emails skipped due to format issues:")
        for bad_email in invalid_emails:
            print(f" - {bad_email}")

    # 📊 Summary
    print(f"\n📊 Summary:")
    print(f" - Total processed: {len(df)}")
    print(f" - Sent: {len(df) - len(invalid_emails)}")
    print(f" - Skipped: {len(invalid_emails)}")

except Exception as e:
    print(f"⚠️ Oops! Something went wrong: {e}")





