import datetime
from datetime import datetime as dt
import time
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import glob

#_________###informations###___________________###
from_addr = 'from_adress@gmail.com'
to_addr = 'to_adress1@gmail.com'
to_addr2 = 'to_adress2@gmail.com'
subject = 'current data'
content = 'IMPORTANT NOTICE:  This email and any attachments may contain information that is confidential and privileged. It is intended to be received only by persons entitled to receive the information. If you are not the intended recipient, please delete it from your system and notify the sender. You should not copy it or use it for any purpose nor disclose or distribute its contents to any other person.'
msg = MIMEMultipart()
msg['from'] = from_addr
msg['to'] = to_addr
msg['subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)
###_____________________###server###______________________###
#_make sure to use the right port_#
server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_addr, 'password')

###___________###seting different sending times###_____________###
dt.now()
T = datetime.datetime.now()
M = dt.now().minute
XT = T.replace(hour=00, minute=10)
XM1 = T.replace(minute=00)
XM2 = T.replace(minute=15)
XM3 = T.replace(minute=30)
XM4 = T.replace(minute=45)
#____________________________________________________________________#
files = glob.glob("folder/path/*.csv")
modified_files = list()
current_time = time.time()
###________________###main_fonction###__________________________###
# on T=XT programm  test if any .csv file is added to the folder and send it to 'to_adress'#

# on other  'T'  programme does the  same test but send the added .csv files to 'to_adress2'#


def main():
    if T == XT:
        for csv_file in files:
            time_delta = current_time - os.path.getctime(csv_file)
            time_delta_days = time_delta / (60*15)
            if time_delta_days < 1 or time_delta_days == 1:
                modified_files.append(csv_file)
        print(modified_files)
        for file in modified_files:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(file, 'rb').read())
            part.add_header('Content-Disposition',
                            'attachment; filename="%s"' % file)
            msg.attach(part)
        server.send_message(msg, from_addr, to_addr)
        time.sleep(60)
    if T == XM1 or T == XM2 or T == XM3 or T == XM4:
        for csv_file in files:
            time_delta = current_time - os.path.getctime(csv_file)
            time_delta_days = time_delta / (60*15)
            if time_delta_days < 1 or time_delta_days == 1:
                modified_files.append(csv_file)
        print(modified_files)
        for file in modified_files:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(file, 'rb').read())
            part.add_header('Content-Disposition',
                            'attachment; filename="%s"' % file)
            msg.attach(part)
        server.send_message(msg, from_addr, to_addr2)
        time.sleep(60)


while True:
    main()
