import pytchat
import time
import random
from thinking import generate_word

import setting
import core
# PytchatCoreオブジェクトの取得
livechat = pytchat.create(setting.video_id)# video_idはhttps://....watch?v=より後ろの

while livechat.is_alive():
    # チャットデータの取得
    chatdata = livechat.get()
    if chatdata.items:
        for c in chatdata.items:
            print(f"{c.datetime} {c.author.name} {c.message} {c.amountString}")
            core.talk(c.message)
    else: 
        if random.randint(0,10) == 0:
            core.talk(generate_word())

    time.sleep(5)