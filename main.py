##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas 
import datetime as dt
import smtplib
import random
import os

path = ("birthdays.csv")
data = pandas.read_csv(path)
data_dict = data.to_dict(orient = "records")

now = dt.datetime.now()
now_tuple = (now.month, now.day)

birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}


if now_tuple in birthday_dict:
    birthday_person = birthday_dict[now_tuple]
    folder = ("letter_templates")
    all_files = os.listdir(folder)
    txt_files = [f for f in all_files if f.endswith(".txt")]
    random_files = random.choice(txt_files)
    with open(os.path.join(folder, random_files), "r") as f:
        contents = f.read()
        personalized_letter = contents.replace("[NAME]", birthday_person["name"])
    
    
    
    email = "thatpythonguy2374@gmail.com"
    password = "jufi dcgg aput uwrp"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr = email, 
                        to_addrs= f"{birthday_person["email"]}",
                        msg = f"Subject:Happy Birthday!\n\n{personalized_letter}.")
else:
    print("None")

   


