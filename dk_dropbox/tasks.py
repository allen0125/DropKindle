import os
import datetime
import dropbox
from dk_dropbox.utils import get_dropbox_file_list, get_tokens, sent_mail
from dk_dropbox.models import UserDropboxHistory


def push_doc():
    active_users = get_tokens()
    for dk_user in active_users:
        dbx = dropbox.Dropbox(dk_user.dropbox_token)
        dropbox_file_list = get_dropbox_file_list(dk_user)
        for doc_file in dropbox_file_list:
            print(doc_file.size/1048576)
            file_path = os.environ.get('DOWNLOAD_DIR') + doc_file.name
            dbx.files_download_to_file(file_path, doc_file.path_lower)
            sent_mail(doc_file.name, file_path, dk_user.email)
            new_history = UserDropboxHistory(dk_user=dk_user, dp_file_name=doc_file.name,
                                             dp_file_value=doc_file.content_hash, push_status=True)
            os.remove(file_path)
