import pytchat
import time
import random
from thinking import generate_word
import voice
import setting
import chat
import emotion

def chat_with_voice(input_text):
    stream = kawaii_voice.setup_stream()

    #入力に従って感情を変化させる
    emotion.change_emotion_based_on_input(input_text)
    
    #言語による応答
    output = chat.chat(input_text)
    print(output)

    #音声出力
    try:
        voice.voice(stream, output)
    except:
        pass

    stream.stop_stream()
    stream.close()


# PytchatCoreオブジェクトの取得
livechat = pytchat.create(setting.video_id)# video_idはhttps://....watch?v=より後ろの

kawaii_voice = voice.Voice()

chat.initialize_conversation()

while livechat.is_alive():

    # チャットデータの取得
    chatdata = livechat.get()
    if chatdata.items:
        for c in chatdata.items:
            print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
            input_text = c.message
            print(input_text)

            chat_with_voice(input_text)
    else: 
        if random.randint(0,1) == 0:

            input_text = generate_word()
            print(input_text)
            
            chat_with_voice(input_text)

    time.sleep(5)

kawaii_voice.pya.terminate()