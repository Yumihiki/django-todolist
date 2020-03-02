# TODOリスト

PythonフレームワークのDjangoで作成するシンプルなTODOリストです。
自作のオリジナルアプリのアイデアをまとめることを目的としています。

## 作業手順

仮想環境の構築
python3 -m venv myvenv

仮想環境の作成
source myvenv/bin/activate

pipのインストール
python -m pip install --upgrade pip

Djangoのインストール（requirements.txtにDjangoのバージョンを記載）
pip install -r requirements.txt

データベースの作成
python manage.py migrate

開発用サーバーの実行
python manage.py runserver

モデルに変更があった場合
python manage.py makemigrations ToDoList

管理者を作成する場合
python manage.py createsuperuser

入力する項目

Username: 任意の名前
Email Adress: 任意の名前
Password: 任意のパスワード

## 追記する時の流れ

1. urls.pyに追加
1. views.pyに追加
1. htmlなどを実際に記述

参考URL
[DjangoGirlsTurorial](https://tutorial.djangogirls.org/ja/django_installation/)
