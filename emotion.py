from gensim.models import Word2Vec
from sklearn.metrics.pairwise import euclidean_distances

from textblob import TextBlob
import unicodedata
import numpy as np
import json


def read_expression_json():
    file_path = "Expression.json"
    with open(file_path, 'r') as file:
        # jsonを辞書型に変換
        data = json.load(file)
    return data

def update_json_parameter(json_data, key, new_value):
    """
    json_data: 辞書に変換されたJSONデータ
    key: 更新したいパラメータのキー
    new_value: 新しい値
    """
    # キーが辞書に存在する場合、値を更新
    if key in json_data:
        json_data[key] = new_value
    else:
        print(f"Key '{key}' not found in JSON data.")
    
    # 更新された辞書を返す
    return json_data



# Word2Vecモデルの訓練（前のステップと同様）
sentences = [['happy',
                'Fun',
                'pleased',
                'Joy',
                'elated',
                'cheerful',
                'joyful',
                'content',
                'delighted',
                'glad',
                'blissful'],
                ['Sorrow',
                'depressed',
                'unhappy',
                'mournful',
                'saddened',
                'melancholic',
                'gloomy',
                'heartbroken',
                'desolate',
                'despairing'],
                ['angry',
                'mad',
                'furious',
                'irate',
                'enraged',
                'incensed',
                'seething',
                'annoyed',
                'agitated',
                'exasperated'],
                ['Neutral',
                'calm',
                'relaxed',
                'serene',
                'peaceful',
                'tranquil',
                'unflustered',
                'composed',
                'unperturbed',
                'stoic']]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=2)

# 感情単語のリストに「Neutral」を追加
emotion_words = ['Fun', 'Sorrow', 'angry', 'Neutral', 'Joy']

# 各感情単語のベクトルを取得
emotion_vectors = np.array([model.wv[word] for word in emotion_words])

try:
    file_path = "Expression.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
        init_emotion = data["expression"]

    # AIの現在の感情を表すベクトルをランダムに初期化
    current_emotion_vector = model.wv[init_emotion].copy()
except:
    init_emotion = "Neutral"

def is_japanese(string):
    for char in string:
        name = unicodedata.name(char, "")
        if "CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name:
            return True
    return False

# 入力テキストに基づいて感情の方向を変える関数
def change_emotion_based_on_input(input_text):
    global current_emotion_vector
    global emotion
    
    blob = TextBlob(input_text)
    
    if is_japanese(input_text):
        try:
            translated_blob = blob.translate(to='en')
            analyzed_text = translated_blob.string
        except Exception as e:
            print(f"Error translating text: {e}")
            analyzed_text = input_text  # 翻訳に失敗した場合は元のテキストを使用
    else:
        analyzed_text = input_text

    blob = TextBlob(analyzed_text)
    polarity = blob.sentiment.polarity
    
    # 極性に基づいて感情方向を選択（ポジティブ、ネガティブ、またはニュートラル）
    if polarity > 0:
        target_emotion = 'Joy'
    elif polarity < 0:
        target_emotion = 'Sorrow'
    else:
        target_emotion = 'Neutral'
    
    # 対象の感情方向に現在の感情ベクトルを少し移動させる
    target_vector = model.wv[target_emotion]
    current_emotion_vector += (target_vector - current_emotion_vector) * 0.5  # 移動量を調整
    
    # 現在の感情と最も近い感情単語を探す
    distances = euclidean_distances(emotion_vectors, [current_emotion_vector])
    nearest_emotion_index = np.argmin(distances)
    emotion = emotion_words[nearest_emotion_index]
    print(f"Input sentiment: {target_emotion}, Current emotion: {emotion}")

    with open(file_path, 'w') as f:
        if emotion == "Joy":
            data = {"expression": "Joy"}
        elif emotion == "Sorrow":
            data = {"expression": "Sorrow"}
        elif emotion == "Fun":
            data = {"expression": "Fun"}
        elif emotion == "Angry":
            data = {"expression": "Angry"}
        else:
            data = {"expression": "Neutral"}
        
        json.dump(data, f)
    
    file_path_to_unity = "Expression2.json"

    # ファイルを読み込み
    with open(file_path_to_unity, 'r') as file:
        data = json.load(file)

    # すべての感情の値を0.0に設定し、指定された感情のみを1.0に設定
    for key in data:
        data[key] = 0.0
    data[emotion] = 0.8

    # 変更を元のファイルに書き戻す
    with open(file_path_to_unity, 'w') as file:
        json.dump(data, file, indent=4)