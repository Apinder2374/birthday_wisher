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
    
    
    
    email = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr = email, 
                        to_addrs= f"{birthday_person["email"]}",
                        msg = f"Subject:Happy Birthday!\n\n{personalized_letter}.")
else:
    print("None")

   


