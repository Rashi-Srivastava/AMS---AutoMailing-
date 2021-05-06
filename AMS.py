#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:15:32 2020

"""

import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import os
from email.mime.application import MIMEApplication


port=465

password=input("Enter Password:")
sender="example@gmail.com"

df = pd.read_csv(r"/home/rashi/Documents/Projects/AMS/FL1.csv")

f = 0
for i in df.iterrows():
    
    recv = df.iloc[f]["Email"]
    print(recv)
    subject="Subject Line"
    X = df.iloc[f]["X"]  #Receiver's name in the csv file
    Y = df.iloc[f]["Y"]  #Receiver's designation in the csv file 
    M = df.iloc[f]["M"]  #Any data which should vary in all the mails.
    
    
    body="""To\n"""+X+"\n"+"\n"+Y+"""
    
Basic para here """+M+""" rest of the body here"""
    message=MIMEMultipart()
    message["From"]= "Sender's name"
    message["To"]=recv
    message["Subject"]=subject
    message.attach(MIMEText(body,"plain"))
    
    
    dirpath = "folder containg the attachments"
   
    filename=["name of different files to besent as attachment"]
        
    for p in filename:  # add files to the message
        file_path = os.path.join(dirpath, p)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="pdf")
        attachment.add_header('Content-Disposition','attachment', filename=p)
        message.attach(attachment)
    
    
    """with open(file,'rb') as attach:
        part=MIMEBase("application", "octet-stream")
        part.set_payload(attach.read())
        
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; Filename= {filename}",
    )"""
    
    
    #message.attach(part)
    text=message.as_string()
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,recv,text)
    f = f+1
