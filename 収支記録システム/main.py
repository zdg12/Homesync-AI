from ai_module import AIModule
from expense_tracker import ExpenseTracker  # 导入 ExpenseTracker 类

# 初始化 AI 模块
ai_module = AIModule()

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
            note = input("輸入備考：")
            
            # 使用 AI 模块预测类别
            predicted_category = ai_module.predict_category(note)
            print(f"AI 推測類別: {predicted_category}")
            
            # 用户确认或修改类别
            category = input(f"確認類別或修正（預設: {predicted_category}）：") or predicted_category
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