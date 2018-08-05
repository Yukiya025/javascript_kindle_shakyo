# -*- coding:utf-8 -*-
# このファイルはすべてコピーして新しいテキストファイルにまるっと貼り付ける方法が分からなかったので、bash画面へ出力するためだけのコードです。
# https://qiita.com/Yukiya025/items/c80b143427ceaa343c22
# 別のファイルを操作したいときは変数filenameの中身 (_script.js) を変えればOK!
filename = "_script.js" 

# 対象ファイルはpage1_script.js～page17_script.jsの計17ファイル
# ただし変数iは0からのカウントなので、page17_script.jsは18番目の要素となる
# shiracamusさん、ありがとうございます!
for i in range(1, 18):
    print("////////////////////////")
    print("// page" + str(i) + filename)
    # ファイルを"読み込みモード"で開く
    file_data = open("./JavaScript2/page" + str(i) + filename, "r")
    
    #テキスト全体をまとめて取得
    text = file_data.read()
    
    #取得したテキストを表示
    print text
    
    #開いたファイルを閉じる
    file_data.close()