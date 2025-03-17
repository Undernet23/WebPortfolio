import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "dobrea.marian.23@gmail.com"
password = "bbavokyrzmmlhgjl"

receiver = "dobrea.marian.23@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hello ! 
Hi !
How are you ?
Bye !
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
