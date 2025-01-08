import sqlite3
from datetime import datetime
from tabulate import tabulate

# 数据库类
class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                note TEXT,
                date TEXT
            )
        """)
        self.conn.commit()

    def add_transaction(self, amount, category, note, date):
        self.cursor.execute("""
            INSERT INTO transactions (amount, category, note, date)
            VALUES (?, ?, ?, ?)
        """, (amount, category, note, date))
        self.conn.commit()
        print("記録を追加した")

    def view_transactions(self):
        self.cursor.execute("SELECT id, amount, category, note, date FROM transactions ORDER BY date DESC")
        transactions = self.cursor.fetchall()
        if transactions:
            print(tabulate(transactions, headers=["ID", "金額", "類別", "備考", "日付"], tablefmt="grid"))
        else:
            print("記録がない！")

    def monthly_summary(self, month):
        self.cursor.execute("""
            SELECT SUM(amount) FROM transactions
            WHERE date LIKE ?
        """, (f"{month}%",))
        total = self.cursor.fetchone()[0]
        income = self.cursor.execute("""
            SELECT SUM(amount) FROM transactions WHERE amount > 0 AND date LIKE ?
        """, (f"{month}%",)).fetchone()[0]
        expense = self.cursor.execute("""
            SELECT SUM(amount) FROM transactions WHERE amount < 0 AND date LIKE ?
        """, (f"{month}%",)).fetchone()[0]

        print(f"\n=== {month} 月統計 ===")
        print(f"収入: {income or 0:.2f}")
        print(f"支出: {abs(expense or 0):.2f}")
        print(f"残り: {total or 0:.2f}\n")

    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.conn.commit()
        print("記録を削除した！")

    def close(self):
        self.conn.close()

# 主程序
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== 家庭收支記録システム ===")
        print("1. 記録追加")
        print("2. 記録確認")
        print("3. 月度統計")
        print("4. 記録削除")
        print("5. 退出")

        choice = input("操作選択（1-5）：")

        if choice == "1":
            amount = float(input("輸入金額（正は収入，負は支出）："))
            category = input("輸入類別（食品、飲み物など）：")
            note = input("輸入備考：")
            date = input("輸入日付（YYYY-MM-DD，デフォルト今日を設定）：") or datetime.now().strftime("%Y-%m-%d")
            tracker.add_transaction(amount, category, note, date)
        elif choice == "2":
            tracker.view_transactions()
        elif choice == "3":
            month = input("輸入月分(形式 YYYY-MM):")
            tracker.monthly_summary(month)
        elif choice == "4":
            transaction_id = int(input("削除された記録を入力"))
            tracker.delete_transaction(transaction_id)
        elif choice == "5":
            tracker.close()
            print("プログラム終了")
            break
        else:
            print("無効選択")

if __name__ == "__main__":
    main()
