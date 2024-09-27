import json

# Qiitaのプロフィールデータを読み込み
with open('output/qiita_profile.json', 'r') as file:
    data = json.load(file)

# Qiitaのプロフィール情報から必要なデータを取得
username = data.get('id', 'Unknown User')
followers = data.get('followers_count', 0)
posts = data.get('items_count', 0)
description = data.get('description', 'No description available.')

# HTMLを生成
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qiita Profile</title>
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }}
        .profile-container {{ max-width: 600px; margin: auto; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }}
        h1 {{ color: #2d3748; }}
        p {{ color: #4a5568; }}
        .profile-data {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="profile-container">
        <h1>{username}'s Qiita Profile</h1>
        <p>{description}</p>
        <div class="profile-data">
            <p><strong>Followers:</strong> {followers}</p>
            <p><strong>Posts:</strong> {posts}</p>
        </div>
    </div>
</body>
</html>
"""

# ファイルに保存
with open('output/qiita_profile.html', 'w') as html_file:
    html_file.write(html_content)
