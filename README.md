# 収支記録システム
![微信截图_20250108182625](https://github.com/user-attachments/assets/55cbbaf7-1e61-4d63-b0a1-336e96bdffc1)
# 概要
本システムは、家庭や個人の日常的な収支を簡単に記録し、管理することができるアプリケーションです。
シンプルな操作で、収支記録、月次の収支集計、カテゴリ別の分類を行い、家計を効率的に管理するための支援をします。
# 使用技術
本プロジェクトは、Pythonを使用して開発され、データ管理のためにSQLiteデータベースを活用しています。
軽量で迅速に動作するよう設計されています。
プログラミング言語: Python
データベース: SQLite
ライブラリ:
Tabulate（データの表形式出力）
datetime（日時管理）
# システム構成図
![微信图片_20250108183022](https://github.com/user-attachments/assets/d1b91c88-b055-4b30-ab09-e5d7fa792cb2)
# 使い方
Pythonをインストールし、依存ライブラリ（tabulate）を導入します。
以下のコマンドを実行してください：
pip install tabulate
プログラムを実行して、画面の指示に従って操作します。
実行コマンド：
python expense_tracker.py
以下の操作を行うことができます：
収支の記録追加：金額、カテゴリ、メモ、日付を入力。
記録の一覧表示：すべての記録を表形式で表示。
月次収支の集計：指定月の収支総額、収入、支出を表示。
記録の削除：不要な記録を削除。
