# はじめに
大阪大学駒谷研究室が開発中の音声対話システムのうち，対話制御プログラムから与えられたメッセージを処理し，NAOへ動作命令を送るプロキシプログラムである．

# 開発環境
- OS: Ubuntu 18.04 LTS
- NAO本体: 
    - ハードウェア: V4 (V6でも動作確認済み)
    - OS: 2.1.4.13
- Python: 2.7.16
- Anaconda: 1.7.2
- NAOqi Python SDK: 2.8.6.23
- Choregraphe: 2.1.4

# 導入方法
## 1. Python2.7の導入
**NAOqi Python SDKはPython 3.x系と互換がなく2.7.xでのみ動作する．** このため別途3.x系環境も利用したい場合にはAnacondaなどで個別に環境構築することを推奨．

## 2. NAOqi Python SDKの導入
NAOqi Python SDKを[Softbank Robotics公式](https://developer.softbankrobotics.com/nao6/downloads/nao6-downloads-linux)よりダウンロードし，環境変数に追加
```shellscript
echo export PYTHONPATH=${PYTHONPATH}:/(NAOqi Python SDKの保存場所)/pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/lib/python2.7/site-packages >> ~/.bashrc
```

## 3. 動作フォルダの転送
NAO本体に./behaviorフォルダの内容を転送する．


## 4. behavior.jsonの編集
3で転送した動作フォルダの.xarファイルのNAO上でのディレクトリを記載する．behaviorフォルダをホームディレクリに配置した場合，編集不要．

# 実行方法
start_proxy.shの各項目を編集し，下記コマンドを実行．
```shellscript
sh start_proxy.sh
```

テスト用クライアントプログラムも同様に下記コマンドで実行．
```shellscript
sh start_client.sh
```
## 編集項目
- IP_NAO: NAO本体のIPアドレス
- port_NAO: NAO本体のポート番号
- IP_server: 本プログラムを実行するマシンのIPアドレス
- port_server: 本プログラムを実行するマシンのポート番号
- send_message: {True, False} 動作命令送信後にクライアントにメッセージを返送するかのオプション

クライアントにて
```shellscript
{"(メッセージタイプ)":"(バリュー)"}
```
とjson形式でメッセージを送ると，対応する動作を行う．

現時点では"playmotion"および"say"のメッセージタイプに対応

# 対応メッセージ
## playmotion
behavior.jsonに記されたバリューに対応する動作を実行する．Choregrapheで.xarファイルを作成し，behavior.jsonを編集することで新しい動作の追加が可能
## say
バリューに記された内容を発話する．

