from django.shortcuts import render, redirect
import dropbox
from dropbox import DropboxOAuth2Flow
import os
from django.http import HttpResponse
from dk_user.models import DKUser
from dk_dropbox.utils import get_dropbox_file_list, get_tokens, sent_mail
from dk_dropbox.models import UserDropboxHistory
# Create your views here.
APP_KEY = os.environ.get('DROPBOX_KEY')
APP_SECRET = os.environ.get('DROPBOX_SECRET')
DP_REDIRECT_URL = os.environ.get('DP_REDIRECT_URL')


def get_dropbox_auth_flow(web_app_session):
    return DropboxOAuth2Flow(
        APP_KEY, APP_SECRET, DP_REDIRECT_URL, web_app_session,
        "dropbox-auth-csrf-token")


def dropbox_auth_start(request):
    if request.user.is_authenticated:
        authorize_url = get_dropbox_auth_flow(request.session).start()
        return redirect(authorize_url)
    return redirect('/login/')


def dropbox_auth_finish(request):
    if request.user.is_authenticated:
        oauth_result = \
                get_dropbox_auth_flow(request.session).finish(request.GET)
        dk_user = request.user
        print(dk_user)
        dk_user.dropbox_token = oauth_result.access_token
        dk_user.save()
        return HttpResponse("获取Dropbox Token 成功")
    return redirect('/login/')


def drop_kindle(request):
    if request.user.is_authenticated:
        dk_user = request.user
        if dk_user.dropbox_token:
            dbx = dropbox.Dropbox(dk_user.dropbox_token)
            dropbox_file_list = get_dropbox_file_list(dk_user)
            for doc_file in dropbox_file_list:
                file_path = os.environ.get('DOWNLOAD_DIR') + doc_file.name
                dbx.files_download_to_file(file_path, doc_file.path_lower)
                sent_mail(doc_file.name, file_path, dk_user.email)
                new_history = UserDropboxHistory(dk_user=dk_user, dp_file_name=doc_file.name,
                                                dp_file_value=doc_file.content_hash, push_status=True)
                new_history.save()
                os.remove(file_path)
            return HttpResponse("推送成功！")
        else:
            return HttpResponse("请先获得Dropbox授权")
    return redirect('/login/')
