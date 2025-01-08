import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# サンプルのトレーニングデータ
data = {
    'note': ['コーヒーを買った', 'バスに乗った', '服を購入', '家賃を支払う', '夕食会', '給油', '本を買う'],
    'category': ['食品', '交通', '買い物', '住宅', '食品', '交通', '学習']
}
df = pd.DataFrame(data)

# 特徴抽出
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['note'])
y = df['category']

# 分類モデルのトレーニング
model = MultinomialNB()
model.fit(X, y)

# モデルとベクトル化ツールを保存
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("モデルとベクトル化ツールが保存されました！")
