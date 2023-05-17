 server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("kalraj000000@gmail.com","syardnuypssianjd")
    from_ = "kalraj000000@gmail.com"
    to_ = list_of_emails[i]
    message = MIMEMultipart("multipart")
    message['Subject'] = "This is a testing message"
    message["from"] = "kalraj000000@gmail.com" #try single quotation
    
    pagal = "Hi " + list_of_name[i] +  ", yes I am personally sending you this. \n " 
    pagal2 = "and I might know a lot about you."+" Yes "+list_of_name[i]+", you heard me.\n"
    pagal3 = "Your age is "+ list_of_age[i]+"and you like playing"+ list_of_interest[i]+"\n"
    text =MIMEText(pagal,"plain")
    text2 =MIMEText(pagal2,"plain")
    text3 =MIMEText(pagal3,"plain")
    # html = '''
    # <html>
    # <body>
    # <h1> Image </h1>
    # <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Viktor_Bout.jpg/248px-Viktor_Bout.jpg> </img>
    # </body>
    # </html>
    # '''
    # text2 = MIMEText(html,"html")

    html2 = '''
    <html>
    <body>
    <p>So, the main purpose for typing this mail, is to show through a visual confirmation that in this image its looking as if its suyash's bday but, it's jaideep's.</p>
    <img src="https://i.postimg.cc/MTN4kZRc/Whats-App-Image-2022-12-14-at-20-48-13.jpg"> 
    <p> image ^-^ </p>
    </body>
    </html>
    '''
    text_html = MIMEText(html2,"html")

    message.attach(text)
    message.attach(text2)
    message.attach(text3)
    # message.attach(text2)
    message.attach(text_html)
    server.sendmail(from_,to_,message.as_string())
    i= i+1

print("message has been sent to the mails.")
print(i)

# except Exception as e:
#     print(e)