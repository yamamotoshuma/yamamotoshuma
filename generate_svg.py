import json
import matplotlib.pyplot as plt

# Qiitaのプロフィールデータを読み込み
with open('output/qiita_profile.json', 'r') as file:
    data = json.load(file)

# Qiitaのプロフィールから、フォロワー数などを取得
followers = data.get('followers_count', 0)
posts = data.get('items_count', 0)
contributions = data.get('contribution', 0)  # Qiitaに貢献したポイントがあれば

# グラフを生成
labels = ['Followers', 'Posts', 'Contributions']
values = [followers, posts, contributions]

plt.figure(figsize=(6, 4))
plt.bar(labels, values, color=['#FF8C00', '#4682B4', '#32CD32'])
plt.title('Qiita Profile Overview')

# SVGとして保存
plt.savefig('output/qiita_profile.svg', format='svg')
