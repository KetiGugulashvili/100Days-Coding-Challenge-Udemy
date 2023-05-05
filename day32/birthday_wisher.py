import pandas
import datetime
import random
import smtplib

data = pandas.read_csv("birthdays.csv")
now = datetime.datetime.now()

same_month = data[data.month == now.month]
same_day = same_month[same_month.day == now.day]
names = same_day.name.to_list()

my_email = "####"
my_password = "####"

for name in names:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as f:
        data = f.read()
        new_data = data.replace("[NAME]", name)

    email = same_day[same_day["name"] == name].email.to_string(index=False)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday {name}!\n\n{new_data}")
