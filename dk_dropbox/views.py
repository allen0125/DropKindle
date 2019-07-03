from django.shortcuts import render, redirect
import dropbox
from dropbox import DropboxOAuth2Flow
import os
from django.http import HttpResponse
from dk_user.models import DKUser

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
