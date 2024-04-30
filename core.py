import chat
import voice
import emotion
import vision
import time
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

def translate_to_jp(texts):
    dic = {"person" : "人", "book" : "本", "tv" : "テレビ", "cell phone" : "携帯電話"}
    return [dic[x] for x in texts]

def main(only_text=False):
    global input_text

    # こえをだすじゅんび
    kawaii_voice = voice.Voice()

    # はなすじゅんび
    chat.initialize_conversation()

    while(1):
        stream = kawaii_voice.setup_stream()

        input_text = None

        if only_text:
            input_text = input()
        elif random.randrange(2):
            input_text = input()
        
        if input_text:
            if input_text == "q":
                break

            #入力に従って感情を変化させる
            emotion.change_emotion_based_on_input(input_text)

            #言語による応答
            output = chat.chat(input_text)
            print(output)
        else:
            labels = vision.get_labels()

            labels = translate_to_jp(labels)

            labels = "".join(labels)

            input_text = labels + "が目の前にあります"
            print(labels)

            #入力に従って感情を変化させる
            emotion.change_emotion_based_on_input(input_text)

            #言語による応答
            output = chat.chat(input_text, role = "system")
            print(output)

        #音声出力
        try:
            voice.voice(stream, output)
        except:
            continue
        
        # ひといきつく
        stream.stop_stream()
        stream.close()
        
        time.sleep(3)

    kawaii_voice.pya.terminate()

def talk2():
    global input_text

    # こえをだすじゅんび
    kawaii_voice = voice.Voice()

    # はなすじゅんび
    chat.initialize_conversation()

    while(1):
        stream = kawaii_voice.setup_stream()

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
        
        # ひといきつく
        stream.stop_stream()
        stream.close()

    kawaii_voice.pya.terminate()


if __name__ == "__main__":
    talk2()