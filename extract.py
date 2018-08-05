# -*- coding:utf-8 -*-
# codesフォルダのファイル名を取得
# [_]以降のファイル名を取得
# print() する
import glob
import os

filelistname = ""
index = 0
def extract_files(path, ext):
    for file_name in sorted(glob.glob(path + "/*" + ext)):
        print(file_name) 
        yield file_name
