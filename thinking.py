import random
import requests
from bs4 import BeautifulSoup
import re

# 対象のURL
url = "https://www.weblio.jp/WeblioRandomSelectServlet"

word_list = ["今日は何をした？", "情緒", "世界", "ブイチューバー", "存在", "特定の食べ物について話す", "最近気になってることは？", "どんな夢をみたい？", "明日何をする？", "最近勉強してることは？"]

def generate_word():
    return random.choice(word_list)

def generate_word_temp():
    # requestsを使用してWebページを取得
    response = requests.get(url)
    response.encoding = response.apparent_encoding  # 日本語の文字化けを防ぐためにエンコーディングを設定

    # BeautifulSoupオブジェクトを作成し、HTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 必要なデータを抽出（例：タイトルを取得）
    title = soup.title.text
    match = re.search(r'^(.*?)とは何？', title)
    if match:
        result = match.group(1)
        return result
    else:
        return random.choice(word_list)
