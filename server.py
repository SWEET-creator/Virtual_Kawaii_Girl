from flask import Flask, jsonify, request, render_template
import json
import core

app = Flask(__name__)

@app.route('/get_expression')
def get_expression():
    file_path = 'Expression2.json'
    try:
        # ファイルを読み取り
        with open(file_path, 'r') as file:
            data = json.load(file)
            # 読み取ったデータをJSONとして返す
            return jsonify(data)
    except FileNotFoundError:
        # ファイルが見つからない場合はエラーメッセージを返す
        return jsonify({"error": "File not found"}), 404

@app.route('/submit_text', methods=['POST'])
def talk():
    data = request.get_json()
    text = data.get('text')
    core.talk(text)

    return jsonify({"message": "Text received successfully", "receivedText": text})

@app.route('/upload', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio_data']
    audio_file.save("received_audio.wav")  # 音声ファイルを保存
    return 'File uploaded successfully', 200

@app.route('/', methods=['GET'])
def get_upload_page():
    return render_template('upload.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
