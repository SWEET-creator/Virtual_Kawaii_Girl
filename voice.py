import json
import requests

import pyaudio

class Voice():
    def __init__(self):
        self.pya = pyaudio.PyAudio()
    
    def setup_stream(self):
        stream = self.pya.open(format=pyaudio.paInt16,
                channels=1,
                rate=24000,
                output_device_index = 14,
                output=True)
        return stream


def voice(stream, text):
    # エンジン起動時に表示されているIP、portを指定
    host = "127.0.0.1"
    port = 50021
    
    # 音声化する文言と話者を指定(3で標準ずんだもんになる)
    params = (
        ('text', text),
        ('speaker', 2),
    )
    
    # 音声合成用のクエリ作成
    query = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )
    
    # 音声合成を実施
    synthesis = requests.post(
        f'http://{host}:{port}/synthesis',
        headers = {"Content-Type": "application/json"},
        params = params,
        data = json.dumps(query.json())
    )
    
    # 再生処理
    voice = synthesis.content
    
    stream.write(voice)