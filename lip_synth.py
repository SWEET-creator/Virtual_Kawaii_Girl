import os
import time
import random
import soundfile as sf
import simpleaudio as sa
import socket
import multiprocessing
from multiprocessing import Manager, Value, Process
import voice

machines = ['localhost', 'mac']
ips = ['', '192.168.50.9']
modules = ['mouth_module']
ports = [11121]
host = 'localhost'
#host = 'mac'
sock_lip = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def lip_control(is_talking, mouth, host):
    while True:
        # Vary lip and emotion
        if is_talking.value == 1:
            # Random lip sync
            mouth.value = random.randrange(0, 10, 1) * 0.1
        else:
            # Close mouth
            mouth.value = 0.0
        # Send to Unity
        try:
            send_lip(mouth.value, sock_lip,
                     ips[machines.index(host)], ports[modules.index('mouth_module')])
        except:
            print('send_lip BrokenPipeError')


def send_lip(mouse_status, sock, host, port):
    message = '{0}'.format(mouse_status).encode('utf-8')
    sock.sendto(message,(host,port))
    time.sleep(0.1)
    return


def load_tts(model_path):
    fs, lang = 44100, "Japanese"
    text2speech = Text2Speech(
        model_file=model_path,
        device="cuda",
        speed_control_alpha=1.2,
        noise_scale=0.333,
        noise_scale_dur=0.333,
    )
    return text2speech


def main():
    # こえをだすじゅんび
    kawaii_voice = voice.Voice()

    stream = kawaii_voice.setup_stream()

    
    # 読み上げる文章
    text = "こんにちは、今日はいい天気ですね"

    with Manager() as manager:
        is_talking = manager.Value('i', 0)
        mouth = manager.Value('d', 0.0)

        # Unityへ口の開度を送信する
        lip_p = Process(target=lip_control, args=[is_talking, mouth, host])
        lip_p.start()

        try:
            voice.voice(stream, text)
        except:
            pass
        
        # ひといきつく
        stream.stop_stream()
        stream.close()

        lip_p.terminate()
    
    kawaii_voice.pya.terminate()


if __name__ == '__main__':
    main()