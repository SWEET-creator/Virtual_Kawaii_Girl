import requests

def get_random_wikipedia_title():
    # Wikipediaのランダムなページを取得するAPIエンドポイント
    url = "https://ja.wikipedia.org/w/api.php"

    # APIリクエストのパラメータ
    params = {
        "action": "query",       # アクションタイプ
        "format": "json",        # レスポンスフォーマット
        "list": "random",        # ランダムなリストを取得
        "rnnamespace": "0",      # 名前空間0（記事のみ）
        "rnlimit": "1"           # 取得する記事の数
    }

    # APIリクエストを送信
    response = requests.get(url, params=params)

    # レスポンスからランダムな記事のタイトルを抽出
    data = response.json()
    title = data['query']['random'][0]['title']

    return title

# ランダムなWikipediaのタイトルを取得して表示
random_title = get_random_wikipedia_title()
print(random_title)
