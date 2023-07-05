import random
import smtplib

import string

def generate_otp(length):
    characters = string.digits  # Use only digits
    otp = ''
    for _ in range(length):
        otp += random.choice(characters)
    return otp

# Generate a 6-digit OTP
otp = generate_otp(6)
print("Generated OTP:", otp)



my_email = "YOUR_EMAIL@Gmail.Com"
password = "ABC123"

receiver = "RECEIVINGEMAIL@GMAIL,COM"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiver,
                        msg=f"SUBJECT:One-time-passcode (OTP)\n\nThe OTP for your account is {otp}. Enter it now to continue logging in.")
