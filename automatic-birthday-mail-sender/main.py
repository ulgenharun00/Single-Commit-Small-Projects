import datetime
import random
import smtplib
import pandas

today = datetime.datetime.now()
today = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}

if today in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace("[NAME]",f"{birthdays_dict[today]['name']}")

my_email = "<mail goes here>"
my_password = "<secure password>"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthdays_dict[today]["email"],
        msg=f"Subject:Happy Birthday!\n\n{letter_content}"
    )



