import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import setting as ST


def sent_mail(filename, filesrc, toaddr):
    fromaddr = ST.MAIL_ADREES
    # toaddr = "wangyao0125@126.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Test Sent File From DropKindle"

    body = "DropKindle Service"

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filesrc, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename, encoders='utf-8')

    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.set_debuglevel(1)
    server.login(fromaddr, ST.MAIL_PASSWD)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
