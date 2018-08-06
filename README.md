# このプログラムの目的
ひとつにまとめたい複数のファイルをcodesフォルダに放り込んでjavascript_kindle.pyを実行すると、プロジェクト直下にoutput.txtというファイルを生成してくれるよ!
複数あるファイルをひとつにまとめてkindleに送信したいよっていう方の助けになります。

または写経目的やコードいじり目的でもOK! 当方、ProgateでPython全コースクリアしたばかりの砂粒プログラマです。
「pythonだけで実用的なコードって何がある?」という方のニーズにも応えるかも。

# 実際に動かす前の注意点
1. codesフォルダのdeletethisfile_itsdummy.txtは削除してください。削除しなかった場合、このファイル内容もひとつにまとめられます。削除する前に中身が見たければどうぞ。
2. codesフォルダにあなたがひとつにまとめたいファイルを、拡張子を揃えて放り込んでください。
3. javascript_kindle.pyを開き、ひとつにまとめたいファイルの拡張子が.jsでない場合は`for file_name in extract.extract_files("./codes", ".js"):`の".js"部分を該当の拡張子に変更してください。


     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Python project on Cloud9 IDE!

To show what Cloud9 can do, we added a basic sample web application to this
workspace, from the excellent Python tutorial _Learning Python the Hard Way_.
We skipped ahead straight to example 50 which teaches how to build a web
application.

If you've never looked at the tutorial or are interested in learning Python,
go check it out. It's a great hands-on way for learning all about programming
in Python.

* _Learning Python The Hard Way_, online version and videos: 
http://learnpythonthehardway.org/book/

* Full book: http://learnpythonthehardway.org

## Starting from the Terminal

To try the example application, type the following in the terminal:

```
cd ex50
python bin/app.py
```

Alternatively, open the file in ex50/bin and click the green Run
button!

## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide.