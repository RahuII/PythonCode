import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    my_email = "yadavkr1303@gmail.com"
    password = "Rahul@2040"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vipulu563@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
