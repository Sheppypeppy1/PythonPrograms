#import smtplib

#with open('data.txt','r') as file:
#    data = file.readlines()

#my_email = data[0]
#my_password = data[1]

#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=my_password)
#    connection.sendmail(from_addr=my_email,to_addrs=my_email, 
#                        msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2023:
    print("year is 2020")