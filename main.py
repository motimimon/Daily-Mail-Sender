import requests
import smtplib
NEWS_API_KEY = "get your api key from https://newsapi.org/"
FROM_EMAIL = "the  email from which you want to send out the mail"
TO_EMAIL = "the email you want to send to. alternatively this could be a list of mails looped to send out to every one of them"
PASSW0RD ="sending email's password"
parameters= {
    "apiKey": NEWS_API_KEY ,
    "country": "il",
    "category": "sports",
    "q": "מכבי חיפה",
}
response = requests.get(url= "https://newsapi.org/v2/top-headlines", params= parameters)
response.raise_for_status()
data = response.json()
what_i_want = data["articles"][0]["url"]
title =  data["articles"][0]["title"]

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= FROM_EMAIL, password=PASSW0RD)
connection.sendmail(
    from_addr=FROM_EMAIL,
    to_addrs=TO_EMAIL,
    msg=f"Subject: p\n\n {what_i_want}")

connection.close()