import pickle

class AIModule:
    def __init__(self):
        # モデルとベクトル化ツールをロード
        try:
            with open('model.pkl', 'rb') as model_file, open('vectorizer.pkl', 'rb') as vectorizer_file:
                self.model = pickle.load(model_file)
                self.vectorizer = pickle.load(vectorizer_file)
        except FileNotFoundError:
            print("モデルファイルが見つかりません。まず train_model.py を実行してください！")

    def predict_category(self, note):
        if not hasattr(self, 'model') or not hasattr(self, 'vectorizer'):
            return "予測できません。モデルがロードされていません！"
        vectorized_input = self.vectorizer.transform([note])
        predicted_category = self.model.predict(vectorized_input)
        return predicted_category[0]

# 使用例
if __name__ == "__main__":
    ai = AIModule()
    print(ai.predict_category("ミルクティーを買った"))

