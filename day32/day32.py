import smtplib
import datetime
import random

# Challenge #1
my_email = "####"
my_password = "####"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg="Subject:Hi!\n\nI am sending an email from python :)")

# Challenge #2
now = datetime.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as f:
        quotes = f.readlines()
        rand_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Motivational Friday\n\n{rand_quote}")

