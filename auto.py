import pytchat
import time
import random
from thinking import generate_word
import voice
import setting
import chat
import emotion

def chat_with_voice(input_text, kawaii_voice, role = "user"):
    stream = kawaii_voice.setup_stream()

    #入力に従って感情を変化させる
    emotion.change_emotion_based_on_input(input_text)
    
    #言語による応答
    output = chat.chat(input_text, role)
    print(output)

    #音声出力
    try:
        voice.voice(stream, output)
    except:
        pass

    stream.stop_stream()
    stream.close()


def live(kawaii_voice):
    # PytchatCoreオブジェクトの取得
    livechat = pytchat.create(setting.video_id)# video_idはhttps://....watch?v=より後ろの

    while livechat.is_alive():

        # チャットデータの取得
        chatdata = livechat.get()
        if chatdata.items:
            for c in chatdata.items:
                print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
                input_text = c.message
                print(input_text)

                chat_with_voice(input_text, kawaii_voice)
        else: 
            if random.randint(0,1) == 0:

                input_text = generate_word()
                print(input_text)
                
                chat_with_voice(input_text, kawaii_voice, role = "system")


        time.sleep(5)

def automatical_talk(kawaii_voice):
    cnt = 0
    while cnt < 20:
        if random.randint(0,1) == 0:

            input_text = generate_word()
            print(input_text)
            
            chat_with_voice(input_text, kawaii_voice, role = "system")

        time.sleep(3)
        cnt += 1

def main():

    live_mode = False

    kawaii_voice = voice.Voice()

    chat.initialize_conversation()

    if live_mode:
        live(kawaii_voice)
    else:
        automatical_talk(kawaii_voice)

    kawaii_voice.pya.terminate()


if __name__ == "__main__":
    main()