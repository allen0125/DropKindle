import os
from dropbox import DropboxOAuth2Flow
import dropbox


DROPBOX_KEY = os.environ.get("DROPBOX_KEY")
DROPBOX_SECRET = os.environ.get("DROPBOX_SECRET")
REDIRECT_URL = os.environ.get("REDIRECT_URL")


def get_dropbox_auth_flow(web_app_session):
    DropboxOAuth2Flow(DROPBOX_KEY,
                      DROPBOX_SECRET,
                      REDIRECT_URL)


def get_dropbox_file_list(access_token):
    dbx_file_list = []
    dbx = dropbox.Dropbox(access_token)
    res = dbx.files_list_folder('', recursive=True)
    for dbx_file in res.entries:
        if isinstance(dbx_file, dropbox.files.FileMetadata):
            dbx_file_list.append(dbx_file)
    return dbx_file_list
