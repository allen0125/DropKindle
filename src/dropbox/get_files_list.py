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

import dropbox
import setting as ST
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Boolean
from sent_with_book import sent_mail, sent_mail_test
import time

engine = create_engine('mysql+pymysql://root@localhost:3306/dropkindle')
Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(String(45))
    book_name = Column(String(80))
    content_hash = Column(String(80))
    is_sent = Column(Boolean)


while True:
    time.sleep(10)
    dbx = dropbox.Dropbox(ST.GEN_ACCESS_TOKEN)
    res = dbx.files_list_folder('', recursive=True)
    buffer_list = []
    check_now_list = []
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    books_in_db = session.query(Book)
    for item in books_in_db:
        buffer_list.append(item.content_hash)
    for doc_file in res.entries:
        if isinstance(doc_file, dropbox.files.FileMetadata):
            if doc_file.content_hash in buffer_list:
                print("In DB:" + doc_file.name + '\n' + doc_file.content_hash)
            else:
                print("Insert DB: " + doc_file.name + '\n' + doc_file.content_hash)
                new_book = Book(id_user='allen0125', book_name=doc_file.name, content_hash=doc_file.content_hash,
                                is_sent=True)
                session.add(new_book)
                dbx.files_download_to_file('download_buffer/%s' % doc_file.name, doc_file.path_lower)
                sent_mail_test(doc_file.name, 'download_buffer/%s' % doc_file.name, ST.TO_ADDR)
    session.commit()
    session.close()
