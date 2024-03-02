import chat
import voice
import emotion
import thinking

import time
#import youtube_live
import random

def talk(input_text):
    kawaii_voice = voice.Voice()

    chat.initialize_conversation()
    
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

    kawaii_voice.pya.terminate()

def interact():
    kawaii_voice = voice.Voice()

    chat.initialize_conversation()

    while(1):
        stream = kawaii_voice.setup_stream()

        # ユーザーからのテキスト入力
        input_text = input() 
        if input_text == "q":
            break
        
        #入力に従って感情を変化させる
        emotion.change_emotion_based_on_input(input_text)

        #言語による応答
        output = chat.chat(input_text)
        print(output)

        #音声出力
        try:
            voice.voice(stream, output)
        except:
            continue
        
        stream.stop_stream()
        stream.close()

    kawaii_voice.pya.terminate()

def speak(input_text):
    kawaii_voice = voice.Voice()

    chat.initialize_conversation()
    
    stream = kawaii_voice.setup_stream()
    
    #入力に従って感情を変化させる
    emotion.change_emotion_based_on_input(input_text)

    #言語による応答
    output = chat.speak(input_text)
    print(output)

    #音声出力
    try:
        voice.voice(stream, output)
    except:
        pass
    
    stream.stop_stream()
    stream.close()

    kawaii_voice.pya.terminate()

def live():
    while(1):
        input = youtube_live.get_chat()
        if input:
            talk(input)
        else:
            rand = random.randoint(10)
            if rand == 0:
                speak(thinking.generate())

        time.sleep(5)

if __name__ == "__main__":
    kawaii_voice = voice.Voice()

    chat.initialize_conversation()

    while(1):
        stream = kawaii_voice.setup_stream()

        # ユーザーからのテキスト入力
        input_text = input() 
        if input_text == "q":
            break
        
        #入力に従って感情を変化させる
        emotion.change_emotion_based_on_input(input_text)

        #言語による応答
        output = chat.speak(input_text)
        print(output)

        #音声出力
        try:
            voice.voice(stream, output)
        except:
            continue
        
        stream.stop_stream()
        stream.close()

    kawaii_voice.pya.terminate()