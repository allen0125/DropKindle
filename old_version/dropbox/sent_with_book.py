import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import setting as ST
import os


def sent_mail(filename, filesrc, toaddr):

    msg = MIMEMultipart('related')
    fromaddr = ST.MAIL_ADREES
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'DropKindle Sent' + os.path.basename(filename)

    # 邮件正文
    text = MIMEText('Thx for use DropKindle', 'plain', 'utf-8')
    msg.attach(text)

    # 邮件附件
    att = MIMEText(open(filesrc, 'rb').read(), 'base64', 'gbk')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
    msg.attach(att)
    smtp = smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.set_debuglevel(1)
    smtp.login(fromaddr, ST.MAIL_PASSWD)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()
