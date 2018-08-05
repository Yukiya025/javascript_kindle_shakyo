# -*- coding:utf-8 -*-

import os
import extract
files = os.listdir('./codes')
filenum = len(files) + 1

with open('./output.txt', 'w+') as f:
    for file_name in extract.extract_files("./codes", ".js"):
        with open(file_name, 'r') as file_data:
            f.write('/' * 24 + '\n//' + os.path.basename(file_name) + '\n' + file_data.read() + '\n')
