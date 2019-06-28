# -*- coding: utf-8 -*-

'''
@Author  : Allen
@Site    : allen0125.com
@E-mail  : me@allen0125.com


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from dropbox import DropboxOAuth2Flow
import setting as ST


def get_dropbox_auth_flow(web_app_session):
    redirect_url = ST.REDIRECT_URL
    DropboxOAuth2Flow(ST.APP_KEY,
                      ST.APP_SECRET,
                      redirect_url)
