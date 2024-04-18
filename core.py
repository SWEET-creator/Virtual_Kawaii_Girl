import chat
import voice
import emotion
import vision

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

def main():
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


if __name__ == "__main__":
    main()