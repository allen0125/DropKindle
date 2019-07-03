import os
from dropbox import DropboxOAuth2Flow
import dropbox
from dk_user.models import DKUser
from dk_dropbox.models import UserDropboxHistory
from django.db.models import Q

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


DROPBOX_KEY = os.environ.get("DROPBOX_KEY")
DROPBOX_SECRET = os.environ.get("DROPBOX_SECRET")
DP_REDIRECT_URL = os.environ.get("DP_REDIRECT_URL")

FILE_EXTENSION = ['mobi', 'azw', 'txt', 'doc', 'docx', 'pdf']


def sent_mail(filename, filesrc, toaddr):
    msg = MIMEMultipart('related')
    fromaddr = os.environ.get('MAIL_ADREES')
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
    smtp = smtplib.SMTP_SSL(os.environ.get('SMTP_SSL'))
    smtp.set_debuglevel(1)
    smtp.login(fromaddr, os.environ.get('MAIL_PASSWD'))
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()


def get_dropbox_auth_flow(web_app_session):
    """
    获取 Dropbox Auth 验证流

    """
    DropboxOAuth2Flow(DROPBOX_KEY,
                      DROPBOX_SECRET,
                      DP_REDIRECT_URL)


def get_dropbox_file_list(dk_user):
    """
    通过 dk_user 的 access_token 获取 Dropbox DropKindle应用文件夹内文件列表
    return: dbx_file_list: Dropbox 文件夹中 Dropbox 文件对象列表
    """
    dbx_file_list = []
    dbx = dropbox.Dropbox(dk_user.dropbox_token)
    res = dbx.files_list_folder('', recursive=True)
    _pushed_list = UserDropboxHistory.objects.filter(dk_user=dk_user).values_list('dp_file_value')

    for dbx_file in res.entries:
        if isinstance(dbx_file, dropbox.files.FileMetadata):

            _extension = dbx_file.name.split('.')[-1] in FILE_EXTENSION
            _file_size = dbx_file.size < 20971520
            _not_pushed = dbx_file.content_hash not in _pushed_list

            if _extension and _file_size and _not_pushed:
                dbx_file_list.append(dbx_file)
    return dbx_file_list


def get_tokens():
    """从DKUser当中获取所有token不是空的User
    
    """
    active_users = DKUser.objects.filter(~Q(dropbox_token= ''))
    return active_users
